import os
import uvicorn

from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from glob import glob
from typing import List


"""
Dalam venv yang berkaitan, buka file ini dengan arahan berikut di cmd:
  python3 preview_and_upload_file.py

Masukkan alamat berikut di pelayar:
  192.168.112.103:8655/

Templat HTML utama.html disimpan dalam folder templat

Skrip ini akan memaparkan senarai nama-nama file dalam folder files berserta pautannya

Skrip ini akan memuatnaik file dengan nama files.filename
ke lokasi os.path.join("files", file.filename).
"""


aplikasi: FastAPI = FastAPI()


templat: Jinja2Templates = Jinja2Templates(directory="templat")


@aplikasi.get("/")
async def hlm_utama(request: Request):
    _senarai_file: list = glob(os.path.join("files", "*.*"))
    senarai_file: list = []


    for file in _senarai_file:
        senarai_file.append(os.path.split(file)[1])


    return templat.TemplateResponse(
        request=request,
        name="utama.html",
        context={
            "files": senarai_file
        }
    )


@aplikasi.get("/prabaca/{nama}")
async def prabaca_file(nama:str):
    return FileResponse(path=os.path.join("files", nama))


@aplikasi.post("/file/muatnaik/", response_class=HTMLResponse)
async def muatnaik_file(files: List[UploadFile]):
    files_berjaya_dimuatnaik: list = []
    
    for file in files:
        isi_file = file.file.read()
        with open(os.path.join("files", file.filename), "wb") as file_semasa:
            file_semasa.write(isi_file)
            files_berjaya_dimuatnaik.append(file.filename)
    
    return RedirectResponse("/", status_code=303)


if __name__ == "__main__":
    uvicorn.run(aplikasi, host="192.168.112.103", port=8655)
