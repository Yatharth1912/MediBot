import streamlit as st
from chatbot.engine import MediBot

# Page config
st.set_page_config(
    page_title="MediBot - AI Healthcare Assistant",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        padding: 10px;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-top: 0px;
    }
    .disclaimer {
        background-color: #FFF3CD;
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #FFC107;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>🩺 MediBot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your AI-Powered Healthcare Assistant</p>", unsafe_allow_html=True)
st.divider()

# Initialize bot
if 'bot' not in st.session_state:
    try:
        st.session_state.bot = MediBot()
        st.session_state.messages = [
            {'role': 'assistant', 'content': "Hey there! 👋 I'm MediBot, your friendly health assistant. How are you feeling today? Feel free to share any symptoms or just have a chat!"}
        ]
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {e}")
        st.info("Please add your GEMINI_API_KEY to the .env file.")
        st.stop()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # User message
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    
    # Bot response with loading spinner
    with st.chat_message('assistant'):
        with st.spinner("MediBot is thinking..."):
            response = st.session_state.bot.respond(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({'role': 'assistant', 'content': response})

# Sidebar
with st.sidebar:
    st.header("🩺 About MediBot")
    st.write("MediBot is an AI-powered healthcare assistant that:")
    st.write("✅ Understands natural conversation")
    st.write("✅ Analyzes symptoms intelligently")
    st.write("✅ Suggests medicines & remedies")
    st.write("✅ Recommends specialists")
    st.write("✅ Detects emergencies instantly")
    
    st.divider()
    
    st.subheader("💡 Try Asking:")
    st.code("I have fever and body ache", language=None)
    st.code("mujhe sardard ho raha hai", language=None)
    st.code("what to eat for cold?", language=None)
    st.code("home remedies for acidity", language=None)
    
    st.divider()
    
    if st.button("🔄 Reset Conversation", use_container_width=True):
        st.session_state.bot.reset()
        st.session_state.messages = [
            {'role': 'assistant', 'content': "Fresh start! 🌟 How can I help you today?"}
        ]
        st.rerun()
    
    st.divider()
    st.markdown("<div class='disclaimer'>⚠️ <b>Disclaimer:</b> MediBot is an AI assistant for informational purposes only. Always consult a qualified doctor for medical advice.</div>", unsafe_allow_html=True)
    
    st.divider()
    st.caption("Powered by Google Gemini AI")