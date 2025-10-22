#!/usr/bin/env python3
"""
Script to import and run GPT SSM model from Ollama
"""

import ollama


def main():
    """
    Main function to run the GPT SSM model using Ollama
    """
    # Initialize the model name
    model_name = "gpt-ssm"
    
    # Sample prompt to test the model
    prompt = "Hello! Can you introduce yourself?"
    
    print(f"Running model: {model_name}")
    print(f"Prompt: {prompt}")
    print("-" * 50)
    
    try:
        # Generate response using the Ollama client
        response = ollama.generate(
            model=model_name,
            prompt=prompt
        )
        
        # Print the response
        print(f"Response: {response['response']}")
        
    except Exception as e:
        print(f"Error running model: {e}")
        print("\nNote: Make sure Ollama is installed and the model is available.")
        print(f"You can pull the model using: ollama pull {model_name}")


if __name__ == "__main__":
    main()
