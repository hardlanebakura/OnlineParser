//make files deployable
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(window.location.href.includes(".com")) ?
(address == "dotapicker") ?
    configDotapicker()
    : (address == "heroes") ?
        configHeroesProduction()
        : {}
:(address == "dotapicker") ?
    config()
    : {}
//(address == "dotapicker") ?
//    configDotapicker()
//    : {}
//:(address == "dotapicker") ?
//    config()
//    : {}
//(window.location.href.includes(".com")) ? (address == "dotapicker") ? configDotapicker() : {} : (address == "dotapicker") ? config() : {}
function configDotapicker() {

    heroes.forEach(hero => {

        heroes[heroes.indexOf(hero)] = hero.split("/hero_avatars/")[1];

    })

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        console.log(`../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];

    })

}

function config() {

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        console.log(`../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];

    })

}

function configHeroesProduction() {

    heroes.sort();

    heroes.forEach(hero => {

        heroes[heroes.indexOf(hero)] = hero.split("/hero_avatars/")[1];

    })

    var heroImgs = document.getElementsByClassName("hero_grid_image");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        console.log(heroes);
        console.log(heroes[Array.from(heroImgs).indexOf(heroImg)]);
        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        console.log(`../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];

    })

}

function configHeroesDevelopment() {



}

