# FastAPI

## Installation
At cmd line, inside an environment:

```python
pip install "fastapi[all]"
```

## Basic Code Template
Basic code `main.py`:

```python
import uvicorn

from fastapi import FastAPI


@app: FastAPI = FastAPI()


if __name__ == "__main__":
  uvicorn.run(app=app, host="0.0.0.0", port=8000)
  # or during development, for convenient reload
  # uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
```

## Get Method
Basic code for routing `main.py`:

```python
@app.get("/")
async def home():
  return "Hello, World!"
```

Basic code for routing `main.py` with html template `templates/home.html`:

```python
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates: Jinja2Templates = Jinja2Templates(directory="templates")


# eg. dictionary, list
dictionary_01: dict = {"key01": value01, "key02": value02,...}
list_01: list = [list_item01, list_item02,...]


@app.get("/")
async def home(request: Request):
  return templates.TemplateResponse(
    request=request,
    name="home.html",
    context={
      "dict_obj": dictionary_01,
      "list_obj": list_01
    }
  )
```

Corresponding html file `templates/home.html`:

```html
<body>

  <!--variables-->
  <p>{{ dict_obj["key01"] }}</p>

  <!--expression-->
  <ul>
  {% for item in list_obj %}
    <li>item</li>
  {% endfor %}
  </ul>

</body>
```

## Post Method
Basic code `main.py` for uploading local file(s) to folder `files`

```python
import os

from fastapi import UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List


@app.post("/files/upload/", response_class=HTMLResponse)
async def upload_file(files: List[UploadFile]):
  for f in files:
    file_content = f.file.read()
    with open(os.path.join("files", f.filename), "wb") as file_new:
      file_new.write(file_content)
    
  return RedirectResponse("/", status_code=303)

```

Corresponding html file `templates/home.html`

```html
<body>
  <form method="post" action="/file/upload/" enctype="multipart/form-data">
    <input name="files" type="file" multiple>
    <input type="submit">
  </form>
</body>
```

### Get method with path parameter
Get method that returns a link to file(s) in folder `files` and can be used to preview or download the file(s)

```python
import os

from fastapi import Request
from fastapi.responses import FileResponse
from glob import glob


@aplikasi.get("/")
async def home(request: Request):
    _list_of_files: list = glob(os.path.join("files", "*.*"))
    list_of_files: list = [os.path.split(file)[1] for file in _list_of_files]

    return templat.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "files": list_of_files
        }
    )


@aplikasi.get("/preview/{file_name}")
async def preview_file(file_name:str):
    return FileResponse(path=os.path.join("files", file_name))
```

Corresponding html file `templates/home.html`

```html
<body>
  <ul>
    {% for f in files %}
    <li><a href="{{ url_for('preview_file', file_name=f) }}">{{ f }}</a></li>
    {% endfor %}
  </ul>
</body>
```

