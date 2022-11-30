from homepage2vec.model import WebsiteClassifier, Webpage
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logging.debug("Python {}".format(sys.version_info))

model = WebsiteClassifier()
website = Webpage("https://example.com")
website.html = "Example"
scores, embeddings = model.predict(website)

logging.debug("scores {} embeddings {}".format(scores, embeddings))
