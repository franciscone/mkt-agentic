from langchain_community.llms import HuggingFaceEndpoint
from langgraph.prebuilt import create_react_agent
import os

# Certifique-se de que sua variável de ambiente está definida
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3-8b-chat-hf",  # ou outro modelo disponível
    task="text-generation",  # ou "text2text-generation" dependendo do modelo
    temperature=0.7,
    max_new_tokens=512
)


def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model=llm, 
    tools=[], 
    prompt="Você é um assistente inteligente e detalhado."
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
