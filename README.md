# Simple Agent QuickStart (Python Copilot SDK)

A simple AI agent using Microsoft Foundry (Azure AI) with the Microsoft Agent Framework.

## Prerequisites

- [Python 3.11+](https://docs.astral.sh/uv/getting-started/installation/)
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools)
- [Azure Developer CLI (azd)](https://aka.ms/azd-install) (only needed for deploying Azure resources)
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

3. Run the function locally:

   ```bash
   func start
   ```

4. Test the agent (in a new terminal):

   ```bash
   # Interactive chat client
   uv run chat.py

   # Or use curl directly
   curl -X POST http://localhost:7071/api/ask -d "what are the laws"
   ```

   Set `AGENT_URL` to point to a deployed instance:

   ```bash
   AGENT_URL=https://<your-function-app>.azurewebsites.net uv run chat.py
   ```

## Source Code

The agent logic is in [`function_app.py`](function_app.py). It creates a `CopilotClient`, configures a session with a system message (Asimov's Three Laws of Robotics), and exposes an HTTP endpoint (`/api/ask`) that accepts a prompt and returns the agent's response.

[`chat.py`](chat.py) is a lightweight console client that POSTs messages to the function in a loop, giving you an interactive chat experience. It defaults to `http://localhost:7071` but can be pointed at a deployed instance via the `AGENT_URL` environment variable.

## Using Azure Foundry (BYOK)

By default the agent uses GitHub Copilot's models. To use your own model from Microsoft Foundry instead, set these environment variables:

```bash
export AZURE_OPENAI_ENDPOINT="https://<your-ai-services>.openai.azure.com/"
export AZURE_OPENAI_API_KEY="<your-api-key>"
export AZURE_OPENAI_MODEL="gpt-5-mini"  # optional, defaults to gpt-5-mini
```

**Getting these values:**
- If you ran `azd up`, the endpoint is already in your environment — run `azd env get-values | grep AZURE_OPENAI_ENDPOINT`
- For the API key, go to [Azure Portal](https://portal.azure.com) → your AI Services resource → **Keys and Endpoint** → select the **Azure OpenAI** tab
- Or find both in the [Azure AI Foundry portal](https://ai.azure.com) under your project settings

See the [BYOK docs](https://github.com/github/copilot-sdk/blob/main/docs/auth/byok.md) for details.

## Learn More

- [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
- [Copilot SDK Python docs](https://github.com/github/copilot-sdk/tree/main/python)
- [BYOK (Bring Your Own Key)](https://github.com/github/copilot-sdk/blob/main/docs/auth/byok.md)
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
