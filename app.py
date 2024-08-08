from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def search_wikipedia(query):
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 10,  # Limit the number of results to 10
    }
    
    response = requests.get(search_url, params=search_params)
    data = response.json()
    
    results = []
    for item in data["query"]["search"]:
        title = item["title"]
        page_id = item["pageid"]
        snippet = item.get("snippet", "")
        # Remove HTML tags from snippet
        snippet = snippet.replace('<span class="searchmatch">', '').replace('</span>', '')
        url = f"https://en.wikipedia.org/?curid={page_id}"
        results.append({
            "title": title,
            "description": snippet,
            "url": url
        })
    
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        results = search_wikipedia(query)
        return render_template("results.html", results=results, query=query)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
