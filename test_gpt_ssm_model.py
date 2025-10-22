#!/usr/bin/env python3
"""
Test script for GPT SSM Model

This script tests the functionality of the GPT SSM Model implementation
without requiring Ollama to be installed (for CI/CD purposes).
"""

import sys
import unittest
from unittest.mock import patch, MagicMock
from gpt_ssm_model import GPTSSMModel


class TestGPTSSMModel(unittest.TestCase):
    """Test cases for GPTSSMModel class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.model = GPTSSMModel(model_name="llama2")
    
    def test_initialization(self):
        """Test model initialization"""
        self.assertEqual(self.model.model_name, "llama2")
        self.assertFalse(self.model.is_initialized)
    
    def test_custom_model_name(self):
        """Test initialization with custom model name"""
        custom_model = GPTSSMModel(model_name="mistral")
        self.assertEqual(custom_model.model_name, "mistral")
    
    @patch('subprocess.run')
    def test_check_ollama_installed_success(self, mock_run):
        """Test Ollama installation check when installed"""
        mock_run.return_value = MagicMock(returncode=0)
        result = self.model.check_ollama_installed()
        self.assertTrue(result)
        mock_run.assert_called_once()
    
    @patch('subprocess.run')
    def test_check_ollama_installed_failure(self, mock_run):
        """Test Ollama installation check when not installed"""
        mock_run.side_effect = FileNotFoundError()
        result = self.model.check_ollama_installed()
        self.assertFalse(result)
    
    @patch('subprocess.run')
    def test_pull_model_success(self, mock_run):
        """Test successful model pulling"""
        mock_run.return_value = MagicMock(returncode=0)
        result = self.model.pull_model()
        self.assertTrue(result)
    
    @patch('subprocess.run')
    def test_pull_model_failure(self, mock_run):
        """Test failed model pulling"""
        mock_run.return_value = MagicMock(returncode=1, stderr="Error message")
        result = self.model.pull_model()
        self.assertFalse(result)
    
    @patch('subprocess.run')
    def test_initialize_success(self, mock_run):
        """Test successful initialization"""
        mock_run.return_value = MagicMock(returncode=0)
        result = self.model.initialize()
        self.assertTrue(result)
        self.assertTrue(self.model.is_initialized)
    
    @patch('subprocess.run')
    def test_initialize_no_ollama(self, mock_run):
        """Test initialization when Ollama is not installed"""
        mock_run.side_effect = FileNotFoundError()
        result = self.model.initialize()
        self.assertFalse(result)
        self.assertFalse(self.model.is_initialized)
    
    @patch('subprocess.run')
    def test_run_without_initialization(self, mock_run):
        """Test running model without initialization"""
        result = self.model.run("Test prompt")
        self.assertIsNone(result)
    
    @patch('subprocess.run')
    def test_run_with_initialization(self, mock_run):
        """Test running model after initialization"""
        # Mock initialization
        mock_run.return_value = MagicMock(returncode=0, stdout="Test response", stderr="")
        self.model.is_initialized = True
        
        # Test run
        result = self.model.run("Test prompt")
        self.assertIsNotNone(result)
        self.assertEqual(result, "Test response")
    
    @patch('subprocess.run')
    def test_list_available_models(self, mock_run):
        """Test listing available models"""
        mock_output = "NAME\nllama2\nmistral\n"
        mock_run.return_value = MagicMock(returncode=0, stdout=mock_output)
        
        models = self.model.list_available_models()
        self.assertIsInstance(models, list)
        self.assertEqual(len(models), 2)
        self.assertIn("llama2", models)
        self.assertIn("mistral", models)
    
    @patch('subprocess.run')
    def test_list_available_models_failure(self, mock_run):
        """Test listing models when command fails"""
        mock_run.return_value = MagicMock(returncode=1)
        models = self.model.list_available_models()
        self.assertEqual(models, [])


def run_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running GPT SSM Model Tests")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGPTSSMModel)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
