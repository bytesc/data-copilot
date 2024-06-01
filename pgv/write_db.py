from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.vectorstores.pgvector import DistanceStrategy
from langchain.docstore.document import Document
from typing import List, Tuple

# https://huggingface.co/GanymedeNil/text2vec-large-chinese
# https://hf-mirror.com/GanymedeNil/text2vec-large-chinese
# https://huggingface.co/shibing624/text2vec-base-multilingual
# https://hf-mirror.com/shibing624/text2vec-base-multilingual
embeddings = HuggingFaceEmbeddings(model_name="../../RAG/models/text2vec-base-multilingual"
                                   , model_kwargs={'device': "cpu"})

# sentence = '你是谁|介绍一下你自己|你叫什么名字'
# vec = embeddings.embed_documents(sentence)
# print(vec)


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

data = [
    "你是谁|介绍一下你自己|你叫什么名字?",
    "商品支持退货吗？",
    "购物车可以添加多少商品?"
]

metadatas = [{
                 "answer": "是智能助手, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。让我们一步步思考，并且尽可能用分点叙述的形式输出。我们开始聊天吧"},
             {"answer": "15天内商品支持退换货"},
             {"answer": "购物车可以添加100件商品"}
             ]

PGVector.from_texts(texts=data,
                    embedding=embeddings,
                    collection_name="custom_qa",
                    connection_string=PGVECTOR_CONNECTION_STRING,
                    metadatas=metadatas
                    )
