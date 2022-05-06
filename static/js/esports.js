var teamRegionalRank = document.getElementsByClassName("team_regional_rank")[0];
var teamRankingRow = document.getElementsByClassName("team_ranking_row");
var teamName = document.getElementsByClassName("team_overview_name_prize_name")[0];
var teamPrizeWinnings = document.getElementsByClassName("team_overview_name_prize_prize")[0];
var teamOverviewRankPoints = document.getElementsByClassName("team_overview_rank_points")[0];
var teamOverviewStatisticsValues = document.getElementsByClassName("team_overview_statistics_value");
var teamOverViewRegionName = document.getElementsByClassName("team_overview_region_name")[0];
var teamOverviewLogo = document.getElementsByClassName("team_overview_logo_img")[0];
var teamRecentMatches = document.getElementsByClassName("team_overview_recent_matches")[0];
var teamRosterPlayers = document.getElementsByClassName("team_players")[0];
var teamPlayer = document.getElementsByClassName("team_players_player");
var teamPlayerImg = document.getElementsByClassName("team_players_player_img");
var teamPlayerName = document.getElementsByClassName("team_players_player_name");
var teamPlayerCountry = document.getElementsByClassName("team_players_player_country");

esportsRegions = { "China":"cn", "Global":"", "EU":"eu", "East EU":"east_eu", "North America":"na", "South America":"SA", "SEA & Oceania":"sea" }

for (const [k, v] of Object.entries(esportsRegions)) {

    if (v == window.location.href.split("/esports/")[1]) teamOverViewRegionName.innerText = k;

}

getRecentMatches(0);

for (let i = 0; i < teamRankingRow.length; i++) {

    teamRankingRow[i].addEventListener("click", event => {

        changeTeamsOnClick(i);


    })

}

function changeTeamsOnClick(i) {

        teamRegionalRank.innerText = i + 1;
        teamName.innerText = teams[i]["name"];
        teamPrizeWinnings.innerText = teams[i]["prize_winning"];
        teamOverviewRankPoints.innerText = teams[i]["rank_points"];
        Array.from(teamOverviewStatisticsValues).forEach(element => console.log(element));
        teamOverviewStatisticsValues[0].innerText = teams[i]["winrate"];
        for (const [k, v] of Object.entries(esportsRegions)) {

            if (v == window.location.href.split("/esports/")[1]) teamOverViewRegionName.innerText = k;

        }
        teamOverviewStatisticsValues[1].childNodes[1].innerText = teams[i]["wins"];
        teamOverviewStatisticsValues[1].childNodes[3].innerText = "/ " + teams[i]["draws"] + " /";
        teamOverviewStatisticsValues[1].childNodes[5].innerText = teams[i]["losses"];
        teamOverviewStatisticsValues[2].innerText = teams[i]["current_streak"];
        let streak = teamOverviewStatisticsValues[2];
        if (streak.innerText.split(" ")[1][0] == "w") streak.style.color = "#1ED775";
        else streak.style.color = "red";
        teamOverviewLogo.setAttribute("src", teams[i]["logo"]);
        teamRecentRows = document.getElementsByClassName("team_recent_row");
        Array.from(teamRecentRows).forEach(row => {

            row.remove();

        })
        getRecentMatches(i);
        getRosterplayers(i);

}

function getRecentMatches(i) {

    for (let j = 0; j < 3; j++) {

        if (Object.keys(teams[i]).includes(`recent_match_${j + 1}`)) {

            teamRecentMatches.insertAdjacentHTML("beforeend",
            `<div class = "team_recent_row">vs
                <img class = "team_recent_row_img">
                <div class = "team_recent_row_opponent"></div>
                <div class = "team_recent_row_result"></div>
            </div>`
            )

        getRecentMatchRow(i, j);

        }


    }

}

//fill up recent match rows
function getRecentMatchRow(i, j) {

    let recentRowImg = document.getElementsByClassName("team_recent_row_img")[j];
    let recentRowOpponent = document.getElementsByClassName("team_recent_row_opponent")[j];
    let recentRowResult = document.getElementsByClassName("team_recent_row_result")[j];
    recentRowImg.setAttribute("src", teams[i][`recent_match_${j + 1}`]["opponent_img"]);
    recentRowOpponent.innerText = teams[i][`recent_match_${j + 1}`]["opponent"];
    recentRowResult.innerText = teams[i][`recent_match_${j + 1}`]["result"];


}

function getRosterplayers(i) {

    if (teams[i]["players"].length > 4) {

        for (let j = 0; j < 5; j++) {

            let rosterUnavailables = document.getElementsByClassName("roster_unavailable");
            if (rosterUnavailables.length > 0) rosterUnavailables[0].remove();
            Array.from(teamPlayer).forEach(element => element.style.display = "block");
            teamPlayerImg[j].setAttribute("src", teams[i]["players"][j]["image"]);
            teamPlayerName[j].innerText = teams[i]["players"][j]["name"];
            teamPlayerCountry[j].setAttribute("src", `../static/images/flags/${teams[i]["players"][j]['country']}.png`);

        }

    }

    else {

        let rosterUnavailables = document.getElementsByClassName("roster_unavailable");
        if (rosterUnavailables.length > 0) rosterUnavailables[0].remove();
        Array.from(teamPlayer).forEach(element => element.style.display = "none");
        teamRosterPlayers.insertAdjacentHTML("beforeend",
        `<div class = "roster_unavailable">Roster for this team is unavailable.
        </div>`
        )

    }

}
