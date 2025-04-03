import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
from docker_chatter import main

class TestDockerChatter(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["Hello, AI!", "exit"])
    @patch('docker_chatter.process_openai')
    def test_main_valid_input(self, mock_process_openai, mock_input):
        # Mock the process_openai function to return a fake response
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(role="assistant", content="Mocked AI response"))
        ]
        mock_process_openai.return_value = mock_response

        # Run the main function
        main()

        # Check if process_openai was called with the correct arguments
        mock_process_openai.assert_called_once_with("Hello, AI!", [])

        # Check if the output contains the mocked response
        output = self.held_output.getvalue()
        self.assertIn("ChatterAI: Mocked AI response", output)

    @patch('builtins.input', side_effect=["", "exit"])
    def test_main_empty_input(self, mock_input):
        # Run the main function
        main()

        # Check if the output contains the empty input warning
        output = self.held_output.getvalue()
        self.assertIn("Input cannot be empty. Please try again.", output)

    @patch('builtins.input', side_effect=["Hello, AI!", "exit"])
    @patch('docker_chatter.process_openai')
    def test_main_api_error(self, mock_process_openai, mock_input):
        # Mock the process_openai function to raise an exception
        mock_process_openai.side_effect = Exception("API error")

        # Run the main function
        main()

        # Check if the output contains the error message
        output = self.held_output.getvalue()
        self.assertIn("An error occurred: API error", output)

if __name__ == "__main__":
    unittest.main()