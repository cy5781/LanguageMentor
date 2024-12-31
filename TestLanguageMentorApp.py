import unittest
from unittest.mock import patch
import gradio as gr
from main import main

class TestLanguageMentorApp(unittest.TestCase):

    @patch("tabs.scenario_tab.create_scenario_tab")
    @patch("tabs.conversation_tab.create_conversation_tab")
    @patch("tabs.vocab_tab.create_vocab_tab")
    @patch("gr.Blocks.launch")
    def test_main_function(self, mock_launch, mock_vocab_tab, mock_conversation_tab, mock_scenario_tab):
        """Test if main function initializes and launches the app."""
        main()

        # Assert that each tab creation function is called once
        mock_scenario_tab.assert_called_once()
        mock_conversation_tab.assert_called_once()
        mock_vocab_tab.assert_called_once()

        # Assert that the app's launch method is called with the correct parameters
        mock_launch.assert_called_once_with(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    unittest.main()
