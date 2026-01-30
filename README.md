# Simple Agent Framework Quickstart (Python)

A simple AI agent application using Microsoft Foundry (Azure AI) with Microsoft Agent Framework 2.0.

## Description

This application demonstrates how to create a simple AI agent using Azure AI and the Microsoft Agent Framework. The agent is configured with robot directives and provides an interactive conversational loop.

<img width="450" height="450" alt="image" src="https://github.com/user-attachments/assets/b379cb39-ba54-4b76-9b5d-1847f5da1e77" />

## Prerequisites

- Python 3.10+
- Azure AI project with a deployed model
- Azure CLI for authentication

## Quickstart - Need Microsoft Foundry Resources?

### Deployment Options

1. **One-Click Deploy**: [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpaulyuk%2Fsimple-agent-af%2Fmain%2Finfra%2Fdeploybutton%2Fazuredeploy.json)

- **Important** fill in the **Principal ID** field with the guid you see under your username in the [Entra blade of the Azure Portal](https://ms.portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview).  This sets up RBAC permissions needed.  Also **give the environment a name you will remember** so you can find the AI Foundry resource in the named resource group later. 
   
2. **Azure Developer CLI** (Recommended for development):
   ```bash
   azd auth login
   azd up
   ```
   - Automatically configures your user access for local development

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### What Gets Deployed

- Microft Foundry AI Project resources with GPT-4.1-mini model
- Storage, monitoring, and all necessary role assignments
- Azure Functions app with Python 3.x to host your agent app (Flex Consumption plan)
- Optional: Azure AI Search (for vector store capabilities, disabled by default)
- Optional: Cosmos DB (for agent thread storage, disabled by default)

## Environment Variables

Set the following environment variables:

- `AZURE_AI_PROJECT_ENDPOINT`: Your Azure AI project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME`: Your model deployment name (optional, defaults to "chat")

## Dependencies

- openai (>=1.0.0) - OpenAI SDK with Azure OpenAI support
- azure-identity (>=1.17.0)  
- agent-framework (>=1.0.0b260114) - Microsoft Agent Framework (pre-release)

**Note**: This project uses the Azure AI Agent Framework to connect to Azure AI projects. Recommend using agent-framework version 1.0.0b260114 or newer.

## Setup

1. Clone the repository
2. Create a virtual environment and install dependencies:

### Recommended: Using uv (fast Python package manager)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

uv pip install -r requirements.txt
```

### Alternative: Using pip

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

3. Set the required environment variables:

```bash
# On Windows PowerShell
$env:AZURE_AI_PROJECT_ENDPOINT = "https://agent-ai-<unique-id>.services.ai.azure.com/api/projects/<project-name>"
$env:AZURE_AI_MODEL_DEPLOYMENT_NAME = "chat"

# On macOS/Linux
export AZURE_AI_PROJECT_ENDPOINT="https://agent-ai-<unique-id>.services.ai.azure.com/api/projects/<project-name>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="chat"
```

Or create a `.env` file in the project root with these values.

AZURE_AI_PROJECT_ENDPOINT (aka Microsoft Foundry Project Endpoint) and other important details will be in the portal: https://ai.azure.com.  If you have multiple AI projects make sure you select the one created for this lab (see quickstart above).  

## Usage

Run the application:

### Recommended: Using uv

```bash
uv run main.py
```

### Alternative: Using python

```bash
python main.py
```

Enter a message like `what are the laws?`

The application will start an interactive conversation loop where you can ask questions. Type 'exit' or 'quit' to end the session.

## Authentication

The application uses `DefaultAzureCredential` for authentication. Make sure you're logged in to Azure CLI:

```bash
az login
```

## Learn More

For more information about building Azure AI Agents using Agent Framework 2.0, see the [official documentation](https://learn.microsoft.com/en-us/agent-framework/).
