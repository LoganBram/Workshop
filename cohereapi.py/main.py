import os
import cohere

# call to expiermental endpoint of cohere api
# goal to make call to language model

co = cohere.Client(os.environ.get("COHERE_API_KEY"))
query = None

query = input("Users: ")

response = co.chat(
    query=query,
    model="command a beta",
)

print(response.reply)

print(("Bot: "(response.reply)))
