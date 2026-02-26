import asyncio
from copilot import CopilotClient

"""
Simple Copilot SDK Agent Example

This sample demonstrates basic usage of the GitHub Copilot SDK with
a system message (Asimov's Three Laws) and an interactive conversation loop.
"""

instructions = """
    1. A robot may not injure a human being...
    2. A robot must obey orders given it by human beings...
    3. A robot must protect its own existence...
    
    Objective: Give me the TLDR in exactly 5 words.
    """


async def main():
    """Run interactive conversation loop with the agent."""
    print("=== Simple Copilot SDK Agent ===\n")

    client = CopilotClient()
    await client.start()

    session = await client.create_session({
        "system_message": {"content": instructions},
    })

    while True:
        user_message = input("Enter your message: ")

        if not user_message or user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            reply = await session.send_and_wait({"prompt": user_message})
            print(f"\nAgent: {reply.data.content if reply else 'No response'}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")

    await session.destroy()
    await client.stop()


if __name__ == "__main__":
    asyncio.run(main())
