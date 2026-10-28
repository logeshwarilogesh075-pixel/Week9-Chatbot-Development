
import csv
from datetime import datetime
from pathlib import Path

import ollama

# Project folders and files
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"

HISTORY_FILE = DATASET_DIR / "chat_history.csv"
LOG_FILE = DATASET_DIR / "chatbot_logs.txt"

MODEL = "llama3.2:1b"

# Create the CSV file and its headings if it doesn't exist
DATASET_DIR.mkdir(parents=True, exist_ok=True)

if not HISTORY_FILE.exists():
    with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "user_question", "chatbot_response"])

# Chatbot's role
SYSTEM_PROMPT = """
You are an Education Assistant chatbot.
Help students understand computer science, programming,
mathematics, and general academic topics.
Use simple English and step-by-step explanations.
If you are unsure about an answer, say so.
"""

# Conversation history helps the chatbot remember earlier messages
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def save_conversation(question, response, timestamp):
    """Save conversations to CSV and text log files."""

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, response])

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"User: {question}\n")
        file.write(f"Chatbot: {response}\n")
        file.write("-" * 50 + "\n")


def run_chatbot():
    print("=" * 50)
    print("          EDUCATION AI CHATBOT")
    print(f"          Model: {MODEL}")
    print("Type 'exit' to stop the chatbot.")
    print("=" * 50)

    # Check whether the model is available
    try:
        ollama.show(MODEL)
    except Exception as error:
        print("Could not connect to the model.")
        print("Check that Ollama is running and the model is installed.")
        print(f"Details: {error}")
        return

    # Keep chatting until the user types exit
    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break

        if not question:
            print("Chatbot: Please enter a question.")
            continue

        messages.append({"role": "user", "content": question})

        try:
            result = ollama.chat(
                model=MODEL,
                messages=messages
            )

            answer = result["message"]["content"]
            timestamp = datetime.now().astimezone().isoformat(
                timespec="seconds"
            )

            print(f"\nChatbot: {answer}")

            messages.append(
                {"role": "assistant", "content": answer}
            )

            save_conversation(question, answer, timestamp)

        except Exception as error:
            messages.pop()
            print("Sorry, I could not generate a response.")
            print(f"Error: {error}")


if __name__ == "__main__":
    run_chatbot()
