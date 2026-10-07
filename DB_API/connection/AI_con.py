import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI
from setting import AI_KEY
from groq import Groq

app = FastAPI()

client = Groq(
    api_key=AI_KEY,
) 
def communicate(user_input: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="openai/gpt-oss-120b",
    )

    return chat_completion.choices[0].message.content

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
