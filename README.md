
# Week 9 - Chatbot Development Using Ollama

## 1. Project Overview

This project demonstrates the development of an interactive AI chatbot using Python and Ollama. The chatbot uses the Llama 3.2 1B language model to answer educational questions.

## 2. Objectives

- Understand the architecture of a local AI chatbot.
- Build a chatbot using Python and Ollama.
- Maintain conversation context during a chat session.
- Save conversations with timestamps.
- Evaluate chatbot responses using sample questions.

## 3. Technologies Used

- Python
- Ollama
- Llama 3.2 1B
- Pandas
- Jupyter Notebook
- Visual Studio Code

## 4. Project Structure

```text
Chatbot_Development/
├── dataset/
│   ├── chat_history.csv
│   ├── chatbot_logs.txt
│   ├── sample_questions.csv
│   └── responses.csv
├── notebook/
│   └── Week9_Chatbot_Development.ipynb
├── chatbot.py
├── generate_responses.py
├── README.md
└── requirements.txt
```

## 5. Features

- Interactive command-line chatbot.
- Uses a locally running language model.
- Maintains conversation history during the session.
- Saves user questions and chatbot answers with timestamps.
- Tests the chatbot with sample educational questions.
- Stores chat logs for later analysis.

## 6. Installation

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

Make sure Ollama is installed and the model is available:

```bash
ollama pull llama3.2:1b
```

## 7. How to Run

Start the chatbot:

```bash
python chatbot.py
```

Type a question and press Enter to receive an answer.

Type `exit` to stop the chatbot.

Generate responses for the sample questions:

```bash
python generate_responses.py
```

## 8. Dataset Description

- `sample_questions.csv`: Contains sample educational questions.
- `chat_history.csv`: Stores conversation timestamps, questions, and answers.
- `chatbot_logs.txt`: Stores readable conversation logs.
- `responses.csv`: Stores answers generated for the sample questions.

## 9. Strengths

- Runs locally using Ollama.
- Provides simple educational explanations.
- Supports multi-turn conversations.
- Saves conversations for evaluation.

## 10. Limitations

- Responses may contain factual errors.
- A small language model may provide incomplete explanations.
- Ollama must be running for the chatbot to work.
- The chatbot is designed mainly for educational questions.

## 11. Conclusion

This project demonstrates how Python and Ollama can be used to build an interactive educational chatbot. The project includes conversation history, timestamped logging, a sample question dataset, and response evaluation.

## 12. Future Enhancement

The chatbot can be improved by adding a graphical user interface, more advanced conversation management, and LangChain integration.
