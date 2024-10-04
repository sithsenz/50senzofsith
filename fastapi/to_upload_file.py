import os
from fastapi import FastAPI, UploadFile


"""
Dalam venv yang berkaitan, buka file ini dengan arahan berikut di cmd:
  python3 to_upload_file.py

Masukkan alamat berikut di pelayar:
  192.168.50.208:8655/docs

Skrip ini akan memuatnaik file dengan nama files.filename
ke lokasi os.path.join("files", file.filename).
"""


aplikasi: FastAPI = FastAPI()


@aplikasi.post("/file/muatnaik/")
async def muatnaik_file(files: UploadFile):
    isi_file = files.file.read()
    with open(os.path.join("files", files.filename), "wb") as file_ini:
        file_ini.write(isi_file)
    return {"nama_file": files.filename}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(aplikasi, host="192.168.50.208", port=8655)
