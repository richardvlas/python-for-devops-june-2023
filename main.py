from fastapi import FastAPI
import uvicorn
from devopslib.logic import search_wiki
from devopslib.logic import wiki as wikilogic
from devopslib.logic import phrase as wikiphase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki endpoints"}


@app.get("/search/{value}")
async def search(value: str):
    """
    Page to search in wikipedia
    """
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""
    result = wikiphase(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
