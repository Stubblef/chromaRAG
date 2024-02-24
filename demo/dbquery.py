# python -m demo.dbquery
import chromadb

client = chromadb.PersistentClient("d:/JHQ/chromaRAG/data/persist")

collection = client.get_collection("test")
rescc = collection.query(query_texts="工程概况应包括什么",n_results=3)

print(rescc)
print(rescc.get("documents"))