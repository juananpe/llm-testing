import sqlite_utils
import llm
import json

db = sqlite_utils.Database("my-embeddings.db")
collection = llm.Collection("srt", db, model_id="ada-002")

if(collection.count()==0):

    with open("test_chunks.json", "r") as file:
    # Parse the JSON file content into a Python list
        lines_in_file = json.load(file)
        
        collection.embed_multi(
            (
                (i, line)
                for i, line in enumerate(lines_in_file)
            ),
            batch_size=10,
            store=True,
        )

print(collection.count())

for entry in collection.similar("qué es el shock del futuro"):
    print(entry.id, entry.score, entry.content)