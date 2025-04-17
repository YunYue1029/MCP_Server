from fastapi import FastAPI
from models.tool_call import MCPRequest
from tools import TOOL_HANDLERS
from fastapi.responses import JSONResponse
from fastapi import File, UploadFile

app = FastAPI()

@app.post("/run")
async def run_mcp(request: MCPRequest):
    responses = []

    for tool_call in request.tool_calls:
        name = tool_call.function["name"]
        args = tool_call.function.get("arguments", {})
        handler = TOOL_HANDLERS.get(name)

        if handler:
            output = handler(args)
            responses.append({
                "tool_call_id": tool_call.id,
                "output": output
            })
        else:
            responses.append({
                "tool_call_id": tool_call.id,
                "error": f"No such tool: {name}"
            })

    return JSONResponse(content={"results": responses})

@app.post("/upload_user_audio")
async def upload_user_audio(file: UploadFile = File(...)):
    contents = await file.read()
    # Ensure the audio directory exists
    with open(f"user_audio/{file.filename}", "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

@app.post("/upload_speech_audio")
async def upload_speech_audio(file: UploadFile = File(...)):
    contents = await file.read()
    # Ensure the audio directory exists
    with open(f"speech_audio/{file.filename}", "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

@app.get("/")
def root():
    return {"message": "MCP server ready!"}