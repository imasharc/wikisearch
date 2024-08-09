document.addEventListener("DOMContentLoaded", function () {
  const searchTypeRadios = document.querySelectorAll(
    'input[name="search_type"]'
  );
  const searchInputContainer = document.getElementById(
    "search-input-container"
  );

  searchTypeRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      searchInputContainer.innerHTML =
        '<input type="text" id="query" name="query" placeholder="Enter search term" required>';
    });
  });
});

function toggleImage(url, index) {
  const container = document.getElementById("image-container-" + index);
  const imageElement = document.getElementById("image-" + index);
  const sourceLink = document.getElementById("source-link-" + index);

  // Hide all other image containers and source links
  document
    .querySelectorAll(".image-container")
    .forEach(function (otherContainer) {
      if (otherContainer !== container) {
        otherContainer.style.display = "none";
        const otherImage = otherContainer.querySelector("img");
        const otherSourceLink = otherContainer.querySelector(".source-link");
        if (otherImage) {
          otherImage.src = "";
        }
        if (otherSourceLink) {
          otherSourceLink.style.display = "none";
        }
      }
    });

  if (container.style.display === "block") {
    container.style.display = "none";
    imageElement.src = "";
    sourceLink.style.display = "none";
  } else {
    container.style.display = "block";
    imageElement.src = url;
    sourceLink.style.display = "block";
  }
}

function toggleArticle(url, index) {
  const container = document.getElementById("article-container-" + index);
  const iframe = document.getElementById("article-frame-" + index);
  const sourceLink = document.getElementById("source-link-" + index);

  // Hide all other article containers and source links
  document
    .querySelectorAll(".article-container")
    .forEach(function (otherContainer) {
      if (otherContainer !== container) {
        otherContainer.style.display = "none";
        const otherIframe = otherContainer.querySelector("iframe");
        const otherSourceLink = otherContainer.querySelector(".source-link");
        if (otherIframe) {
          otherIframe.src = "";
        }
        if (otherSourceLink) {
          otherSourceLink.style.display = "none";
        }
      }
    });

  if (container.style.display === "block") {
    container.style.display = "none";
    iframe.src = "";
    sourceLink.style.display = "none";
  } else {
    container.style.display = "block";
    iframe.src = url;
    sourceLink.style.display = "block";
  }
}
