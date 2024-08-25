from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/api-server")
async def main():
    return {"key":"value"}