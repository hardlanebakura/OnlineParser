This is a website for parsing matches in online multiplayer games. I have added some additional features such as the counterpicker and esports tracker.

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

<img src = "https://user-images.githubusercontent.com/74912567/167113490-31fe10b4-4e7e-48b9-be7d-ab8af1c3d9a6.png" width = "230" height = "170">
<img src = "https://user-images.githubusercontent.com/74912567/167114403-decf581d-3e8c-4184-a020-16ca66d30f08.png" width = "230" height = "170">
<img src = "https://user-images.githubusercontent.com/74912567/167114613-f3f1ab2d-1500-452f-b263-e46a85ea6583.png" width = "230" height = "170">
It scraps the data from the web via Selenium automation tool and the API calls and puts it into the Mongo Database.

It works for all matches and, with several hundred players tested, on all players.

<b>Example searches:<b>

6525357182
6553666833
6549930254

42735465
395248349
122765274
928188595
345104544


Hosted on Heroku: <a href = "https://pythonflaskdotabuff.herokuapp.com/">https://pythonflaskdotabuff.herokuapp.com/</a>

(searches are very slow there due to their dynos being very limited, on local server runs very fast)

(sometimes API for gathering data goes down, it doesn't affect existing pages but affects dynamic search pages via the searchbar)
