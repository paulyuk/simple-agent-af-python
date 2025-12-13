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
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Your deployment name (optional, defaults to "gpt-4.1-mini")

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
$env:AZURE_OPENAI_ENDPOINT = "https://agent-ai-servicesai7wu23avdwjg.openai.azure.com/"
$env:AZURE_OPENAI_DEPLOYMENT_NAME = "gpt-4.1-mini"

# On macOS/Linux
export AZURE_OPENAI_ENDPOINT="https://agent-ai-servicesai7wu23avdwjg.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4.1-mini"
```

## Usage

Run the application:

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
