import validators
from pydantic import BaseModel
from homepage2vec.model import WebsiteClassifier, Webpage
from fastapi import FastAPI, Depends, HTTPException, status
import os
import logging

logging.basicConfig(level=logging.DEBUG)

model = WebsiteClassifier()

WARMUP_MODEL = os.getenv("WARMUP_MODEL", 'False').lower() in ('true', '1', 't')
if WARMUP_MODEL:
    logging.info("Warming up model")
    website = Webpage("https://example.com")
    website.html = "Example"
    scores, embeddings = model.predict(website)
    logging.info("Model warmed up")

logging.info("FastAPI starting")
app = FastAPI()

class ClassifyRequest(BaseModel):
    url: str
    html: str = None

@app.get("/")
def read_root():
    return {"POST with [url] or [url, html] to / with a bearer token"}

@app.post("/")
def classify(classify_request: ClassifyRequest):
    if (not validators.url(classify_request.url)):
      raise HTTPException(status_code=403, detail="Invalid URL")

    if (not classify_request.html):
      raise HTTPException(status_code=403, detail="Must pass html")

    website = Webpage(classify_request.url)
    website.html = classify_request.html
    
    scores, embeddings = model.predict(website)
    return {"scores": scores, "embeddings": embeddings, "url": classify_request.url}
