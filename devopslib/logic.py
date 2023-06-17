import wikipedia
from textblob import TextBlob

def wiki(name="War Goddess", length=1):
    """
    Get a Wikipedia article and print a summary.
    """
    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for a given Name"""
    return wikipedia.search(name)

def phrase(name):
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases

if __name__ == "__main__":
    # print(wiki("War Goddess", 100))
    print(search_wiki("LeBronJames"))
    # print(phrase("War Goddess"))
    print(phrase("War Goddess"))