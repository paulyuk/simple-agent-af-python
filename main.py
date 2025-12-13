import asyncio
import os
from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# 1. Setup Entra ID Credential
# DefaultAzureCredential will check: Environment Vars -> Azure CLI -> Managed Identity
credential = DefaultAzureCredential()

# 2. Create a Token Provider
token_provider = get_bearer_token_provider(
    credential, 
    "https://cognitiveservices.azure.com/.default"
)

# 3. Configure the Client with the Token Provider
# Note: We NO LONGER pass an api_key. We pass azure_ad_token_provider instead.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4.1-mini")

if not endpoint:
    raise ValueError("AZURE_OPENAI_ENDPOINT is not set. Please set this environment variable.")

chat_client = AzureOpenAIChatClient(
    endpoint=endpoint,
    deployment_name=deployment_name,
    api_version="2024-08-01-preview",
    ad_token_provider=token_provider  # <--- Changed from azure_ad_token_provider
)

instructions = """
    1. A robot may not injure a human being...
    2. A robot must obey orders given it by human beings...
    3. A robot must protect its own existence...
    
    Objective: Give me the TLDR in exactly 5 words.
    """

# 4. Create the Agent
agent = ChatAgent(
    chat_client=chat_client,
    instructions=instructions
)

# Optional: Add MCP tool from remote URL
# agent.add_mcp_server("https://example.com/mcp-server")

# Optional: Add MCP tool with authentication
# import httpx
# headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}
# agent.add_mcp_server("https://example.com/mcp-server", headers=headers)

async def main():
    # Stay in a loop for continuous conversation
    while True:
        user_message = input("Enter your message: ")
        
        # Check for exit commands
        if not user_message or user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        try:
            # Invoke the agent and output the text result
            result = await agent.run(user_message)
            print(f"\n{result.text}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")

if __name__ == "__main__":
    asyncio.run(main())
