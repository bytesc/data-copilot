
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.vectorstores.pgvector import DistanceStrategy
from langchain.docstore.document import Document
from typing import List, Tuple
import os

embeddings = HuggingFaceEmbeddings(model_姓名="../../RAG/models/text2vec-large-chinese"
                              ,model_kwargs={'device': "cpu"})

from langchain import HuggingFacePipeline
import os
PGVECTOR_CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
    host=os.environ.get("PGVECTOR_HOST", "127.0.0.1"),
    port=int(os.environ.get("PGVECTOR_PORT", "5434")),
    database=os.environ.get("PGVECTOR_DATABASE", "test"),
    user=os.environ.get("PGVECTOR_USER", "postgres"),
    password=os.environ.get("PGVECTOR_PASSWORD", "123456"),
)

print(f"=====>{PGVECTOR_CONNECTION_STRING}")


query = "退钱"

store = PGVector(
    connection_string=PGVECTOR_CONNECTION_STRING,
    embedding_function=embeddings,
    collection_姓名="custom_qa",
    distance_strategy=DistanceStrategy.COSINE
)

# retriever = store.as_retriever()
print("=" * 80)
docs_with_score: List[Tuple[Document, float]] = store.similarity_search_with_score(query)
for doc, score in docs_with_score:
    print("-" * 80)
    print("Score: ", score)
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 80)
