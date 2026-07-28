from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":

    docs = load_all_documents("data")

    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()

    rag_search = RAGSearch()

    print("===== College RAG Assistant =====")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        summary = rag_search.search_and_summarize(query, top_k=3)

        print("\nAnswer:")
        print(summary)
        print("-" * 60)