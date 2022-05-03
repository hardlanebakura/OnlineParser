var matchDuration = document.getElementsByClassName("match_duration")[0];
var duration = parseInt(match["duration"]);
var durationInMinutes = parseInt(duration / 60);
var durationInSeconds = duration % 60;
var heroNetworth = document.getElementsByClassName("hero_nw_stats");
var heroLastHits = document.getElementsByClassName("hero_lh_stats");
var heroDamage = document.getElementsByClassName("hero_damage_stats");
var heroHealing = document.getElementsByClassName("hero_healing_stats");
var heroBuilding = document.getElementsByClassName("hero_building_stats");
var radiantPicks = [];
var radiantBans = [];
var direPicks = [];
var direBans = [];
var heroImages = document.getElementsByClassName("team_heroes_hero_image");
var picksAndBansPick = document.getElementsByClassName("picks_and_bans_pick");
var picksAndBansBan = document.getElementsByClassName("picks_and_bans_ban");
var pickBanOrder = document.getElementsByClassName("pick_ban_order");
var teamHeroesHeroAbilities = document.getElementsByClassName("team_heroes_hero_ability");
var matchTime = document.getElementsByClassName("match_time")[0];
var matchWinner = document.getElementsByClassName("match_winner")[0];

let remainder = "";
if (durationInSeconds < 10) remainder = "0";

matchDuration.innerText = durationInMinutes.toString() + ":" + remainder + durationInSeconds.toString();

function statsDisplay(stats) {

    stats = parseFloat(stats/1000).toFixed(1).toString() + "K";
    if (stats == "0.0K") stats = "-";
    return stats;

}

for (let i = 0; i < heroLastHits.length; i++) {

    heroNetworth[i].innerText = statsDisplay(heroNetworth[i].innerText);
    heroDamage[i].innerText = statsDisplay(heroDamage[i].innerText);
    heroHealing[i].innerText = statsDisplay(heroHealing[i].innerText);
    heroBuilding[i].innerText = statsDisplay(heroBuilding[i].innerText);


}

for (let i = 0; i < match["picks_bans"].length; i++) {

    match["picks_bans"][i]["order"] += 1;

    //hero was banned
    if (match["picks_bans"][i]["team"] == 0 && match["picks_bans"][i]["is_pick"] == false) radiantBans.push(match["picks_bans"][i]);

    else if (match["picks_bans"][i]["is_pick"] == false) direBans.push(match["picks_bans"][i]);

}

//console.log(match["picks_bans"]);
console.log(radiantBans);
console.log(direBans);

//if one side has more bans than the other, switch the last one to the other side
if (radiantBans.length > direBans.length) direBans.push(radiantBans.pop());

else if (radiantBans.length < direBans.length) radiantBans.push(direBans.pop());

console.log(direBans);

Array.from(heroImages).forEach(element => {

    var heroAvatar = element.getAttribute("src").split("/hero_avatars/")[1].split(".png")[0];
    if (Array.from(heroImages).indexOf(element) < 5) radiantPicks.push(heroAvatar);
    else direPicks.push(heroAvatar);

})

for (let i = 0; i < picksAndBansPick.length; i++) {

    if (i < 5) picksAndBansPick[i].setAttribute("src", `/static/images/hero_avatars/${radiantPicks[i]}.png`);
    else picksAndBansPick[i].setAttribute("src", `/static/images/hero_avatars/${direPicks[i - 5]}.png`);

}

for (let i = 0; i < picksAndBansBan.length; i++) {

    if (i < picksAndBansBan.length/2) {
        if (radiantBans[i] != undefined) {
            //console.log(i); console.log(radiantBans[i]);
            picksAndBansBan[i].setAttribute("src", `/static/images/hero_avatars/${radiantBans[i]["hero"]}.png`);
        }
        else {
            picksAndBansBan[i].parentNode.style.display = "none";
        }
    }
    else {
        //console.log(direBans[i - 4]);
        //console.log(direBans[i - 4] == undefined);
        if (direBans[i - 4] != undefined) picksAndBansBan[i].setAttribute("src", `/static/images/hero_avatars/${direBans[i - 4]["hero"]}.png`);
        else picksAndBansBan[i].parentNode.style.display = "none";
    }
}

