from fastapi import FastAPI, Query
from vector import retriever

app = FastAPI()

@app.get("/ask")
def ask_question(question: str = Query(..., description="Your question")):
    docs = retriever.invoke(question)
    reviews = [
        {
            "content": d.page_content,
            "rating": d.metadata.get("rating"),
            "date": d.metadata.get("date"),
            "city": d.metadata.get("city"),
            "restaurant": d.metadata.get("restaurant"),
        }
        for d in docs
    ]
    return {"reviews": reviews}