from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    docs=retriever.invoke(question)

    reviews = "\n".join([
        f"- {d.page_content} (Rating: {d.metadata.get('rating')}, "
        f"Date: {d.metadata.get('date')}, "
        f"City: {d.metadata.get('city')}, "
        f"Restaurant: {d.metadata.get('restaurant')})"
        for d in docs
    ])

    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)


    