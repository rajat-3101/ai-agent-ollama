# README.md

This project is an AI-powered pizza restaurant review assistant built with LangChain, Ollama, and Chroma. It enables users to ask questions about a pizza restaurant, leveraging a database of realistic customer reviews to provide relevant, context-aware answers.

## Features

- **Review Database:** Uses [`realistic_restaurant_reviews.csv`](realistic_restaurant_reviews.csv ) containing detailed pizza restaurant reviews.
- **Vector Search:** Embeds reviews using Ollama's embedding model and stores them in a Chroma vector database (chroma_langchain_db/).
- **Retrieval-Augmented Generation:** When a user asks a question, the system retrieves the most relevant reviews and passes them to a language model for a tailored response.
- **Interactive CLI:** Users interact via the command line, entering questions and receiving expert answers based on real customer experiences.

## How It Works

1. **Data Loading:** Reviews are loaded from [`realistic_restaurant_reviews.csv`](realistic_restaurant_reviews.csv ).
2. **Embedding & Storage:** Reviews are embedded using Ollama and stored in Chroma for fast similarity search.
3. **Retrieval:** When a question is asked, the top relevant reviews are retrieved.
4. **Answer Generation:** The retrieved reviews and user question are sent to an Ollama LLM, which generates an expert answer.
5. **User Interaction:** The process repeats until the user quits.

## Main Files

- [`main.py`](main.py ): Runs the interactive question-answer loop.
- [`vector.py`](vector.py ): Handles review loading, embedding, and vector database setup.
- [`realistic_restaurant_reviews.csv`](realistic_restaurant_reviews.csv ): Source of restaurant reviews.

## Requirements

See [`requirements.txt`](requirements.txt ) for dependencies.

## Usage

```sh
pip install -r requirements.txt
python main.py
```

Ask any question about the pizza restaurant and get answers based on real reviews!

---

**Project Structure:**

- [`main.py`](main.py )
- [`vector.py`](vector.py )
- [`realistic_restaurant_reviews.csv`](realistic_restaurant_reviews.csv )
- [`chroma_langchain_db`](chroma_langchain_db )
- [`requirements.txt`](requirements.txt )