from qdrant_client import QdrantClient

qdrant_client = QdrantClient(url="http://localhost:6333")

def create_collection(collection_name: str, vector_size: int):
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config={"size": vector_size, "distance": "Cosine"}
    )

def store_chunks_in_qdrant(collection_name: str, document_id: str, chunks: list, embeddings: list, metadata: dict):
    points = [
        {
            "id": f"{document_id}_chunk_{i}",
            "vector": embeddings[i],
            "payload": {
                "chunk_text": chunks[i],
                "metadata": metadata
            }
        }
        for i in range(len(chunks))
    ]
    qdrant_client.upsert(collection_name=collection_name, points=points)
