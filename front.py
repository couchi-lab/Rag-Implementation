from fastapi import FastAPI
from conection.AI_con import communicate
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "server running"}


@app.get("/chat")
async def chat(prompt: str):
    result = await communicate(prompt)

    return {
        "input": prompt,
        "output": result
    }
