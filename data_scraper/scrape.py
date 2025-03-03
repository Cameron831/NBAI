from bs4 import BeautifulSoup
import requests

# get html content for games played on March 2, 2025
url = "https://www.basketball-reference.com/boxscores/index.fcgi?month=3&day=2&year=2025"
response = requests.get(url)
html_content = response.text

# create bs4 object with the html content retrieved
soup = BeautifulSoup(html_content, 'html.parser')
# find the div containing the game summaries for that day
game_summaries = soup.find("div", class_='game_summaries')
# get all links in the summaries table
games = game_summaries.find_all("a")
# find all links where the text is 'Final'; these are the links to the box scores for each game
for game in games:
    if game.text == "Final":
        print("https://www.basketball-reference.com" + game['href'])
