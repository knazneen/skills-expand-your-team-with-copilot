#!/usr/bin/env python3
"""
Simple example of using the GPT SSM Model

This script demonstrates basic usage of the GPT SSM Model
with custom prompts.
"""

from gpt_ssm_model import GPTSSMModel
import sys


def main():
    print("GPT SSM Model - Simple Example")
    print("-" * 60)
    
    # Create model instance
    print("Creating model instance...")
    model = GPTSSMModel(model_name="llama2")
    
    # Initialize (this will pull the model if needed)
    print("\nInitializing model...")
    if not model.initialize():
        print("Failed to initialize model.")
        print("Make sure Ollama is installed: https://ollama.ai")
        sys.exit(1)
    
    # Example 1: Simple question
    print("\n" + "=" * 60)
    print("Example 1: Simple Question")
    print("=" * 60)
    response = model.run("What is 2 + 2?")
    
    # Example 2: Explaining a concept
    print("\n" + "=" * 60)
    print("Example 2: Concept Explanation")
    print("=" * 60)
    response = model.run("Explain what a state space model is in one sentence.")
    
    # Example 3: Code generation
    print("\n" + "=" * 60)
    print("Example 3: Code Generation")
    print("=" * 60)
    response = model.run("Write a Python function to calculate factorial.")
    
    print("\n" + "=" * 60)
    print("Examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
