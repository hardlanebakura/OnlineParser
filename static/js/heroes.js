var heroesGridHero = document.getElementsByClassName("heroes_grid_hero");
var heroWinrates = Object.assign([], hero_popularities);
heroWinrates.sort(function(a, b) {

    return parseFloat(b["hero_winrate"].split("%")[0]) - parseFloat(a["hero_winrate"].split("%")[0]);

})

var mostPopularHeroes = hero_popularities.slice(0, 10).map(c => c["hero_name"]);
var highestWinrates = heroWinrates.slice(0, 10).map(c => c["hero_name"]);

//heroes.forEach(hero => {
//
//    if (hero.length > 22) hero = hero.split("/hero_avatars/")[1];
//
//})

Array.from(heroesGridHero).forEach(element => {

    //hero image
    if (element.getElementsByClassName("hero_grid_image")[0] != undefined) {

        var heroName = element.getElementsByClassName("hero_grid_image")[0].getAttribute("src").split("/hero_avatars/")[1].split(".png")[0].replace("%20", " ");
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

})

console.log(mostPopularHeroes);
console.log(highestWinrates);
console.log(hero_popularities);

