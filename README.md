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

**Warning**: The first run will be VERY slow to load

Visit `http://localhost:3007/docs` in a browser once it's loaded

Call it in python like this:

```
TODO
```
