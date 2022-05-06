var address = window.location.href.split("/")[window.location.href.split("/").length - 1];
(address == "winrate") ? getWinrates(): (address == "impact") ? getImpact() : (address == "meta") ? getMeta() : {}
var heroesRows = document.getElementsByClassName("heroes_row");

colorByIndex(heroesRows);

function getWinrates() {

    var heroWinrates = document.getElementsByClassName("heroes_hero_winrate");
    var heroPopularities = document.getElementsByClassName("heroes_hero_popularity");
    var heroKDAs = document.getElementsByClassName("heroes_hero_kda");

    visualForAdvantage(heroWinrates, "green", "70px");
    visualForAdvantage(heroPopularities, "red", "70px");
    visualForAdvantage(heroKDAs, "orange", "70px");

}

function getImpact() {

    var heroKills = document.getElementsByClassName("heroes_hero_kills");
    var heroDeaths = document.getElementsByClassName("heroes_hero_deaths");
    var heroAssists = document.getElementsByClassName("heroes_hero_assists");
    var heroKDAs = document.getElementsByClassName("heroes_hero_kda");

    visualForAdvantage(heroKDAs, "orange", "70px");
    visualForAdvantage(heroKills, "red", "70px");
    visualForAdvantage(heroDeaths, "gray", "70px");
    visualForAdvantage(heroAssists, "green", "70px");
}

function getMeta() {

    //style
    var toMoveByPixels = {1:9, 2:7, 3:7, 4:7, 5:11, 6:7, 7:-8, 8:12, 9:6}
    var heroesMetaUsagesDetails = document.getElementsByClassName("heroes_hero_meta_usage_percentage_details")
    var heroesMetaWinPercentagesDetails = document.getElementsByClassName("heroes_hero_meta_win_percentage_details");
    var arr = [];
    for (let i = 0; i < heroesMetaUsagesDetails.length; i++) { arr.push(heroesMetaUsagesDetails[i]); arr.push(heroesMetaWinPercentagesDetails[i]); }
    for (const [k, v] of Object.entries(toMoveByPixels)) arr[k].style.marginLeft = v.toString() + "px";
    for (let i = arr.length -3; i < arr.length; i++) { arr[i].style.width = "83px"; arr[i].style.textAlign = "center"; }

    var heroesMetaUsagePercentages = document.getElementsByClassName("heroes_hero_meta_usage_percentage");
    var heroesMetaWinPercentages = document.getElementsByClassName("heroes_hero_meta_win_percentage");

    visualForAdvantage(heroesMetaUsagePercentages, "red", "70px");
    visualForAdvantage(heroesMetaWinPercentages, "white", "70px");

}

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


