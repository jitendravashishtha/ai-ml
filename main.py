from langchain_ollama.llms import OllamaLLM # Import the Ollama LLM wrapper
from langchain_core.prompts import ChatPromptTemplate # Import prompt template for chat
from vector import retriever # Import the retriever for fetching relevant reviews

# Initialize the language model with the specified model name
model = OllamaLLM(model="llama3.2")

# Define the prompt template for the chatbot.
# This template provides context (relevant reviews) and the user's question to the model.
template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

# Create a prompt object from the template, which will be filled with actual data at runtime
prompt = ChatPromptTemplate.from_template(template)

# Combine the prompt and the model into a chain.
# The chain takes input variables, formats the prompt, and sends it to the model for a response.
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    # Use the retriever to fetch reviews relevant to the user's question   
    reviews = retriever.invoke(question)

    # Pass the reviews and question to the chain to generate an answer
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)