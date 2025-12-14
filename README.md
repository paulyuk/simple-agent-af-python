# Simple Agent Framework Quickstart (Python)

A simple AI agent application using Azure AI with Microsoft Agent Framework 2.0.

## Description

This application demonstrates how to create a simple AI agent using Azure AI and the Microsoft Agent Framework. The agent is configured with robot directives and provides an interactive conversational loop.

<img width="450" height="450" alt="image" src="https://github.com/user-attachments/assets/b379cb39-ba54-4b76-9b5d-1847f5da1e77" />

## Deploy to Azure

### Quick Start Options

1. **One-Click Deploy**: [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpaulyuk%2Fsimple-agent-af-python%2Fmain%2Finfra%2Fdeploybutton%2Fazuredeploy.json)
   
2. **Azure Developer CLI** (Recommended):
   ```bash
   azd auth login
   azd up
   ```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### What Gets Deployed

- Azure Functions app with Python 3.11 runtime (Flex Consumption plan)
- Azure AI services with GPT-4.1-mini model
- Storage, monitoring, and all necessary role assignments
- Optional: Azure AI Search (for vector store capabilities, disabled by default)
- Optional: Cosmos DB (for agent thread storage, disabled by default)

## Prerequisites

### For Azure Deployment
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- Azure subscription

### For Local Development
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

## Local Development Usage

After deploying to Azure or setting up your own Azure OpenAI resources:

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

4. Set the required environment variables (or use `azd env get-values` after deployment):

```bash
# On Windows PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://agent-ai-<unique-id>.openai.azure.com/"
$env:AZURE_OPENAI_DEPLOYMENT_NAME = "chat"

# On macOS/Linux
export AZURE_OPENAI_ENDPOINT="https://agent-ai-<unique-id>.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="chat"
```

5. Run the application:

```bash
python main.py
```

6. Enter a message like `what are the laws?`

The application will start an interactive conversation loop where you can ask questions. Type 'exit' or 'quit' to end the session.

## Authentication

The application uses `DefaultAzureCredential` for authentication. Make sure you're logged in to Azure CLI:

```bash
az login
```

## Learn More

For more information about building Azure AI Agents using Agent Framework 2.0, see the [official documentation](https://learn.microsoft.com/en-us/agent-framework/).
