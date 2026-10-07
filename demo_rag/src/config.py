from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

PDF_PATH = str(BASE_DIR / "data" / "test.pdf")
CHROMA_PATH = str(BASE_DIR / "db")
MODEL_NAME = os.getenv("MODEL_NAME")
AI_KEY = os.getenv("AI_KEY")
MODEL = os.getenv("MODEL")
if __name__ == "__main__":
    print("PDF_PATH:", PDF_PATH)
    print("CHROMA_PATH:", CHROMA_PATH)
    print("MODEL_NAME:", MODEL_NAME)
    print("AI_KEY:", AI_KEY)
    print("MODEL:", MODEL)