Array.from(pickBanOrder).forEach(element => {

    if (element.previousElementSibling.getAttribute("src") != null) {

            var heroName = element.previousElementSibling.getAttribute("src").split("/hero_avatars/")[1].split(".png")[0].replaceAll("%20", " ");
            match["picks_bans"].forEach(hero => {

                if (hero["hero"] == heroName) element.innerText = hero["order"];

            })

    }


})

console.log(radiantPicks);
console.log(direPicks);

Array.from(teamHeroesHeroAbilities).forEach(element => {

    if (element.innerText == "766") {
    console.log(element);
    console.log(Object.keys(talentTreeCodes).includes(element.innerText));
    console.log(Object.keys(abilities).includes(element.innerText));
    }

    if ((Object.keys(talentTreeCodes).includes(element.innerText) == false) && (Object.keys(abilities).includes(element.innerText) == false) && (element.innerText != "")) {

        console.log(element.innerText);
        element.innerText = "";
        console.log(Object.keys(abilities).includes("1"));
        console.log(Object.keys(abilities).includes(element.innerText));
        element.insertAdjacentHTML("beforeend",
                `<img class = "team_heroes_hero_ability_image" src = "../static/images/talent_tree.png">
                <div class = "team_heroes_talent_tree_detailed_info">1</div>`
                )

    }

    for (const [k, v] of Object.entries(abilities)) {

        //console.log(element.innerText);
        if (element.innerText == k) {

            if (abilities[k].substr(0, 7) != "special") {

                element.innerText = "";

                element.insertAdjacentHTML("beforeend",
                `<img class = "team_heroes_hero_ability_image" src = "http://cdn.dota2.com/apps/dota2/images/abilities/${abilities[k]}_lg.png">`
                )

            }

            //talent level
            else {

                console.log(Object.keys(abilities).includes(element.innerText));
                element.innerText = "";
                element.insertAdjacentHTML("beforeend",
                `<img class = "team_heroes_hero_ability_image" src = "../static/images/talent_tree.png">
                <div class = "team_heroes_talent_tree_detailed_info">1</div>`
                )

                console.log(abilities[k])
                console.log(k)

                element.getElementsByClassName("team_heroes_hero_ability_image")[0].addEventListener("mouseover", event => {

                    element.getElementsByClassName("team_heroes_talent_tree_detailed_info")[0].style.display = "block";
                    element.parentNode.style.height = "26px";

                })

                element.getElementsByClassName("team_heroes_hero_ability_image")[0].addEventListener("mouseout", event => {

                    element.getElementsByClassName("team_heroes_talent_tree_detailed_info")[0].style.display = "none";

                })

                console.log(element.getElementsByClassName("team_heroes_hero_ability_image")[0]);

                let selectedTalent = talentTreeCodes[k];
                console.log(typeof(k));
                console.log(k);
                console.log(selectedTalent);
//                element.innerText = element.innerText + selectedTalent;
//                if (selectedTalent != undefined) element.innerText = selectedTalent;
//                else element.innerText = abilities[k];

            }

        }

        else {



        }

    }

})

console.log(abilities);

matchTime.innerText = getMatchTime(matchTime.innerText);

function getMatchTime(time) {

    timeString = time.split(": ")[1];
    for (const letter of timeString) {

        if (isNaN(parseInt(letter)) == false && parseInt(letter) > 0) {

            d = timeString.substr(timeString.indexOf(letter), timeString.length).replace(",", "");
            //after finding first number find next sequence of strings
            return d.split(" ")[0] + " " + d.split(" ")[1] + " ago";

        }

    }

}

matchWinner.style.color = matchWinner.innerText.split(" ")[0] == "RADIANT" ? "#A9CF54" : "#C23C2A";


