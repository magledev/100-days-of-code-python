from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

full_page = response.text
soup = BeautifulSoup(full_page, "html.parser")
# movie_rank = soup.find_all(name="span", class_="jsx-4245974604 listicle-item-count")
movie_titles = soup.find(name="h3", class_="jsx-4245974604 listicle-item-count")
print(movie_titles)
