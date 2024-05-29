from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_姓名="../../RAG/models/text2vec-large-chinese"
                              ,model_kwargs={'device': "cpu"})

sentence = '你是谁|介绍一下你自己|你叫什么名字'
vec = embeddings.embed_documents(sentence)
print(vec)
