var profileStatsRow = document.getElementsByClassName("profile_stats_row");
var profileStatsGamemodes = document.getElementById("profile_stats_gamemodes");
var profileStatsSide = document.getElementById("profile_stats_sides");
var profileStatsRegion = document.getElementById("profile_stats_regions").getElementsByClassName("profile_stats_row");
var playerRecentMatches = document.getElementsByClassName("profile_recent_matches_row");
var profileRecentMatchResults = document.getElementsByClassName("profile_recent_match_result");
var profileHeroRows = document.getElementsByClassName("profile_hero_row");
var profileStats = document.getElementsByClassName("profile_stats");
var profileLanes = document.getElementById("profile_lanes");
var profileLanesSummary = document.getElementById("profile_lanes_summary");
var laneColors = {"Safelane":"#66B5AB", "Midlane":"#B970CA", "Jungle":"#75946B", "Offlane":"#FDA55A"};
var overviewDate = document.getElementsByClassName("overview_t_date")[0];
var profileRecentMatchTimes = document.getElementsByClassName("profile_recent_match_time");
var profileHeroRowTimes = document.getElementsByClassName("profile_hero_row_time");
var profileHeroRowWinrates = document.getElementsByClassName("profile_hero_row_winrate");
var profileHeroRowGames = document.getElementsByClassName("profile_hero_row_games");
var recentDurations = document.getElementsByClassName("profile_recent_match_duration");

console.log(profileStatsRegion);

function colorByIndex (divElement) {

    Array.from(divElement).forEach(element => {

        var nodesByParent = Array.from((element.parentNode).getElementsByClassName(element.className));

        nodesByParent.forEach(c => {

            var statsRowIndex = nodesByParent.indexOf(c);
            if (statsRowIndex % 2 == 0) c.style.backgroundColor = "#242F39";
            else c.style.backgroundColor = "#2E3740";

        })

    })

}

colorByIndex(playerRecentMatches);
colorByIndex(profileHeroRows);

Array.from(profileRecentMatchResults).forEach(element => {

    if (element.innerText[0] == "W") element.style.color = "#A9CF54";
    else element.style.color = "#C23C2A";


})

//add other tab in 'profile_stats_row' class
function addOtherRow(statsElement) {

    for (const [key, value] of Object.entries(player)) {

        //compare 'regions' stats class with 'player["regions"]' etc.
        if (statsElement.getAttribute("id").split("_")[2] == key) {
            console.log(player[key]);

            //get existing 'profile_stats_row' elements and their corresponding values
            var displayedStatsElements = statsElement.getElementsByClassName("profile_stats_row");
            console.log(displayedStatsElements);

            var dictWithNonUsedKeys = {};
            var displayedKeys = [];
            var gamesSum = 0;
            var winSum = 0;

           Array.from(displayedStatsElements).forEach(statsRow => {

               var displayedKey = Array.from(statsRow.childNodes).filter(element => element.tagName == "DIV")[0].innerText;
               displayedKeys.push(displayedKey);

           })

           console.log(displayedKeys);

           //make an object with unused keys
           for (const [playerKey, playerValue] of Object.entries(player[key])) {

               if (displayedKeys.includes(playerKey) == false) {

                   dictWithNonUsedKeys[playerKey] = player[key][playerKey];
                   gamesSum += player[key][playerKey]["games"];
                   winSum += player[key][playerKey]["win"];
               }

           }

           console.log(dictWithNonUsedKeys);
           console.log(gamesSum);
           console.log(winSum);
           var oDict = {"games":gamesSum, "win":winSum};
           console.log(statsElement);
           if (gamesSum > 0) statsElement.insertAdjacentHTML("beforeend",
           `<div class = "profile_stats_row">
               <div class = "profile_stats_row_name">
                   Other
               </div>
               <div class = "profile_stats_row_all">
                   ${gamesSum}
               </div>
               <div class = "profile_stats_row_winrate">
                   ${(((winSum / gamesSum) * 100).toFixed(2)).toString() + "%"}
               </div>
           </div>`
           );

        }

    }

}

Array.from(profileStats).forEach(element => {

    addOtherRow(element);

})

colorByIndex(profileStatsRow);

delete player["roles"]["Unknown"];
console.log(player["roles"]);

var lanesMatches = 0;

for (const [key, value] of Object.entries(player["roles"])) {

    lanesMatches += player["roles"][key]["games"]

}

for (const [key, value] of Object.entries(player["roles"])) {

    player["roles"][key]["percentage"] = ((player["roles"][key]["games"] / lanesMatches) * 100).toFixed(2);

}

