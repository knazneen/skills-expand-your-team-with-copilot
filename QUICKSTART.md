# Quick Start Guide

## Prerequisites
Install Ollama from https://ollama.ai

## Basic Usage

### 1. Run the demo
```bash
python gpt_ssm_model.py
```

### 2. Use in your own code
```python
from gpt_ssm_model import GPTSSMModel

# Initialize
model = GPTSSMModel(model_name="llama2")
model.initialize()

# Run inference
response = model.run("Your prompt here")
print(response)
```

### 3. Run tests
```bash
python test_gpt_ssm_model.py
```

### 4. Try the example
```bash
python example_usage.py
```

## Available Models
- llama2 (default)
- mistral
- codellama
- phi
- And more from https://ollama.ai/library

## Key Features
✓ Automatic model downloading
✓ Easy initialization
✓ Standard and streaming output
✓ Multiple model support
✓ Comprehensive error handling
