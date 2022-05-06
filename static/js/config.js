//make files deployable
var address = window.location.href.split("/")[window.location.href.split("/").length - 2];
(window.location.href.includes(".com")) ?
(address == "dotapicker") ?
    configDotapickerProduction()
    : (address == "heroes") ?
        configHeroesProduction()
        : {}
:(address == "dotapicker") ?
    configDotapicker()
    : (address == "heroes") ?
        configHeroesDevelopment()
        : {}
function configDotapickerProduction() {

    heroes.forEach(hero => {

        heroes[heroes.indexOf(hero)] = hero.split("/hero_avatars/")[1];

    })

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];

    })

}

function configDotapicker() {

    var heroImgs = document.getElementsByClassName("dotapicker_hero_img");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];

    })

}

function configHeroesProduction() {

    heroes.sort();

    var heroImgs = document.getElementsByClassName("hero_grid_image");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    var heroLinks = document.getElementsByClassName("hero_link");
    heroLinks = Array.from(heroLinks).splice(4);

    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroGridTitles[Array.from(heroImgs).indexOf(heroImg)].innerText = heroes[Array.from(heroImgs).indexOf(heroImg)].split(".png")[0];
        heroLinks[Array.from(heroImgs).indexOf(heroImg)].setAttribute("href", `../heroes/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`.split(".png")[0]);

    })

}

function configHeroesDevelopment() {

    var heroImgs = document.getElementsByClassName("hero_grid_image");
    var heroGridTitles = document.getElementsByClassName("hero_grid_title");
    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);

    })

}

