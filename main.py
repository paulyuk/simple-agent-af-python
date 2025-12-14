import asyncio
import os
from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get configuration for agent
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "chat")

if not endpoint:
    raise ValueError("AZURE_OPENAI_ENDPOINT is not set. Please set this environment variable.")

instructions = """
    1. A robot may not injure a human being...
    2. A robot must obey orders given it by human beings...
    3. A robot must protect its own existence...
    
    Objective: Give me the TLDR in exactly 5 words.
    """

# Get Azure token for authentication
# DefaultAzureCredential will check: Environment Vars -> Azure CLI -> Managed Identity
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, 
    "https://cognitiveservices.azure.com/.default"
)

# Create Azure OpenAI client
chat_client = AzureOpenAIChatClient(
    endpoint=endpoint,
    deployment_name=deployment_name,
    api_version="2024-08-01-preview",
    ad_token_provider=token_provider
)

# Optional: Create MCP tool from remote URL
# Example 1 - Microsoft Learn MCP server:
# mcp_tool = MCPStreamableHTTPTool(
#     name="learn-mcp",
#     url="https://learn.microsoft.com/mcp",
#     description="Microsoft Learn MCP server"
# )

# Example 2 - GitHub MCP server with OAuth:
# mcp_tool = MCPStreamableHTTPTool(
#     name="github-mcp",
#     url="https://api.github.com/mcp",
#     headers={"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"},
#     description="GitHub MCP server"
# )

# Stay in a loop for continuous conversation
async def main():
    """Run interactive conversation loop with the agent."""
    
    # Optional: Use MCP tool in async context manager
    # Uncomment to use MCP tools with the agent:
    # async with mcp_tool:
    
    # Create the agent
    agent = ChatAgent(
        chat_client=chat_client,
        instructions=instructions
        # Uncomment to add MCP tools:
        # , tools=mcp_tool
    )
    
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
