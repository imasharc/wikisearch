# [Flask Wikipedia Search](https://trywikisearch.azurewebsites.net/)

This project is a simple web application built using Flask that allows users to search Wikipedia articles. The application fetches the top search results from Wikipedia and displays them. Users can click on the article titles to view the embedded Wikipedia article directly on the page or open the article in a new tab. User can also search for images, view them and go to their source link.

## Features

- Search Wikipedia articles by entering a search term.
- Display set limit of search results with titles, snippets, and links.
- Display set limit of image results with titles, media, and source links.
- Click on article titles to toggle the embedded Wikipedia article within the page.
- Click on image title to toggle the original image within the page.
- Open the full Wikipedia article/image in a new tab.

## Prerequisites

- Python 3.8 or higher
- Flask
- Requests

## Setup

### Windows

1. **Clone the repository**:

   git clone https://github.com/yourusername/wikisearch.git

   cd wikisearch

2. **Run the setup script**:

   ./setup.bat

3. **Activate the virtual environment and start the application**:

   venv\Scripts\activate

   python app.py

### Unix-based Systems (Linux/Mac)

1. **Clone the repository**:

   git clone https://github.com/yourusername/wikisearch.git

   cd wikisearch

2. **Run the setup script**:
   ./setup.sh

3. **Activate the virtual environment and start the application**:

   source venv/bin/activate

   python app.py

## Usage

1. **Navigate to the home page**:

   Open your web browser and go to http://localhost:5000.

2. **Search for articles**:

   Enter a search term and click "Search". The top 10 search results from Wikipedia will be displayed.

3. **View articles**:

   Click on the article title to toggle the embedded article within the page.

   Click on "Go to article" to open the full Wikipedia article in a new tab.
