from src.ingest import build_db
from src.rag import ask

mode = input(
    "1: Build DB\n2: Ask Question\n"
)

if mode == "1":
    build_db()

elif mode == "2":

    question = input("Question: ")

    answer = ask(question)

    print("\nAnswer")
    print(answer)