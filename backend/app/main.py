from fastapi import FastAPI,File,UploadFile,responses,Request,Response
from fastapi.middleware.cors import CORSMiddleware
from fileservices import convert_word_to_csv
import uuid
import os
app = FastAPI()


origins :list = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


UPLOAD_URL = "download/file"
@app.post("/file/upload")
async def upload_file(file :UploadFile = File(...)):
    if not file.filename.endswith("docx"):
        return responses.JSONResponse({
            "error":{"detail" :" FIle most be a docx extension"},
            "message" : "FIle most be docx extension",
            "status" : 400
        })


    try:
        temp_file = f"{uuid.uuid4()}.docx"
        with open(temp_file, "wb") as buffer:
            buffer.write(await file.read())
        filename :str = str(uuid.uuid4())
        otuput_file_name = f'{UPLOAD_URL}/{filename}.csv'
        convert_word_to_csv(temp_file,output_file=otuput_file_name)
        
        os.remove(temp_file)
        return responses.JSONResponse({"filename":f'{filename}.csv'},status_code=201)


    except Exception as e:
        print(e)
        return responses.JSONResponse("Server error", status_code=500)



@app.get("/get/file/{filename}")
async def get_file_name(filename :str):
    file_path  = os.path.join(UPLOAD_URL,filename)
    try:
        with open(file_path,mode="r") as file:
            return responses.FileResponse(file_path)
    except FileNotFoundError:
        
        return responses.JSONResponse("File does not exists .", status_code=404)
    return {"text" : "hi "}
    