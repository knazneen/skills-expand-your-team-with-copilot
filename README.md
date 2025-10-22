# skills-expand-your-team-with-copilot
Exercise: Expand your team with GitHub Copilot coding agent

## GPT SSM Model with Ollama

This project implements a GPT State Space Model (SSM) using Ollama, providing an interface to create and run language models for various tasks.

### Features

- **Easy Model Initialization**: Automatically pull and initialize models from Ollama
- **Multiple Inference Modes**: Support for both standard and streaming output
- **Model Management**: List and switch between available models
- **Simple API**: Clean Python interface for model interactions

### Prerequisites

1. **Python 3.7+**: Ensure Python is installed on your system
2. **Ollama**: Install Ollama from [https://ollama.ai](https://ollama.ai)

   For Linux/Mac:
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

   For Windows, download from the Ollama website.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/knazneen/skills-expand-your-team-with-copilot.git
   cd skills-expand-your-team-with-copilot
   ```

2. Install Python dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running the Demo

Execute the main script to see the GPT SSM model in action:

```bash
python gpt_ssm_model.py
```

This will:
1. Check if Ollama is installed
2. Pull the default model (llama2)
3. Run example prompts
4. Display responses

#### Using as a Library

You can also use the `GPTSSMModel` class in your own scripts:

```python
from gpt_ssm_model import GPTSSMModel

# Create a model instance
model = GPTSSMModel(model_name="llama2")

# Initialize the model
if model.initialize():
    # Run a prompt
    response = model.run("What is a State Space Model?")
    print(response)
    
    # Or use streaming output
    model.run_stream("Explain machine learning in simple terms.")
```

#### Available Methods

- `check_ollama_installed()`: Verify Ollama installation
- `pull_model()`: Download the model from Ollama
- `initialize()`: Initialize the model (checks installation and pulls model)
- `run(prompt, **kwargs)`: Run model with a prompt and return the response
- `run_stream(prompt)`: Run model with streaming output
- `list_available_models()`: List all locally available models

### Customization

You can use different Ollama models by specifying the model name:

```python
# Use a different model
model = GPTSSMModel(model_name="mistral")
model.initialize()
```

Popular models include:
- `llama2` - Meta's Llama 2 model
- `mistral` - Mistral AI's model
- `codellama` - Code-specialized Llama model
- `phi` - Microsoft's Phi model

### Example Output

```
============================================================
GPT SSM Model with Ollama
============================================================
Ollama is installed ✓
Pulling model 'llama2' from Ollama...
Model 'llama2' pulled successfully!
GPT SSM Model initialized successfully!

Available models:
  - llama2

============================================================
Running Example Prompts
============================================================

--- Example 1 ---
Running model with prompt: 'What is a State Space Model in the context of machine learning?'

Response:
[Model response will appear here]

Success! Generated XXX characters.
------------------------------------------------------------
```

### Troubleshooting

**Issue**: "Ollama is not installed"
- **Solution**: Install Ollama from https://ollama.ai

**Issue**: Model pull timeout
- **Solution**: Check your internet connection and try again

**Issue**: Model not found
- **Solution**: Ensure you're using a valid model name from Ollama's model library

### Contributing

This is an educational project. Feel free to fork and experiment with different models and features!

### License

This project is part of a GitHub Skills exercise.
