import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
from chatbot.prompts import DOCTOR_SYSTEM_PROMPT
from chatbot.safety import is_emergency, get_emergency_response

# Load environment variables
load_dotenv()

class MediBot:
    def __init__(self):
        # Configure Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file!")
        
        genai.configure(api_key=api_key)
        
        # Initialize model with system prompt
        self.model = genai.GenerativeModel(
            model_name='models/gemini-flash-latest',
            system_instruction=DOCTOR_SYSTEM_PROMPT,
            generation_config={
                'temperature': 0.7,      # balanced creativity
                'top_p': 0.9,
                'max_output_tokens': 1024,
            }
        )
        
        # Start chat session (maintains context)
        self.chat = self.model.start_chat(history=[])
        self.conversation_log = []
    
    def respond(self, user_input):
        """Generate response using Gemini AI"""
        try:
            # Safety check first — emergency detection
            if is_emergency(user_input):
                emergency_msg = get_emergency_response()
                self._log(user_input, emergency_msg)
                return emergency_msg
            
            # Send to Gemini with conversation history
            response = self.chat.send_message(user_input)
            reply = response.text
            
            self._log(user_input, reply)
            return reply
        
        except Exception as e:
            error_msg = f"Sorry, I'm having trouble responding right now. 😔\n\nError: {str(e)}\n\nPlease try again in a moment."
            return error_msg
    
    def _log(self, user_msg, bot_msg):
        """Log conversation for debugging"""
        self.conversation_log.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'user': user_msg,
            'bot': bot_msg
        })
    
    def reset(self):
        """Reset conversation"""
        self.chat = self.model.start_chat(history=[])
        self.conversation_log = []