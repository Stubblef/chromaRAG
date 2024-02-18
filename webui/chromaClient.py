import os
import chromadb
from typing import Union, List


class ChromaClient:
    save_path="./data/persist"
    
    def __init__(self, save_path="./data/persist"):
        os.makedirs(self.save_path, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=save_path)


    def rm_tmp(self):
        list_collection = self.chroma_client.list_collections()
        for collection in list_collection:
            print("Deleting collection: ", collection)
            self.chroma_client.delete_collection(collection.name)  # Delete the collection
        print("All collections deleted")

    def create_collection(self, name, rm_tmp=False):
        if rm_tmp:
            self.rm_tmp()
        print("Creating collection with name: ", name)
        return self.chroma_client.create_collection(name)
    
    def add_doc(self, collection: str, document: Union[str, List], split_length:int = 512, metadatas: List[dict] = None, ids: List[str] = None):
        """
        Param:
        document: str or List: ["This is a document", "This is another document"]
        metadata: dict: [{"source": "my_source"}, {"source": "my_source"}]
        ids: List[str]: ["id1", "id2"]
        """
        if isinstance(document, str):
            document = [document]
        if metadatas is None:
            metadatas = [0 for _ in range(len(document))]
        if ids is None:
            ids = [None for _ in range(len(document))]
        collection_insert = self.chroma_client.get_collection(collection)
        print(document, metadatas, ids)
        return collection_insert.add(document, metadatas, ids)


