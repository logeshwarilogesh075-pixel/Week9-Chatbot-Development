
import csv
from datetime import datetime
from pathlib import Path

import ollama

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"

QUESTIONS_FILE = DATASET_DIR / "sample_questions.csv"
RESPONSES_FILE = DATASET_DIR / "responses.csv"

MODEL = "llama3.2:1b"


def main():
    # Read questions from the CSV file
    with open(QUESTIONS_FILE, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    # Skip the header and ignore any duplicate header rows
    questions = [
        line.strip().strip('"')
        for line in lines[1:]
        if line.strip()
        and line.strip().strip('"').lower() != "question"
    ]

    if not questions:
        print("No questions found. Please check sample_questions.csv.")
        return

    print(f"Found {len(questions)} questions.")
    print("Generating responses...\n")

    # Save answers to responses.csv
    with open(
        RESPONSES_FILE, "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "question", "response"])

        for index, question in enumerate(questions, start=1):
            print(f"Question {index}/{len(questions)}: {question}")

            try:
                result = ollama.chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an Education Assistant. "
                                "Answer in simple English."
                            ),
                        },
                        {"role": "user", "content": question},
                    ],
                )

                answer = result["message"]["content"]

            except Exception as error:
                answer = f"ERROR: {error}"
                print(f"Error: {error}")

            timestamp = datetime.now().astimezone().isoformat(
                timespec="seconds"
            )

            writer.writerow([timestamp, question, answer])
            file.flush()

    print("\nFinished!")
    print(f"Saved {len(questions)} responses to:")
    print(RESPONSES_FILE)


if __name__ == "__main__":
    main()
