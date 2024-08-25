from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/")
async def main():
    return {"key":"value"}