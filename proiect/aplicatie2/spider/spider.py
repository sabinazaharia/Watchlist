import requests
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/chart/top/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find(class_='lister-list')


# Extract all titles and years from list
table_titles = table.find_all(class_='titleColumn')
titles = []
years = []

for title in table_titles:
    title_cell = title.find('a')
    year_cell = title.find('span')
    title_name = title_cell.text.strip()
    year = year_cell.text.strip()
    titles.append(title_name)
    years.append(year)

# Extract all ratings from list

table_ratings = table.find_all(class_='ratingColumn imdbRating')
ratings = []

for rating in table_ratings:
    rating_cell = rating.find('strong')
    note = rating_cell.text.strip()
    ratings.append(note)

