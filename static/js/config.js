//make files deployable
//if (window.location.href)
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(window.location.href.includes(".com")) ? (address == "dotapicker") ? configDotapicker() : config() : {}

function configDotapicker() {

    heroes.forEach(hero => {

        heroes[heroes.indexOf(hero)] = hero.split("/hero_avatars/")[1];

    })
    console.log(heroes);
    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    Array.from(heroImgs).forEach(heroImg => {

        console.log("1");
        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        console.log(`../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);

    })

    heroImgs[0].setAttribute("src", "../static/images/hero_avatars/Abaddon.png");
    console.log("1");

}

function config() {

    console.log("asd");

}

