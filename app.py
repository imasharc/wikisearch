from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def search_wikipedia(query, limit=10):
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": limit  # Use the limit parameter to control the number of results
    }
    
    response = requests.get(search_url, params=search_params)
    data = response.json()
    
    results = []
    for item in data["query"]["search"]:
        title = item["title"]
        page_id = item["pageid"]
        snippet = item.get("snippet", "")
        snippet = snippet.replace('<span class="searchmatch">', '').replace('</span>', '')
        url = f"https://en.wikipedia.org/?curid={page_id}"
        results.append({
            "title": title,
            "description": snippet,
            "url": url
        })
    
    return results

def search_images(query, limit=10):
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srnamespace": 6,  # Namespace 6 is for files
        "format": "json",
        "srlimit": limit  # Use the limit parameter to control the number of results
    }
    
    response = requests.get(search_url, params=search_params)
    data = response.json()
    
    images = []
    for item in data["query"]["search"]:
        title = item["title"]
        page_id = item["pageid"]
        imageinfo_url = "https://en.wikipedia.org/w/api.php"
        imageinfo_params = {
            "action": "query",
            "titles": title,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json"
        }
        imageinfo_response = requests.get(imageinfo_url, params=imageinfo_params)
        imageinfo_data = imageinfo_response.json()
        pages = imageinfo_data["query"]["pages"]
        for page in pages.values():
            if "imageinfo" in page:
                images.append({
                    "title": title,
                    "url": page["imageinfo"][0]["url"]
                })
    
    return images

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_type = request.form.get("search_type")
        query = request.form.get("query")
        limit = int(request.form.get("limit", 10))  # Default to 10 if no limit is provided
        if search_type == "image":
            results = search_images(query, limit)
        else:
            results = search_wikipedia(query, limit)
        return render_template("results.html", results=results, query=query, search_type=search_type)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
