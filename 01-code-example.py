import os
import gradio as gr
from google import genai

def call_gemini_model(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    """
    Calls a Google Gemini model with a given prompt and returns the response.

    Args:
        prompt: The text prompt to send to the Gemini model.
        model_name: The name of the Gemini model to use (default: "gemini-2.5-flash").

    Returns:
        The text response from the Gemini model, or an error message if the call fails.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY environment variable not set."

    # The google.genai package automatically picks up GOOGLE_API_KEY from environment variables.
    # No explicit configuration call like genai.configure() or genai.set_api_key() is needed.

    client = genai.Client() # Initialize the client
    try:
        # Apply the suggested edit here:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error calling Gemini model: {e}"

def chat_interface_function(message, history):
    # history is a list of lists: [[user_msg1, bot_msg1], [user_msg2, bot_msg2], ...
    # message is the current user input

    # Call the existing Gemini model function
    response = call_gemini_model(message)
    return response

if __name__ == '__main__':
    # Gradio Interface
    gr.ChatInterface(chat_interface_function, 
                     title="Easy Chatbot").launch(theme=gr.themes.Glass())

