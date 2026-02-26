# Simple Agent QuickStart (Python Copilot SDK)

A simple AI agent using Microsoft Foundry (Azure AI) with the Microsoft Agent Framework.

## Prerequisites

- [Python 3.11+](https://docs.astral.sh/uv/getting-started/installation/)
- [Azure Developer CLI (azd)](https://aka.ms/azd-install)
- [Azure CLI](https://aka.ms/install-azure-cli)
- Access to an AI model via one of:
  - **GitHub Copilot subscription** — models are available automatically
  - **Bring Your Own Key (BYOK)** — use an API key from [Microsoft Foundry](https://ai.azure.com) (see [BYOK docs](https://github.com/github/copilot-sdk/blob/main/docs/auth/byok.md))

## Deploy Azure AI Resources (if needed)

If you're using BYOK and don't already have a Microsoft Foundry AI project with a model deployed, use one of these options:

### Option 1: Azure Developer CLI (Recommended)

Provisions all Azure resources and configures local development automatically:

```bash
azd auth login
azd up
```

### Option 2: One-Click Deploy

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpaulyuk%2Fsimple-agent-af%2Fmain%2Finfra%2Fdeploybutton%2Fazuredeploy.json)

> **Important:** Fill in the **Principal ID** field with your user object ID from the [Entra blade](https://ms.portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) and give the environment a memorable name.

### What Gets Deployed

- Microsoft Foundry AI Project with GPT-5-mini model
- Azure Functions app (Python, Flex Consumption plan)
- Storage, monitoring, and all necessary RBAC role assignments
- Optional: Azure AI Search for vector store (disabled by default)
- Optional: Cosmos DB for agent thread storage (disabled by default)

## Quickstart

1. Clone the repository

2. Install dependencies using [uv](https://docs.astral.sh/uv/):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   uv pip install -r requirements.txt
   ```

3. Configure environment variables (created automatically by `azd up`, or set manually):

   ```bash
   export AZURE_AI_PROJECT_ENDPOINT="https://<your-ai-services>.services.ai.azure.com/api/projects/<your-project>"
   export AZURE_AI_MODEL_DEPLOYMENT_NAME="chat"
   ```

   Or copy `.env.example` to `.env` and fill in values. Find your project endpoint at [ai.azure.com](https://ai.azure.com).

4. Log in to Azure for authentication:

   ```bash
   az login
   ```

5. Run the agent:

   ```bash
   uv run main.py
   ```

   Enter a message like `what are the laws?` — type `exit` or `quit` to end the session.

## Source Code

The agent logic is in [`main.py`](main.py). It creates a `CopilotClient`, configures a session with a system message (Asimov's Three Laws of Robotics), and runs an interactive conversation loop where user input is sent to the agent and responses are printed.

## Learn More

- [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
- [Copilot SDK Python docs](https://github.com/github/copilot-sdk/tree/main/python)
- [BYOK (Bring Your Own Key)](https://github.com/github/copilot-sdk/blob/main/docs/auth/byok.md)
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
