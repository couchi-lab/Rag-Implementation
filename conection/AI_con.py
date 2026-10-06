import sys
from pathlib import Path
Path=sys.path.append(str(Path(__file__).parent.parent))
from setting import AI_KEY
from groq import Groq


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

if __name__ == "__main__":
    print("Directory running the script AI_con.py\n")
    print(communicate("Explain the importance of fast language models"))
