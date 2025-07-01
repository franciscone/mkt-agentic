import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from huggingface_hub import login

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv('HF_API_TOKEN')
login(token=HUGGINGFACEHUB_API_TOKEN)

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=10,
    do_sample=False,
    repetition_penalty=1.03
)

chat = ChatHuggingFace(llm=llm, verbose=True)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]

response = chat.invoke(messages)
print(response.content)