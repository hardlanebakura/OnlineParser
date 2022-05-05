This is a clone of the Dotabuff website, popular statistics parsing website for online multiplayer game DotA 2. I have added some additional features such as the counterpicker and esports tracker.

This project has following features:
    <ul>
        <li>Parse matches statistics</li>
        <li>Parse players statistics</li>
        <li>Parse heroes statistics</li>
        <li>Parse items statistics</li>
        <li>Parse esports matches and players</li>
        <li>Find the best hero pick for the selected match or for any given lineups</li>
        <li>Automation testing</li>
        <li>Unit testing
    </ul>

It scraps the data from the web via Selenium automation tool and the API calls and puts it into the Mongo Database.

It works for all matches and, with several hundred players tested, on all players.

<b>Example searches:<b>

42735465
395248349
122765274
928188595
345104544

6525357182
6553666833

Hosted on Heroku: <a href = "https://pythonflaskdotabuff.herokuapp.com/">https://pythonflaskdotabuff.herokuapp.com/</a>

(searches are very slow there due to their dynos being very limited, on local server runs very fast)

