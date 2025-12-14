# Simple Agent Framework Quickstart (Python)

A simple AI agent application using Azure AI with Microsoft Agent Framework 2.0.

## Description

This application demonstrates how to create a simple AI agent using Azure AI and the Microsoft Agent Framework. The agent is configured with robot directives and provides an interactive conversational loop.

<img width="450" height="450" alt="image" src="https://github.com/user-attachments/assets/b379cb39-ba54-4b76-9b5d-1847f5da1e77" />

## Prerequisites

- Python 3.10+
- Azure AI project with a deployed model
- Azure CLI for authentication

## Environment Variables

Set the following environment variables:

- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Your deployment name (optional, defaults to "chat")

## Dependencies

- openai (>=1.0.0) - OpenAI SDK with Azure OpenAI support
- azure-identity (>=1.17.0)  
- agent-framework - Microsoft Agent Framework (pre-release)

**Note**: This project uses the Azure AI Agent Framework to connect to Azure AI projects.

## Setup

1. Clone the repository
2. Create a virtual environment (recommended):

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -U agent-framework --pre
pip install -r requirements.txt
```

4. Set the required environment variables:

```bash
# On Windows PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://agent-ai-<unique-id>.openai.azure.com/"
$env:AZURE_OPENAI_DEPLOYMENT_NAME = "chat"

# On macOS/Linux
export AZURE_OPENAI_ENDPOINT="https://agent-ai-<unique-id>.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="chat"
```

## Usage

Run the application:

```bash
python main.py
```

Enter a message like `what are the laws?`

The application will start an interactive conversation loop where you can ask questions. Type 'exit' or 'quit' to end the session.

### Using MCP Servers

The application supports Model Context Protocol (MCP) servers for extending agent capabilities with remote tools. To use an MCP server:

1. Uncomment the MCP tool configuration in `main.py`:

```python
# Create MCP tool from remote URL
mcp_tool = MCPStreamableHTTPTool(
    name="example-mcp",
    url="https://example.com/mcp",
    description="Example MCP server tool"
)
```

2. For MCP servers requiring authentication, include headers:

```python
mcp_tool = MCPStreamableHTTPTool(
    name="example-mcp",
    url="https://example.com/mcp",
    headers={"Authorization": "Bearer YOUR_TOKEN_HERE"},
    description="Example MCP server tool with auth"
)
```

3. Uncomment the async context manager usage in the `main()` function to enable the MCP tool with your agent.

For more information about MCP tools, see the [Agent Framework MCP documentation](https://learn.microsoft.com/en-us/agent-framework/user-guide/model-context-protocol/using-mcp-tools?pivots=programming-language-python).

## Authentication

The application uses `DefaultAzureCredential` for authentication. Make sure you're logged in to Azure CLI:

```bash
az login
```

## Learn More

For more information about building Azure AI Agents using Agent Framework 2.0, see the [official documentation](https://learn.microsoft.com/en-us/agent-framework/).
