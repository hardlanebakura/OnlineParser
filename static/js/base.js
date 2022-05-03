var currentLink = window.location.href.split("/").slice(3);
var headerMenuItem = document.getElementsByClassName("header_menu_item");
var headerLink = document.getElementsByClassName("header_link");
var listOfLinkNames = Array.from(document.getElementsByClassName("header_link")).map(e => e.innerText.toLowerCase());
var searchButton = document.getElementsByClassName("header_search_button")[0];
var searchMenu = document.getElementsByClassName("search_menu")[0];

Array.from(headerLink).forEach(element => {

    element.classList.remove("active");
    listOfLinkNames.forEach(linkName => {

        if (currentLink.includes(linkName)) headerLink[listOfLinkNames.indexOf(linkName)].style.color = "red";

    })

})

searchButton.addEventListener("click", event => {

    searchMenu.style.display = "flex";
    searchMenu.style.justifyContent = "center";
    searchMenu.style.alignItems = "center";

})

