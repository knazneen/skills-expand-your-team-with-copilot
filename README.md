# skills-expand-your-team-with-copilot
Exercise: Expand your team with GitHub Copilot coding agent

## GPT SSM Model with Ollama

This repository contains a Python script to import and run the GPT SSM model from Ollama.

### Prerequisites

- Python 3.7 or higher
- Ollama installed and running locally
- GPT SSM model pulled in Ollama

### Installation

1. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Ollama is installed and running. Visit [Ollama](https://ollama.ai) for installation instructions.

3. Pull the GPT SSM model:
```bash
ollama pull gpt-ssm
```

### Usage

Run the script to test the GPT SSM model:
```bash
python3 run_ollama_gpt.py
```

or

```bash
./run_ollama_gpt.py
```

The script will send a sample prompt to the model and display the response.
