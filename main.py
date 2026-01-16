import asyncio
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity.aio import DefaultAzureCredential

"""
Simple Azure AI Agent Example

This sample demonstrates basic usage of AzureAIProjectAgentProvider with automatic
lifecycle management and an interactive conversation loop.
"""

instructions = """
    1. A robot may not injure a human being...
    2. A robot must obey orders given it by human beings...
    3. A robot must protect its own existence...
    
    Objective: Give me the TLDR in exactly 5 words.
    """


async def main():
    """Run interactive conversation loop with the agent."""
    print("=== Simple Azure AI Agent ===\n")
    
    # For authentication, DefaultAzureCredential checks: Environment Vars -> Azure CLI -> Managed Identity
    async with (
        DefaultAzureCredential() as credential,
        AzureAIProjectAgentProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="RobotAgent",
            instructions=instructions,
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
                print(f"\nAgent: {result}\n")
            except Exception as ex:
                print(f"Error: {ex}\n")


if __name__ == "__main__":
    asyncio.run(main())
