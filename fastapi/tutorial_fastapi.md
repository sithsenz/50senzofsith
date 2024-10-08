# FastAPI

## Getting Started: Installing FastAPI
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints. To begin using FastAPI, follow the steps below for installation. Before installing FastAPI, it’s a good practice to set up a virtual environment. This ensures that your project dependencies are isolated from your global Python installation. The simplest way to install everything you need is by using the fastapi[all] option, which also includes uvicorn (the server that will run your application) and other important packages:

```python
pip install "fastapi[all]"
```

This command installs FastAPI along with:
+ Uvicorn: A lightning-fast ASGI server that runs FastAPI applications
+ Pydantic: For data validation and settings management using Python type hints
+ Starlette: The web micro-framework that FastAPI builds upon for routing, middleware, and more

Once the installation is complete, you’re ready to start developing your FastAPI app.

## Your First FastAPI Application: Basic Template
Once FastAPI is installed, we can move on to writing our first FastAPI application. This basic code template will get you started with a minimal FastAPI app, which you can expand on as needed. This code should be saved as a Python file, such as `main.py`:

```python
import uvicorn

from fastapi import FastAPI


@app: FastAPI = FastAPI()


if __name__ == "__main__":
  uvicorn.run(app=app, host="0.0.0.0", port=8000)
```

### Explanation:
+ `FastAPI()`: This line initializes the FastAPI app, creating an instance of the framework
+ `uvicorn.run()`: Uvicorn is an ASGI server that runs your FastAPI application. The `run()` method launches the app on `host="0.0.0.0"` (which makes it accessible to any device on the network) and `port=8000`

### Development Mode:
For ease of development, you can run the app in "reload" mode. This allows the server to automatically reload any changes made to the code, making the development process faster:

```python
if __name__ == "__main__":
  uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
```

### Running Your App
To run the application, execute the following command in your terminal (ensure you are inside the project directory where your `main.py` file is located):

```python
python3 main.py
```

Your application will now be running at `http://127.0.0.1:8000` and ready to handle requests.

## Handling Requests: Using the GET Method
The GET method is one of the most common HTTP methods used to request data from a server. In FastAPI, you can define routes to handle GET requests very easily.

### Basic GET Request
Let’s start with a simple example. The following code defines a basic route that listens for GET requests at the root URL `/` and responds with a simple message:

```python
@app.get("/")
async def home():
  return "Hello, World!"
```

### Explanation:
+ `@app.get("/")`: This decorator registers a route with the FastAPI app that listens for HTTP GET requests at the `/` endpoint
+ `async def home()`: The home function is defined as asynchronous, which allows it to handle more requests efficiently without blocking the server
+ `return "Hello, World!"`: This returns a basic string as a response when the root URL is accessed

With this in place, if you run the app and navigate to `http://127.0.0.1:8000`, you should see the response "Hello, World!" displayed on the browser or in any HTTP client.

### Using Templates to Render HTML
FastAPI also supports rendering HTML templates using Jinja2, allowing you to create dynamic web pages. Here’s how you can return an HTML page instead of a plain text response `templates/home.html`:

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

### Explanation:
+ `Jinja2Templates()`: This object initializes the Jinja2 templating engine, pointing to the `templates` directory where your HTML files are stored
+ `TemplateResponse()`: This function renders the `home.html` template and returns it as the HTTP response. It also passes `context` variables like `dictionary_01` and `list_01` to the template

You can create a corresponding `home.html` file inside the `templates` folder:

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

### Explanation:
+ `{{ dict_obj["key01"] }}`: This expression displays the value associated with `key01` in the dictionary passed to the template
+ `{% for item in list_obj %}`: This loops through the list `list_obj` and generates a list item `<li>` for each element

### Combining Data and HTML Templates
This integration of data and HTML allows you to build interactive web pages with dynamic content based on the data your API serves. Whether it's simple text responses or complex HTML pages, FastAPI makes handling GET requests straightforward and efficient.

