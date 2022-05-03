var dotapickerHeroImg = document.getElementsByClassName("dotapicker_hero_img");
var dotapickerHeroOptions = document.getElementsByClassName("dotapicker_hero_options");
var heroOptionOne = document.getElementsByClassName("dotapicker_hero_option_1")[0];
var addEnemyButton = document.getElementsByClassName("option_add_enemy");
var addAllyButton = document.getElementsByClassName("option_add_team");
var addBanButton = document.getElementsByClassName("option_ban");
var banButton = document.getElementsByClassName("option_ban");
var dotapickerTeamsDisplay = document.getElementsByClassName("dotapicker_teams_display")[0];
var dotapickerTeamTitle = document.getElementsByClassName("dotapicker_team_title");
var dotapickerTeamEnemy = document.getElementsByClassName("dotapicker_team_enemy")[0];
var dotapickerTeamAlly = document.getElementsByClassName("dotapicker_team_ally")[0];
var enemyImage = document.getElementsByClassName("dotapicker_team_enemy_image");
var allyImage = document.getElementsByClassName("dotapicker_team_ally_image");
var dotapickerHeroGrid = document.getElementsByClassName("dotapicker_hero_grid")[0];
var dotapickerHeroGridMenu = document.getElementsByClassName("dotapicker_hero_grid_menu")[0];
var dotapickerHeroGridPicks = document.getElementsByClassName("dotapicker_hero_grid_picks")[0];
var dotapickerPicksCore = document.getElementsByClassName("dotapicker_hero_grid_picks_core")[0];
var dotapickerPicksUtility = document.getElementsByClassName("dotapicker_hero_grid_picks_utility")[0];
var enemyHeroes = [];
var allyHeroes = [];
var bannedHeroes = [];
var pickImg = document.getElementsByClassName("pick_img");
var dotapickerCounterpick = document.getElementsByClassName("dotapicker_counterpick");
var counterpickBan = document.getElementsByClassName("counterpick_ban");
var searchInput = document.getElementsByClassName("search_input")[0];
var showHeroGridButton = document.getElementsByClassName("show_hero_grid_button")[0];

var attributes = {
    "str":"Strength",
    "agi":"Agility",
    "int":"Intelligence"
}

//toggling the display of menu to add the hero to enemy, ban or team on hover
for (let i = 0; i < dotapickerHeroImg.length; i++) {

        dotapickerHeroImg[i].addEventListener("mouseover", event => {

        dotapickerHeroImg[i].parentNode.childNodes[3].style.display = "none";
        dotapickerHeroOptions[i].style.display = "flex";
        dotapickerHeroOptions[i].style.transform = "translate(0px, -58px)";
        dotapickerHeroImg[i].parentNode.style.height = "80px";

    })

        dotapickerHeroImg[i].addEventListener("mouseout", event => {

        dotapickerHeroImg[i].parentNode.childNodes[3].style.display = "block";
        dotapickerHeroOptions[i].style.display = "none";

    })

}

