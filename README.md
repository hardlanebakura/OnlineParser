This is a clone of the Dotabuff website, popular statistics parsing website for online multiplayer game DotA 2. I have added some additional features such as the counterpicker and esports tracker.

This project has following features:
    <ul>
        <li>Parse matches statistics</li>
        <li>Parse players statistics</li>
        <li>Parse heroes statistics</li>
        <li>Parse items statistics</li>
        <li>Parse esports matches and players</li>
        <li>Find the best hero pick for the selected match or for any given lineups</li>
        <li>
    </ul>

It scraps the data from the web via Selenium automation tool and the API calls and puts it into the Mongo Database.

It works for all matches and for most of players, in rare occasions it will fail when the searched player has very little data.

<b>Example searches:<b>

42735465
395248349
122765274
928188595
345104544

6525357182
6553666833