console.log(player["roles"]);
//make profileLanesSummary reflect lanes percentage
var profileLanesSummaryWidth = profileLanesSummary.clientWidth;
for (const [key, value] of Object.entries(player["roles"])) {

    if (player['roles'][key]["percentage"] > 5) {

        profileLanesSummary.insertAdjacentHTML("beforeend",
        "<div class = 'profile_lanes_summary_lane'></div>"
        )

        var profileLanesSummaryLanes = document.getElementsByClassName("profile_lanes_summary_lane");
        var desiredLanesWidth = player["roles"][key]["percentage"] + "%";
        profileLanesSummaryLanes[profileLanesSummaryLanes.length - 1].style.width = desiredLanesWidth;
        profileLanesSummaryLanes[profileLanesSummaryLanes.length - 1].style.backgroundColor = laneColors[key];

        var profileLanesSummaryLaneLabels = profileLanes.getElementsByClassName("title_subtitle")[0];
        profileLanesSummaryLaneLabels.style.display = "flex";
        profileLanesSummaryLaneLabels.insertAdjacentHTML("beforeend",
        "<div class = 'profile_lanes_summary_lane_label'></div>"
        )

        var laneLabels = profileLanesSummaryLaneLabels.getElementsByClassName("profile_lanes_summary_lane_label");
        laneLabels[laneLabels.length - 1].style.width = desiredLanesWidth;
        laneLabels[laneLabels.length - 1].innerText = key;
        laneLabels[laneLabels.length - 1].style.paddingBottom = "1px";
        laneLabels[laneLabels.length - 1].style.textAlign = "center";

    }

}

overviewDate.innerText = getMatchTime(overviewDate.innerText);

for (const recentMatchTime of profileRecentMatchTimes) recentMatchTime.innerText = getMatchTime(recentMatchTime.innerText);
for (const profileHeroRowTime of profileHeroRowTimes) profileHeroRowTime.innerText = getMatchTime(profileHeroRowTime.innerText);

function getMatchTime(time) {

    timeString = time.split(": ")[1];
    console.log(timeString);
    for (const letter of timeString) {

        if (isNaN(parseInt(letter)) == false && parseInt(letter) > 0) {

            console.log(letter);
            let d = timeString.substr(timeString.indexOf(letter), timeString.length).replace(",", "");
            if (parseInt(d.split(" ")[0]) == 1) value = d.split(" ")[1].replace("s", "");
            else value = d.split(" ")[1];
            console.log(value);
            console.log(parseInt(value) == 1);
            //after finding first number find next sequence of strings
            return d.split(" ")[0] + " " + value + " ago";

        }

    }

}

visualForAdvantage(profileHeroRowGames, "red", "70px");
visualForAdvantage(profileHeroRowWinrates, "green", "70px");

//add visual indicator on elements based on their value
function visualForAdvantage(elements, chosenColor, maxWidth) {

    elementsPositive = [];
    elementsNegative = [];

    Array.from(elements).forEach(element => {

        elementValue = parseFloat(element.innerText.split("%")[0]);
        console.log(elementValue);
        if (elementValue > 0) elementsPositive.push(element);
        else elementsNegative.push(element);
        element.insertAdjacentHTML("afterend",
        `<div class = "visual_indicator">
        </div>`
        )

    })

    var visualIndicators = document.getElementsByClassName("visual_indicator");
    Array.from(visualIndicators).forEach(visualIndicator => {

        //change for visual indicators when necessary, leave for others if not necessary for them
        if (visualIndicator.previousElementSibling.className == elements[0].className) {

            //copying css
            copyStyle(visualIndicator, visualIndicator.previousElementSibling);
            console.log(visualIndicator.previousElementSibling);
            visualIndicator.style.backgroundColor = chosenColor;
            visualIndicator.style.height = "3px";
            visualIndicator.style.width = maxWidth;

        }

    })
    console.log(visualIndicators.length);

    elementsPositive.sort((a,b) => parseFloat(b.innerText.split("%")[0]) - parseFloat(a.innerText.split("%")[0]));
    var maxPositiveValue = parseFloat(elementsPositive[0].innerText.split("%")[0]);
    Array.from(elementsPositive).forEach(positiveElement => {

        var elementWidth = parseInt(positiveElement.innerText.split("%")[0] / maxPositiveValue * parseFloat(maxWidth)).toString() + "px";
        //console.log(elementWidth);
        positiveElement.nextElementSibling.style.width = elementWidth;

    })

    elementsNegative.sort((a,b) => Math.abs(parseFloat(b.innerText.split("%")[0])) - Math.abs(parseFloat(a.innerText.split("%")[0])));

    if (elementsNegative.length > 0) {

        var minNegativeValue = parseFloat(elementsNegative[0].innerText.split("%")[0]);

        Array.from(elementsNegative).forEach(negativeElement => {

            var elementWidth = parseInt(negativeElement.innerText.split("%")[0] / minNegativeValue * parseFloat(maxWidth)).toString() + "px";
            //console.log(elementWidth);
            negativeElement.nextElementSibling.style.width = elementWidth;

        })

    }

}

function copyStyle(elementToCopyTo, elementToCopyFrom) {

    const elementToCopyFromStyles = window.getComputedStyle(elementToCopyFrom);
    let cssText = elementToCopyFromStyles.cssText;

    if (!cssText) {

          cssText = Array.from(elementToCopyFromStyles).reduce((str, property) => {
                return `${str}${property}:${elementToCopyFromStyles.getPropertyValue(property)};`;
          }, '');

    }

    elementToCopyTo.style.cssText = cssText;

}

Array.from(recentDurations).forEach(element => {

    if (element.innerText.includes(":") == false) element.innerText = element.innerText.slice(0, 2) + ":" + element.innerText.slice(2,4);

})

