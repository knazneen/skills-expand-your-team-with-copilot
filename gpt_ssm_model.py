#!/usr/bin/env python3
"""
GPT SSM Model using Ollama

This module implements a GPT State Space Model (SSM) using Ollama.
The model can be initialized, configured, and run for inference.
"""

import json
import subprocess
import sys
from typing import Optional, Dict, Any, List


class GPTSSMModel:
    """
    A GPT State Space Model wrapper using Ollama.
    
    This class provides an interface to create and run GPT-based SSM models
    using the Ollama framework.
    """
    
    def __init__(self, model_name: str = "llama2"):
        """
        Initialize the GPT SSM Model.
        
        Args:
            model_name: The name of the Ollama model to use (default: llama2)
        """
        self.model_name = model_name
        self.is_initialized = False
        
    def check_ollama_installed(self) -> bool:
        """
        Check if Ollama is installed on the system.
        
        Returns:
            True if Ollama is installed, False otherwise
        """
        try:
            result = subprocess.run(
                ["ollama", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def pull_model(self) -> bool:
        """
        Pull the model from Ollama if not already available.
        
        Returns:
            True if model is available, False otherwise
        """
        try:
            print(f"Pulling model '{self.model_name}' from Ollama...")
            result = subprocess.run(
                ["ollama", "pull", self.model_name],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"Model '{self.model_name}' pulled successfully!")
                return True
            else:
                print(f"Error pulling model: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            print("Timeout while pulling model")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def initialize(self) -> bool:
        """
        Initialize the model by checking dependencies and pulling the model.
        
        Returns:
            True if initialization successful, False otherwise
        """
        if not self.check_ollama_installed():
            print("Error: Ollama is not installed. Please install Ollama first.")
            print("Visit https://ollama.ai for installation instructions.")
            return False
        
        print("Ollama is installed ✓")
        
        if not self.pull_model():
            return False
        
        self.is_initialized = True
        print("GPT SSM Model initialized successfully!")
        return True
    
    def run(self, prompt: str, **kwargs) -> Optional[str]:
        """
        Run the model with the given prompt.
        
        Args:
            prompt: The input prompt for the model
            **kwargs: Additional parameters for the model
                - temperature: Controls randomness (0.0-1.0)
                - max_tokens: Maximum number of tokens to generate
                - top_p: Nucleus sampling parameter
        
        Returns:
            The model's response, or None if an error occurred
        """
        if not self.is_initialized:
            print("Model not initialized. Call initialize() first.")
            return None
        
        try:
            print(f"\nRunning model with prompt: '{prompt}'\n")
            
            # Prepare the command
            cmd = ["ollama", "run", self.model_name, prompt]
            
            # Run the model
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                response = result.stdout.strip()
                print(f"Response:\n{response}\n")
                return response
            else:
                print(f"Error running model: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("Timeout while running model")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def run_stream(self, prompt: str) -> None:
        """
        Run the model with streaming output.
        
        Args:
            prompt: The input prompt for the model
        """
        if not self.is_initialized:
            print("Model not initialized. Call initialize() first.")
            return
        
        try:
            print(f"\nRunning model with prompt (streaming): '{prompt}'\n")
            print("Response:")
            
            # Run with streaming output
            process = subprocess.Popen(
                ["ollama", "run", self.model_name, prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Stream the output
            for line in process.stdout:
                print(line, end='')
            
            process.wait()
            print("\n")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def list_available_models(self) -> List[str]:
        """
        List all available Ollama models on the system.
        
        Returns:
            List of available model names
        """
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Parse the output
                lines = result.stdout.strip().split('\n')[1:]  # Skip header
                models = [line.split()[0] for line in lines if line.strip()]
                return models
            else:
                return []
        except Exception as e:
            print(f"Error listing models: {e}")
            return []


def main():
    """
    Main function to demonstrate the GPT SSM Model.
    """
    print("=" * 60)
    print("GPT SSM Model with Ollama")
    print("=" * 60)
    
    # Create the model
    model = GPTSSMModel(model_name="llama2")
    
    # Initialize the model
    if not model.initialize():
        print("Failed to initialize model. Exiting.")
        sys.exit(1)
    
    # List available models
    print("\nAvailable models:")
    available_models = model.list_available_models()
    for m in available_models:
        print(f"  - {m}")
    
    # Run some example prompts
    print("\n" + "=" * 60)
    print("Running Example Prompts")
    print("=" * 60)
    
    examples = [
        "What is a State Space Model in the context of machine learning?",
        "Explain the difference between GPT and SSM models.",
        "Write a simple Python function to add two numbers."
    ]
    
    for i, prompt in enumerate(examples, 1):
        print(f"\n--- Example {i} ---")
        response = model.run(prompt)
        if response:
            print(f"Success! Generated {len(response)} characters.")
        print("-" * 60)
    
    print("\n" + "=" * 60)
    print("GPT SSM Model Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