## Uploading Files: Handling POST Requests
In addition to handling data retrieval with GET requests, FastAPI also allows you to accept and process data from clients using POST requests. This section will cover how to upload files through POST requests and store them on the server.

### File Upload Example
The following example demonstrates how to upload one or more files from a client to the server:

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

### Explanation:
+ `UploadFile`: This type is used to handle file uploads. It abstracts away many details, like how the file is read, and provides a simple interface for file handling
+ `List[UploadFile]`: FastAPI allows you to upload multiple files by accepting a list of `UploadFile` objects
+ Reading and Saving the Files: The uploaded files are read as binary content and then saved to the `files` directory. Each file is written to the disk using its original filename `f.filename`
+ `RedirectResponse("/")`: After the files are successfully uploaded, the user is redirected back to the home page with a `303 (See Other)` status code

### File Upload HTML Form
To allow users to upload files, you need an HTML form that lets them select files and submit them to the `/files/upload/` endpoint:

```html
<body>
  <form method="post" action="/file/upload/" enctype="multipart/form-data">
    <input name="files" type="file" multiple>
    <input type="submit">
  </form>
</body>
```

### Explanation:
+ `enctype="multipart/form-data"`: This attribute is required when uploading files via HTML forms, as it tells the browser to send the file data in a format the server can handle
+ `<input type="file">`: This input allows users to select files from their local system
+ `multiple`: The multiple attribute allows users to select and upload more than one file at a time.

### Running the Upload Feature
Once the HTML form is submitted, the selected `files` are sent to the server via a POST request to the `/files/upload/` endpoint. FastAPI then processes the files and stores them in the specified directory `files`.

After the upload is complete, the user is redirected to the home page, where additional actions (like viewing the uploaded files) can be taken.

### Dynamic Routing: GET Method with Path Parameters
In addition to handling simple GET requests, FastAPI allows you to create more dynamic routes by accepting parameters in the URL path. This is particularly useful when building APIs that need to handle varying data based on user input or other criteria.

### Example: Serving Files with Path Parameters
In this example, we’ll extend our previous file upload functionality to include a dynamic route that serves files for preview or download based on their filenames.

```python
import os

from fastapi import Request
from fastapi.responses import FileResponse
from glob import glob


@aplikasi.get("/")
async def home(request: Request):
    _list_of_files: list = glob(os.path.join("files", "*.*"))
    list_of_files: list = [os.path.split(file)[1] for file in _list_of_files]

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "files": list_of_files
        }
    )


@aplikasi.get("/preview/{file_name}")
async def preview_file(file_name: str):
    return FileResponse(path=os.path.join("files", file_name))
```

### Explanation:
+ `@app.get("/preview/{file_name}")`: This route uses a path parameter `{file_name}` that allows users to specify the file they want to preview by including the filename in the URL
+ `FileResponse()`: This function is used to send files back to the client, either for previewing in the browser or for downloading. It retrieves the file from the server's `files` directory
+ Listing Files on the Home Page: In the root route `/`, we use `glob` to fetch all files stored in the `files` directory and display their filenames on the homepage. The filenames are passed to the HTML template as `context`

### Displaying Files on the Homepage

Here’s the corresponding HTML template that displays the list of uploaded files as clickable links:

```html
<body>
  <ul>
    {% for f in files %}
    <li><a href="{{ url_for('preview_file', file_name=f) }}">{{ f }}</a></li>
    {% endfor %}
  </ul>
</body>
```

### Explanation:
+ `{% for f in files %}`: This Jinja2 template code loops through the list of filenames passed to the template and generates a clickable link for each file
+ `{{ url_for('preview_file', file_name=f) }}`: The `url_for()` function dynamically creates the URL for the `preview_file` route by inserting the filename as a path parameter

### Dynamic Routing in Action
With this setup, users can visit the root page to see a list of uploaded files. Each file is a clickable link that takes them to the corresponding URL to either preview or download the file. This demonstrates how path parameters allow you to build dynamic routes in FastAPI that respond to user input or other variables in the URL.
