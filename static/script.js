function toggleArticle(url, index) {
  // Get the selected article container and iframe
  var container = document.getElementById("article-container-" + index);
  var iframe = document.getElementById("article-frame-" + index);

  // Check if the container is currently displayed
  if (container.style.display === "block") {
    // Hide the container if it is already displayed
    container.style.display = "none";
  } else {
    // Hide all article containers
    document
      .querySelectorAll(".article-container")
      .forEach(function (container) {
        container.style.display = "none";
      });
    // Show the selected article container and set the iframe src
    container.style.display = "block";
    iframe.src = url;
  }
}