//adding event listeners for 'add enemy' button
for (let i = 0; i < addEnemyButton.length; i++) {

    addEnemyButton[i].addEventListener("click", event => {

        dotapickerTeamsDisplay.style.display = "flex";
        dotapickerTeamsDisplay.style.justifyContent = "center";
        dotapickerTeamEnemy.style.display = "block";
        dotapickerHeroGridMenu.style.display = "block";
        dotapickerHeroGridPicks.style.display = "flex";
        console.log(enemyImage.length);
        let heroName = addEnemyButton[i].parentNode.parentNode.parentNode.childNodes[3].innerText;

        for (let j = 0; j < enemyImage.length; j++) {

            console.log(j);
            if (enemyImage[j].getAttribute("src") == "/static/images/black.png") {

                //remove old counterpicks and replace with new ones
                Array.from(dotapickerCounterpick).forEach(counterpick => counterpick.parentNode.removeChild(counterpick));

                console.log(heroName);
                enemyHeroes.push(heroName);
                console.log(enemyHeroes);
                counterpicksForGivenHeroes = getCounterpicks(enemyHeroes);
                counterpicksForGivenHeroesCore = [];
                counterpicksForGivenHeroesUtility = [];

                counterpicksForGivenHeroes.forEach(hero => {

                    if (hero["roles"].includes("Carry")) counterpicksForGivenHeroesCore.push(hero);
                    else counterpicksForGivenHeroesUtility.push(hero);

                })

                counterpicksForGivenHeroesCore.forEach(hero => {

                    let imgLocation = `<img class = 'pick_img' src = "/static/images/hero_avatars/${hero['name']}.png">`;
                    dotapickerPicksCore.insertAdjacentHTML("beforeend", `<div class = "dotapicker_counterpick">${imgLocation}
                    <div class = "counterpick_name_and_advantage">
                        <div class = "counterpick_name">${hero["name"]}</div>
                        <div class = "counterpick_advantage">${hero["advantage"]}</div>
                    </div>
                    <button class = "counterpick_ban">ban</button>
                    </div>
                    <div class = "counterpick_details">1</div>
                    `);

                })

                counterpicksForGivenHeroesUtility.forEach(hero => {

                    let imgLocation = `<img class = 'pick_img' src = "/static/images/hero_avatars/${hero['name']}.png">`;
                    dotapickerPicksUtility.insertAdjacentHTML("beforeend", `<div class = "dotapicker_counterpick">${imgLocation}
                    <div class = "counterpick_name_and_advantage">
                        <div class = "counterpick_name">${hero["name"]}</div>
                        <div class = "counterpick_advantage">${hero["advantage"]}</div>
                    </div>
                    <button class = "counterpick_ban">ban</button>
                    </div>
                    <div class = "counterpick_details">1</div>
                    `);

                })

                console.log(counterpicksForGivenHeroesCore);
                enemyImage[j].setAttribute("src", `/static/images/hero_avatars/${heroName}.png`);
                addEnemyButton[i].parentNode.parentNode.parentNode.style.display = "none";

                break;

            }

        }

        //styling counterpicks based on their advantage
        console.log(dotapickerCounterpick.length);
        for (let m = 0; m < dotapickerCounterpick.length; m++) {
        let heroAdvantage = dotapickerCounterpick[m].childNodes[2].childNodes[3].innerText;
        if (parseFloat(heroAdvantage) > 1.5) dotapickerCounterpick[m].style.backgroundColor = "rgba(0,255,0,0.112)";
        if (parseFloat(heroAdvantage) < -1.5) dotapickerCounterpick[m].style.backgroundColor = "rgba(255,0,0,0.112)";

        }

        console.log(counterpickBan.length);
        for (let m = 0; m < counterpickBan.length; m++) {

            counterpickBan[m].addEventListener("click", event => {

                dotapickerCounterpick[m].style.display = "none";

            })

        }



    })

}

//adding event listeners for 'add ally' button
for (let i = 0; i < addAllyButton.length; i++) {

    addAllyButton[i].addEventListener("click", event => {

        dotapickerTeamsDisplay.style.display = "flex";
        dotapickerTeamsDisplay.style.justifyContent = "center";
        dotapickerTeamAlly.style.display = "block";
        dotapickerHeroGridMenu.style.display = "block";
        dotapickerHeroGridPicks.style.display = "flex";
        console.log(allyImage.length);
        for (let j = 0; j < enemyImage.length; j++) {

            console.log(j);
            if (allyImage[j].getAttribute("src") == "/static/images/black.png") {

                let heroName = addAllyButton[i].parentNode.parentNode.parentNode.childNodes[3].innerText;
                console.log(heroName);
                allyImage[j].setAttribute("src", `/static/images/hero_avatars/${heroName}.png`);
                addAllyButton[i].parentNode.parentNode.parentNode.style.display = "none";
                break;

            }

        }
        
    })

}

//adding event lsiteners for 'add ban' button
for (let i = 0; i < addBanButton.length; i++) {

    addBanButton[i].addEventListener("click", event => {

        addBanButton[i].parentNode.parentNode.parentNode.style.display = "none";

    })

}

dotapickerTeamTitle[0].style.color = "red";
dotapickerTeamTitle[1].style.color = "green";

//function to get counterpicks for enemy heroes
function getCounterpicks(enemyHeroes) {

    console.log(enemyHeroes);
    console.log(counterpicks[0]);
    var counterpicksForGivenHeroes = [];

    for (let i = 0; i < counterpicks.length; i++) {

        if (enemyHeroes.includes(counterpicks[i]["counterpick_for"])) counterpicksForGivenHeroes.push(counterpicks[i]);

    }

    var allCounterpicksForGivenHeroes = {};
    var heroNames = [];
    Array.from(heroes).forEach(hero => {

        let heroName = hero.split(".")[0]
        heroNames.push(heroName);
        allCounterpicksForGivenHeroes[heroName] = 0;

    })

    for (let i = 0; i < counterpicksForGivenHeroes.length; i++) allCounterpicksForGivenHeroes[counterpicksForGivenHeroes[i]["hero"]] += parseFloat(counterpicksForGivenHeroes[i]["advantage"].split("%")[0]);


    for (let key in allCounterpicksForGivenHeroes) allCounterpicksForGivenHeroes[key] = allCounterpicksForGivenHeroes[key].toFixed(2);
    console.log(allCounterpicksForGivenHeroes);

    // Create items array
    var sortedCounterpicks = Object.keys(allCounterpicksForGivenHeroes).map(function(key) {
        return [key, allCounterpicksForGivenHeroes[key]];
    });

    // Sort the array based on the second element
    sortedCounterpicks.sort(function(first, second) {
      return second[1] - first[1];
    });

    var sortedCounterpicksList = [];

    for (const [key, value] of Object.entries(sortedCounterpicks)) {

        let heroName = sortedCounterpicks[key][0];
        let hero = {"name":heroName, "advantage":sortedCounterpicks[key][1]};
        for (let i = 0; i < responseHeroes.length; i++) {

            if (hero["name"] == responseHeroes[i]["localized_name"]) {

                hero["roles"] = responseHeroes[i]["roles"];
                break;

            }

        }
        sortedCounterpicksList.push(hero);

    }

    console.log(sortedCounterpicksList);
    return sortedCounterpicksList

}

