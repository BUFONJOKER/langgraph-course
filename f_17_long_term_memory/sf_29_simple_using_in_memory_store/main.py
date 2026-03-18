from langgraph.store.memory import InMemoryStore
from langchain_ollama import OllamaEmbeddings

# 1. Initialize the local model
embeddings = OllamaEmbeddings(model="qwen3-embedding:0.6b")

# 2. Configure the store (Ensure dims matches your model output)
# Qwen3-0.6b is usually 1024, but check your output if 1536 fails
store = InMemoryStore(index={
    "dims": 1024,
    "embed": embeddings,
    "fields": ["memory"]
})

name_space = ('user', 'u1')

# 3. Store the memories
# Using a list of tuples to be cleaner
memories = [
    ("1", {"memory": "user is a student."}),
    ("2", {"memory": "user likes cricket."}),
    ("3", {"memory": "user loves korean crime shows on netflix."}),
    ("4", {"memory": "user is learning langchain."}),
    ("5", {"memory": "user is learning langgraph."}),
    ("6", {"memory": "user has no friends."}),
    ("7", {"memory": "user loves his mom."})
]

for key, val in memories:
    store.put(name_space, key, val)

# 4. Search
query = input("Write your query (e.g., 'What shows does the user watch?'): ")

# Searching with a limit of 1 to get the best match
items = store.search(name_space, query=query, limit=1)

print("\n--- Semantic Search Results ---")
if items:
    for item in items:
        print(f"Result found: {item.value['memory']}")
        print(f"Similarity Score: {item.score:.4f}")
else:
    print("No relevant memories found.")

# print(store.get(name_space,'1'))

# print(store.search(name_space))

# items = store.search(name_space)

# for item in items:
#     print(item.value)

# result = embeddings.embed_query("What is my memory?")