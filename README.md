# BreadRank

A small reranker API service powered by mixedbred.ai reranker model.  It's currently using the mxbai-rerank-xsmall-v1 model.

## Local Installation

```
pip install -r requirements.txt
```

## Local Running

```
uvicorn main:app --host 0.0.0.0 --port 3007
```

## Docker

```
docker build -t breadrank .
docker run -d -p 3007:3007 breadrank
```

**Warning**: The first run will be VERY slow to load

Visit `http://localhost:3007/docs` in a browser once it's loaded

Call it in python like this:

```
import requests
import json

# Define the URL of your FastAPI endpoint
url = "http://localhost:3007/rerank/"

# Define the data you want to send to the endpoint
query = "Your query here"
documents = ["Document 1", "Document 2", "Document 3"]
top_k = 2

data = {"query": query, "documents": documents, "top_k": top_k}

# Make the POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Request failed with status code {response.status_code}")
```
