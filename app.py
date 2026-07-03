import streamlit as st
from chatbot.engine import MediBot
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="MediBot - AI Healthcare Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #00b4db 0%, #0083b0 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0, 180, 219, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .header-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.95);
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 0.5rem;
        position: relative;
        z-index: 1;
    }
    
    /* Status Badge */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(46, 204, 113, 0.2);
        color: #2ecc71;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 1rem;
        border: 1px solid rgba(46, 204, 113, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #2ecc71;
        border-radius: 50%;
        animation: blink 1.5s ease-in-out infinite;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }
    
    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a2a3a 0%, #0f1c2e 100%);
    }
    
    [data-testid="stSidebar"] > div {
        padding: 1.5rem 1rem;
    }
    
    .sidebar-title {
        color: #00b4db;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Feature Cards in Sidebar */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: white;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .feature-card:hover {
        background: rgba(0, 180, 219, 0.15);
        border-color: #00b4db;
        transform: translateX(5px);
    }
    
    /* Try Asking Cards */
    .try-card {
        background: linear-gradient(135deg, rgba(0, 180, 219, 0.1) 0%, rgba(0, 131, 176, 0.05) 100%);
        border: 1px solid rgba(0, 180, 219, 0.2);
        padding: 10px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
        color: #ecf0f1;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .try-card:hover {
        background: rgba(0, 180, 219, 0.2);
        transform: scale(1.02);
    }
    
    /* Chat Messages */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
        animation: slideIn 0.4s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* User message specific */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: linear-gradient(135deg, rgba(0, 180, 219, 0.15) 0%, rgba(0, 131, 176, 0.1) 100%);
        border-color: rgba(0, 180, 219, 0.3);
    }
    
    /* Chat Input */
    [data-testid="stChatInput"] {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 180, 219, 0.3);
        border-radius: 25px;
        transition: all 0.3s ease;
    }
    
    [data-testid="stChatInput"]:focus-within {
        border-color: #00b4db;
        box-shadow: 0 0 20px rgba(0, 180, 219, 0.3);
    }
    
    [data-testid="stChatInput"] textarea {
        color: white !important;
        font-size: 1rem !important;
    }
    
    /* Warning/Info Boxes */
    .warning-box {
        background: linear-gradient(135deg, rgba(231, 76, 60, 0.15) 0%, rgba(192, 57, 43, 0.1) 100%);
        border-left: 4px solid #e74c3c;
        padding: 12px 16px;
        border-radius: 10px;
        color: #ecf0f1;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(52, 152, 219, 0.15) 0%, rgba(41, 128, 185, 0.1) 100%);
        border-left: 4px solid #3498db;
        padding: 12px 16px;
        border-radius: 10px;
        color: #ecf0f1;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00b4db 0%, #0083b0 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 24px;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 180, 219, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 180, 219, 0.5);
    }
    
    /* Stats Container */
    .stats-container {
        display: flex;
        gap: 12px;
        margin: 1rem 0;
    }
    
    .stat-box {
        flex: 1;
        background: rgba(255, 255, 255, 0.05);
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stat-number {
        color: #00b4db;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.75rem;
        margin-top: 4px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00b4db, #0083b0);
        border-radius: 10px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.8rem;
        margin-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Divider */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 180, 219, 0.5), transparent);
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INITIALIZE BOT ====================
if "bot" not in st.session_state:
    st.session_state.bot = MediBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">
        🩺 About MediBot
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; line-height: 1.6;">
    Your AI-powered healthcare companion, available 24/7 to help you understand symptoms and provide guidance.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Features
    st.markdown('<div style="color: #00b4db; font-weight: 600; margin-bottom: 12px;">✨ Features</div>', unsafe_allow_html=True)
    
    features = [
        ("💬", "Natural Conversation"),
        ("🔍", "Symptom Analysis"),
        ("💊", "Medicine Suggestions"),
        ("👨‍⚕️", "Specialist Recommendations"),
        ("🚨", "Emergency Detection"),
    ]
    
    for icon, text in features:
        st.markdown(f"""
        <div class="feature-card">
            <span style="font-size: 1.2rem;">{icon}</span>
            <span>{text}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Stats
    st.markdown('<div style="color: #00b4db; font-weight: 600; margin-bottom: 12px;">📊 Session Stats</div>', unsafe_allow_html=True)
    
    total_msgs = len(st.session_state.messages)
    user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
    
    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-box">
            <div class="stat-number">{user_msgs}</div>
            <div class="stat-label">Questions</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">{total_msgs}</div>
            <div class="stat-label">Messages</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Try Asking
    st.markdown('<div style="color: #00b4db; font-weight: 600; margin-bottom: 12px;">💡 Try Asking</div>', unsafe_allow_html=True)
    
    examples = [
        "I have fever and body ache",
        "mujhe sardard ho raha hai",
        "What to eat for cold?",
        "Home remedies for acidity"
    ]
    
    for ex in examples:
        st.markdown(f'<div class="try-card">💭 {ex}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Reset Button
    if st.button("🔄 New Conversation", use_container_width=True):
        st.session_state.bot.reset()
        st.session_state.messages = []
        st.rerun()
    
    # Disclaimer
    st.markdown("""
    <div class="warning-box" style="margin-top: 1rem;">
        <strong>⚠️ Medical Disclaimer</strong><br>
        MediBot provides general information only. Always consult a qualified doctor for proper diagnosis and treatment.
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN AREA ====================

# Header
st.markdown("""
<div class="main-header">
    <h1 class="header-title">🩺 MediBot</h1>
    <p class="header-subtitle">Your AI Healthcare Assistant • Powered by Advanced AI</p>
    <div class="status-badge">
        <span class="status-dot"></span>
        <span>Online & Ready to Help</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Welcome message (only if no messages)
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="info-box">
        <strong>👋 Welcome to MediBot!</strong><br>
        I'm here to help you with your health questions. You can ask me in English or Hindi (Hinglish).
        Just type your symptoms or health concern below to get started.
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🩺"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("💬 Type your health question here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant", avatar="🩺"):
        with st.spinner("🤔 Analyzing your query..."):
            response = st.session_state.bot.respond(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# Footer
st.markdown("""
<div class="footer">
    Made with ❤️ by Yatharth | MediBot v2.0 | © 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)