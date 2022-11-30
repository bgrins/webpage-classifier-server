# webpage-classifier-server

A demo server wrapper around https://github.com/epfl-dlab/homepage2vec.

## Setup

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt 
```

## Running 

Local:
```sh
uvicorn main:app --reload
```

Docker:
```sh
docker rm -f fastapi-test-container && docker build -t fastapi-test . && docker run -it --name fastapi-test-container -e PORT=8080 -p 8000:8080 fastapi-test
```

After that, load http://localhost:8000/docs, or make a request like so:

```
curl -X POST http://localhost:8000 -d '{"html":"<h1>sports sports sports<h1>", "url":"https://example.com"}' -H "Content-Type: application/json"
```

Which should return something like

```json
{
  "scores": {
    "Arts": 2.5276106541127774e-08,
    "Business": 6.061993644834729e-07,
    "Computers": 8.69573705131188e-06,
    "Games": 5.664257951565332e-09,
    "Health": 4.4610296754399315e-06,
    "Home": 7.144159393297722e-19,
    "Kids_and_Teens": 1.4455079622166522e-07,
    "News": 0.3982723355293274,
    "Recreation": 9.85487190519052e-07,
    "Reference": 0.986739993095398,
    "Science": 2.1317753635230474e-05,
    "Shopping": 3.280406133399083e-07,
    "Society": 0.00023037487699184567,
    "Sports": 0.999995231628418
  },
  "embeddings": [
    -0.24816516041755676,
    1.058244228363037,
    -10.483004570007324,
    -7.135867118835449,
    -15.366525650024414,
    5.949895858764648,
    -1.9832568168640137,
    -11.333369255065918,
    -6.8231401443481445,
    0.44682779908180237,
    -1.6561615467071533,
    -1.9870593547821045,
    ...
  ],
  "url": "https://example.com"
}
```

There's also a helper script that can be used like:

```
./categorize.sh https://example.com
```

## Deploying

```
gcloud config set project $PROJECT_NAME
gcloud config set run/region us-central1
gcloud run deploy --source .
gcloud run services update $PROJECT_NAME --memory 4G
```
