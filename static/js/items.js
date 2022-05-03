var pageMenuItem = document.getElementsByClassName("page_menu_item");
var currentPage = window.location.href.split("items/")[1].charAt(0).toUpperCase() + window.location.href.split("items/")[1].slice(1);

Array.from(pageMenuItem).forEach(menuItem => {

    menuItem.classList.remove("active_item");
    if (menuItem.innerText == currentPage) menuItem.classList.add("active_item");
    if (Array.from(pageMenuItem).indexOf(menuItem) == 0 && currentPage == "") menuItem.classList.add("active_item");

})

