import sqlite3
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("punkt")


# Connect to the database
conn = sqlite3.connect('worldcup.db')
cursor = conn.cursor()

# Query the wcarticle table
query = "SELECT title, contents FROM wc_article"
cursor.execute(query)

# Tokenize the text data into sentences
for row in cursor.fetchall():
    title = row[0]
    contents = row[1]
    title_sentences = sent_tokenize(title)
    contents_sentences = sent_tokenize(contents)
words_title_sentences = [nltk.word_tokenize(sent) for sent in title_sentences]
words_contents_sentences = [nltk.word_tokenize(sent) for sent in contents_sentences]

print(words_title_sentences)
print(words_contents_sentences)
# Close the database connection
conn.close()

