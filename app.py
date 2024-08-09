import os
import json
from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)

LOG_FILE_PATH = 'logs/search_logs.json'

def log_search(phrase, search_type):
    log_entry = {
        "last_search_time": datetime.now().isoformat(),
        "search_phrase": phrase,
        "search_type": search_type,
        "frequency": 1
    }
    
    if not os.path.exists('logs'):
        os.makedirs('logs')

    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r+') as file:
            logs = json.load(file)
            # Check if the phrase already exists in the logs
            found = False
            for log in logs:
                if log["search_phrase"] == phrase and log["search_type"] == search_type:
                    log["frequency"] += 1
                    log["last_search_time"] = datetime.now().isoformat()
                    found = True
                    break
            if not found:
                logs.append(log_entry)
            file.seek(0)
            json.dump(logs, file, indent=4)
    else:
        with open(LOG_FILE_PATH, 'w') as file:
            json.dump([log_entry], file, indent=4)

def search_wikipedia(query, limit=10):
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": limit
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
        "srnamespace": 6,
        "format": "json",
        "srlimit": limit
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
        limit = int(request.form.get("limit", 10))

        # Check if the user opted out of logging
        opt_out = request.form.get("opt_out")

        if opt_out != "yes":
            # Log the search request if the user did not opt out
            log_search(query, search_type)

        if search_type == "image":
            results = search_images(query, limit)
        else:
            results = search_wikipedia(query, limit)
        return render_template("results.html", results=results, query=query, search_type=search_type)
    return render_template("index.html")

@app.route("/stats")
def view_stats():
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as file:
            logs = json.load(file)
    else:
        logs = []
    return render_template("stats.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
