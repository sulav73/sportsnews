import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to the database
conn = sqlite3.connect("worldcup.db")
cursor = conn.cursor()

# Create the table to store the data
cursor.execute("CREATE TABLE IF NOT EXISTS wc_article (id INTEGER PRIMARY KEY, title TEXT, headers TEXT, contents TEXT)")

# Scrape the text data from the news article
url = "https://olympics.com/en/news/fifa-world-cup-2022-records-and-stats"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# Extract the title and content of the article
title = soup.find("h1").text
headers = [header.text for header in soup.find_all("h1, h2")]
header_contents = [header.find_next("p").text for header in soup.find_all("h1, h2")]
paragraphs = soup.find_all("p")
content = ' '.join([p.text for p in paragraphs])

# Store the data in the database
try:
    cursor.execute("ALTER TABLE wc_article ADD COLUMN contents TEXT, headers TEXT")
except sqlite3.OperationalError:
    pass
cursor.execute("INSERT INTO wc_article (title, headers, contents) VALUES (?,?,?)", (title, ' '.join(headers), content))

# Close the connection
conn.commit()
conn.close()
