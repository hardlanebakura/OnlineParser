//make files deployable
//if (window.location.href)
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(window.location.href.includes(".com")) ? (address == "dotapicker") ? configDotapicker() : config() : {}

function configDotapicker() {

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    Array.from(heroImgs).forEach(heroImg => {

        console.log("1");
        heroImg.setAttribute("src", `${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);

    })

}

function config() {

    console.log("asd");

}

