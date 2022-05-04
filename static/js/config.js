//make files deployable
//if (window.location.href)
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(address == "dotapicker") ? configDotapicker() : config();

function configDotapicker() {

    var heroImg = document.getElementsByClassName("dotapicker_hero_img");
    console.log(heroes);

}

function config() {

    console.log("asd");

}

