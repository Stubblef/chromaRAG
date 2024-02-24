# import chromadb

# chroma_client = chromadb.Client()  # Create a new client
# collection = chroma_client.create_collection(name="test_collection")  # Create a new collection

# # Make sure the embeddings have the correct dimension (in this case, 3)
# embeddings = [[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]]

# collection.add(
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

# results = collection.query(
#     query_texts=["This is a document"],
#     n_results=2
# )

# print(results)


# python -m demo.dbinsert 

import chromadb
from db_server.chromaClient import ChromaClient


# 读取篇pvdocs.txt
with open('data/pvdocs.txt', 'r',encoding="utf-8") as f:
    vdocs = f.readlines()  # 读取全部内容
    # vdocs = [x.strip() for x in vdocs]  # 去掉每行头尾空白
    print(vdocs)

# client = chromadb.PersistentClient("d:/JHQ/chromaRAG/data/persist")
client = ChromaClient()
client.create_collection(name="test",rm_tmp=True)

client.add_doc(collection="test",document=vdocs)   # split_length=512

