var heroesGridHero = document.getElementsByClassName("heroes_grid_hero");
var heroWinrates = Object.assign([], hero_popularities);
heroWinrates.sort(function(a, b) {

    return parseFloat(b["hero_winrate"].split("%")[0]) - parseFloat(a["hero_winrate"].split("%")[0]);

})

var mostPopularHeroes = hero_popularities.slice(0, 10).map(c => c["hero_name"]);
var highestWinrates = heroWinrates.slice(0, 10).map(c => c["hero_name"]);
var heroImgs = document.getElementsByClassName("hero_grid_image");
var heroGridTitles = document.getElementsByClassName("hero_grid_title");
var heroLinks = document.getElementsByClassName("hero_link");
heroLinks = Array.from(heroLinks).splice(4);
console.log(heroLinks.length);

if (window.location.href.includes(".com") == false) {


    Array.from(heroImgs).forEach(heroImg => {

        heroImg.setAttribute("src", `../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        console.log(`../static/images/hero_avatars/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`);
        heroLinks[Array.from(heroImgs).indexOf(heroImg)].setAttribute("href", `../heroes/${heroes[Array.from(heroImgs).indexOf(heroImg)]}`.split(".png")[0]);

    })

}

Array.from(heroesGridHero).forEach(element => {

    //hero image
    if (heroImgs[0] != undefined) {

        if (element.getElementsByClassName("hero_grid_image")[0] != undefined) {

        console.log(heroes);
        console.log(element);
        console.log(element.getElementsByClassName("hero_grid_image")[0]);
        var heroName = (window.location.href.includes(".com")) ? heroes[Array.from(heroesGridHero).indexOf(element)]
        : element.getElementsByClassName("hero_grid_image")[0].getAttribute("src").split("/hero_avatars/")[1].split(".png")[0].replace("%20", " ");

        console.log(heroName);

        //var heroName = element.getElementsByClassName("hero_grid_image")[0].getAttribute("src").split("/hero_avatars/")[1].split(".png")[0].replace("%20", " ");
        hero_popularities.forEach(hero => {

            if (hero["hero_name"] == heroName) {

                //hero is in most popular
                if (mostPopularHeroes.includes(heroName)) {

                    console.log(heroName);
                    element.insertAdjacentHTML("beforeend",
                    `<img class = "most_popular_hero" src = "../static/images/high_popularity_icon.png">`
                    )

                }

                //hero is in highest winrate
                if (highestWinrates.includes(heroName)) {

                    console.log(heroName);
                    element.insertAdjacentHTML("beforeend",
                    `<img class = "highest_winrate_hero" src = "../static/images/high_winrate_icon.png">`
                    )


                    //hero is also extremely popular
                    if (element.getElementsByClassName("most_popular_hero")[0] != undefined) {

                        element.getElementsByClassName("most_popular_hero")[0].style.transform = "translate(109px, -102px)";
                        element.getElementsByClassName("highest_winrate_hero")[0].style.transform = "translate(109px, -102px)";

                    }

                }

                element.parentNode.style.height = "100px";

            }

        })

    }

    }

})

console.log(mostPopularHeroes);
console.log(highestWinrates);
console.log(hero_popularities);


