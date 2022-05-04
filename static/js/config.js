//make files deployable
//if (window.location.href)
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(address == "dotapicker") ? configDotapicker() : config();

function configDotapicker() {

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../images/hero_avatars/${}`);

    })

}

function config() {

    console.log("asd");

}

