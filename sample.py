from google import genai
from typing import List, Dict

class GeminiChatbot:
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []

    def add_to_history(self, role: str, content: str):
        """Add a message to the conversation history"""
        self.conversation_history.append({
            "role": role,
            "parts": [{"text": content}]
        })

    def generate_response(self, user_input: str) -> str:
        """Generate a response from the model with conversation context"""
        self.add_to_history("user", user_input)

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=self.conversation_history
            )
            bot_response = response.text
            self.add_to_history("model", bot_response)
            return bot_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []

# Example usage
if __name__ == "__main__":
    # Initialize the chatbot (replace with your actual API key)
    chatbot = GeminiChatbot(api_key="AIzaSyDYlLPKXjcrvyTMl8ANYH_FgvKM1mrIdcM")

    print("Gemini Chatbot initialized. Type 'quit' to exit or 'clear' to reset the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'clear':
            chatbot.clear_history()
            print("Conversation history cleared.")
            continue

        response = chatbot.generate_response(user_input)
        print("Bot:", response)
