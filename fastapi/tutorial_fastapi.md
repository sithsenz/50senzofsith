# FastAPI

## Installation
At cmd line, inside an environment:

```python
pip install "fastapi[all]"
```

## Basic Code Template
Basic code:

```python
# main.py
import uvicorn

from fastapi import FastAPI


@app: FastAPI = FastAPI()


if __name__ == "__main__":
  uvicorn.run(app=app, host="0.0.0.0", port=8000)
  # or during development, for convenient reload
  # uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
```
