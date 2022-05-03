var heroRoles = document.getElementsByClassName("hero_roles")[0];
console.log(heroRoles);
console.log(typeof(heroRoles) == 'undefined');
var heroWinrate = document.getElementsByClassName("hero_winrate_title")[0];
var highColor = "#A9CF54";
var lowColor = "#C23C2A";
var heroPopularityRankTitle = document.getElementsByClassName("hero_popularity_rank_title")[0];
var matchupsRow = document.getElementsByClassName("matchups_row");
var matchupsRowsHeroWinPercentages = document.getElementsByClassName("matchups_row_hero_win_percentage");
var matchupsRowsHeroAdvantages = document.getElementsByClassName("matchups_row_hero_advantage");
var heroStatsRow = document.getElementsByClassName("hero_stats_row");
var heroAttributeImage = document.getElementsByClassName("hero_attributes_img");
var heroAttributeAttributeGains = document.getElementsByClassName("hero_attributes_attribute_gains");
var statsTalentRow = document.getElementsByClassName("stats_talent_row");
var overviewMatchupRows = document.getElementsByClassName("overview_matchups_row");
var heroLanesRow = document.getElementsByClassName("hero_lanes_row");
var matchupsRowsHeroAdvantagesBig = document.getElementsByClassName("matchups_row_hero_advantage_big");
var matchupsRowsHeroWinPercentagesBig = document.getElementsByClassName("matchups_row_hero_win_percentage_big");
var heroRowPresences = document.getElementsByClassName("hero_lanes_row_presence");
var heroRowWinrates = document.getElementsByClassName("hero_lanes_row_winrate");
var heroRowKdaRatios = document.getElementsByClassName("hero_lanes_row_kda");
var heroRowGPM = document.getElementsByClassName("hero_lanes_row_gpm");
var heroRowXpm = document.getElementsByClassName("hero_lanes_row_xpm");

var roles = hero["roles"];
roles.unshift(hero["attack_type"]);
roles = roles.join(", ");
if (!(typeof(heroRoles) == 'undefined')) heroRoles.innerText = roles;

console.log(parseFloat(heroWinrate.innerText.split("%")[0]));
console.log(parseFloat(heroWinrate.innerText.split("%")[0]) > 50);
if (parseFloat(heroWinrate.innerText.split("%")[0]) > 50) heroWinrate.style.color = highColor;
else heroWinrate.style.color = lowColor;

if (parseInt(heroPopularityRankTitle.innerText) == 1) heroPopularityRankTitle.innerText += "st";
else if (parseInt(heroPopularityRankTitle.innerText) == 1) heroPopularityRankTitle.innerText += "nd";
else if (parseInt(heroPopularityRankTitle.innerText) == 1) heroPopularityRankTitle.innerText += "rd";
else heroPopularityRankTitle.innerText += "th";

//we are in main page now
if (window.location.href.split("/heroes/")[1].includes("/") == false) {

    //- becomes + for hero advantages
    Array.from(matchupsRowsHeroAdvantages).forEach(element => {

        if (element.innerText[0] == "-") {
            element.innerText = "" + element.innerText.substring(1, element.innerText.length);
            element.style.paddingLeft = "7px";
            console.log(element.parentNode.nextElementSibling.childNodes[1]);
            element.parentNode.nextElementSibling.childNodes[1].style.marginLeft = "3px";
        }
        else element.innerText = "-" + element.innerText;

    })

    Array.from(matchupsRowsHeroWinPercentages).forEach(element => {

        element.innerText = (100 - element.innerText).toString() + "%";

    })

    heroAttributeImage[1].style.marginLeft = "17px";
    heroAttributeImage[2].style.marginLeft = "19px";
    heroAttributeAttributeGains[1].style.marginLeft = "17px";

    Array.from(statsTalentRow).forEach(talentRow => {

       console.log(talentRow.innerText);
       for (const [k, v] of Object.entries(talentsForHero)) {

           if (v["name"] == talentRow.innerText) {

               //advantageous talent
               if (v["advantage"] != "") {

                   talentRow.style.backgroundColor = "rgba(0, 255, 0, 0.114)";
                   console.log(talentRow.parentNode);
                   talentRow.insertAdjacentHTML("afterend",
                   `<div class = "talent_row_advantage">${v["advantage"]}
                   </div>`
                   )

               }

               else {

                   talentRow.style.backgroundColor = "red";

               }

           }

       }

    })

    heroLanesRowIndicatorClasses = [];
    Array.from(heroLanesRow[1].childNodes).forEach(childElement => {

        if (!isNaN(parseFloat(childElement.innerText))) {

            console.log(childElement.childNodes[1]);
            heroLanesRowIndicatorClasses.push(childElement.childNodes[1].className);

        }

    })

    visualForAdvantage(heroRowPresences, "red", "70px");
    visualForAdvantage(heroRowWinrates, "green", "70px");
    visualForAdvantage(heroRowKdaRatios, "orange", "70px");
    visualForAdvantage(heroRowGPM, "gold", "70px");
    visualForAdvantage(heroRowXpm, "lightblue", "70px");
    colorByIndex(heroLanesRow);

}

colorByIndex(matchupsRow);
colorByIndex(heroStatsRow);
colorByIndex(overviewMatchupRows);

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

Array.from(heroAttributeImage).forEach(element => element.style.marginLeft = "10px");

visualForAdvantage(matchupsRowsHeroAdvantages, "red", "70px");
visualForAdvantage(matchupsRowsHeroWinPercentages, "green", "70px");
visualForAdvantage(matchupsRowsHeroAdvantagesBig, "red", "70px");
visualForAdvantage(matchupsRowsHeroWinPercentagesBig, "green", "70px");

//adding the visual indicator for hero lane rows

console.log(heroLanesRowIndicatorClasses);
for (let i = 0; i < heroLanesRowIndicatorClasses.length; i++) {

    visualForAdvantage(document.getElementsByClassName(heroLanesRowIndicatorClasses[i]), "red", "70px");

}

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

