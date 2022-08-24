from textblob import TextBlob

from newspaper import Article

url = "https://timesofindia.indiatimes.com/city/mangaluru/another-chilling-murder-in-mangaluru-youth-hacked-to-death/articleshow/93199887.cms"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)


def senti(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


print(senti(text))
