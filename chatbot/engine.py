import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from chatbot.prompts import DOCTOR_SYSTEM_PROMPT
from chatbot.safety import is_emergency, get_emergency_response

# Load environment variables
load_dotenv()

class MediBot:
    def __init__(self):
        # Configure Groq
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file!")
        
        # Initialize Groq client
        self.client = Groq(api_key=api_key)
        
        # Model configuration
        self.model_name = "llama-3.3-70b-versatile"  # Best free model on Groq
        self.temperature = 0.7
        self.max_tokens = 1024
        
        # Conversation history (Groq uses message list format)
        self.messages = [
            {"role": "system", "content": DOCTOR_SYSTEM_PROMPT}
        ]
        
        self.conversation_log = []
    
    def respond(self, user_input):
        """Generate response using Groq AI"""
        try:
            # Safety check first — emergency detection
            if is_emergency(user_input):
                emergency_msg = get_emergency_response()
                self._log(user_input, emergency_msg)
                return emergency_msg
            
            # Add user message to history
            self.messages.append({"role": "user", "content": user_input})
            
            # Send to Groq with full conversation history
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            
            reply = response.choices[0].message.content
            
            # Add bot reply to history (maintains context)
            self.messages.append({"role": "assistant", "content": reply})
            
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
        self.messages = [
            {"role": "system", "content": DOCTOR_SYSTEM_PROMPT}
        ]
        self.conversation_log = []