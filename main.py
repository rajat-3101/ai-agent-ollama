from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever 

# Initialize the Ollama LLM with the model name
model = OllamaLLM(model="llama3.2")

template = """ 
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer : {question}

"""

promt = ChatPromptTemplate.from_template(template)
chain = promt | model


while True:
    print("\n\n-------------")
    user_input = input("Enter your question (or 'q' to quit): ")
    print("\n\n")
    if user_input.lower() == 'q':
        break

    reviews = retriever.invoke(user_input) 
    # Invoke the chain with the user input
    result = chain.invoke({
        "reviews": reviews,
        "question": user_input
    })

    print(result)