getCounterpicks(["Marci", "Lich"]);

function dotapicker_search() {

    console.log("1");

}

showHeroGridButton.addEventListener("click", event => {

    var attributesHeroGrid = document.getElementsByClassName("attributes_hero_grid")[0];

    if (showHeroGridButton.innerText == "Show Hero Grid" && attributesHeroGrid == undefined) {

        showHeroGridButton.insertAdjacentHTML("afterend",
        `<div class = "attributes_hero_grid">
        <div>`);

        showHeroGridButton.innerText = "Hide Hero Grid";
        dotapickerHeroGrid.style.display = "none";
        let attributesHeroGrid = document.getElementsByClassName("attributes_hero_grid")[0];
        getAttributesHeroGridElements(attributesHeroGrid);

    }

    else {

        attributesHeroGrid.remove();
        showHeroGridButton.innerText = "Show Hero Grid";
        dotapickerHeroGrid.style.display = "block";

    }

})

console.log(heroes);
console.log(responseHeroes);

function getAttributesHeroGridElements(heroGrid) {

    var strHeroes = [];
    var agiHeroes = [];
    var intHeroes = [];

    responseHeroes.forEach(hero => {

        if (hero["primary_attr"] == "str") strHeroes.push(hero["localized_name"]);
        else if (hero["primary_attr"] == "agi") agiHeroes.push(hero["localized_name"]);
        else intHeroes.push(hero["localized_name"]);

    })

    var allHeroAttributes = {

        "str":strHeroes,
        "agi":agiHeroes,
        "int":intHeroes

    }

    getHeroGridForAttribute(allHeroAttributes, heroGrid, "str");
    getHeroGridForAttribute(allHeroAttributes, heroGrid, "agi");
    getHeroGridForAttribute(allHeroAttributes, heroGrid, "int");

}

function getHeroGridForAttribute(allHeroAttributes, heroGrid, attribute) {

    heroGrid.insertAdjacentHTML("beforeend",
    `<div class = "attributes_title">${attributes[attribute]} Heroes
    </div>`
    );

    var imageNumbersInAttribute = allHeroAttributes[attribute].length;

    const rowNumbers = parseInt(allHeroAttributes[attribute].length / 8);
    for (let rowNumber = 0; rowNumber <= rowNumbers; rowNumber++) {

        heroGrid.insertAdjacentHTML("beforeend",
        `<div class = "attributes_hero_grid_row">
        </div>`);

        var attributesHeroGridRow = document.getElementsByClassName("attributes_hero_grid_row");
        switch((rowNumber + 1) * 8 > imageNumbersInAttribute) {

            //row will have 8 images
            case false: {

                for (let imgIndex = 0; imgIndex < 8; imgIndex++) {

                    attributesHeroGridRow[attributesHeroGridRow.length - 1].insertAdjacentHTML("beforeend",
                    `<img class = "attributes_hero_grid_image" src = "/static/images/hero_avatars/${allHeroAttributes[attribute][(rowNumber * 8) + imgIndex]}.png">`
                    );

                }

                break;

            }

            //row will have imageNumbersInAttribute - (rowNumber * 8) images
            case true: {

                for (let imgIndex = 0; imgIndex < imageNumbersInAttribute - (rowNumber * 8); imgIndex++) {

                    attributesHeroGridRow[attributesHeroGridRow.length - 1].insertAdjacentHTML("beforeend",
                    `<img class = "attributes_hero_grid_image" src = "/static/images/hero_avatars/${allHeroAttributes[attribute][(rowNumber * 8) + imgIndex]}.png">`
                    );

                }

            }

        }


    }

}


