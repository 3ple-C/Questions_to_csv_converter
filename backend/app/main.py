from fastapi import FastAPI,File,UploadFile,responses
from fileservices import convert_word_to_csv
import uuid
import os
app = FastAPI()
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
        return responses.JSONResponse({"filename":filename})


    except Exception as e:
        print(e)
        return responses.JSONResponse("Server error", status_code=500)



@app.get("get/file/{filename}")
async def get_file_name(filename :str):
    file_path :str = os.path.join(UPLOAD_URL,filename)
    print(file_path)
    return {"text" : "hi "}
    