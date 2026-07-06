import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="FIFA 2026 StadiumPulse AI", page_icon="⚽", layout="wide")

# Sidebar for Secure API Input
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.sidebar.warning("Please enter your Gemini API Key to activate the assistant.")

# Header
st.title("⚽ FIFA World Cup 2026 - StadiumPulse AI")
st.subheader("GenAI-Enabled Smart Stadium Operations & Fan Experience Platform")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("🌐 Fan & Volunteer Assistant")
    st.info("Ask about navigation, restrooms, food counters, or language support.")
    
    fan_query = st.text_input("Ask Stadium Assistant", placeholder="Type your query here...")
    
    if st.button("Ask AI"):
        if not api_key:
            st.error("Please provide an API key in the sidebar.")
        elif fan_query:
            with st.spinner("Processing..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    context_prompt = f"You are an advanced multilingual stadium assistant for the FIFA World Cup 2026. Provide precise and concise answers. Query: {fan_query}"
                    response = model.generate_content(context_prompt)
                    st.success("AI Response:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

with col2:
    st.header("📊 Operational Intelligence Control")
    st.info("Real-time crowd monitoring and automated incident support for venue staff.")
    
    gate_density = st.slider("Gate 3 Crowd Density (%)", 0, 100, 85)
    incident_report = st.selectbox("Reported Incident", ["None", "Medical Emergency near Section 110", "Crowd bottleneck at Turnstile B"])
    
    if st.button("Generate Smart Action Protocol"):
        if not api_key:
            st.error("Please provide an API key in the sidebar.")
        else:
            with st.spinner("Analyzing context..."):
                model = genai.GenerativeModel('gemini-pro')
                ops_prompt = f"You are an AI Operational Command Center Agent for FIFA 2026. Gate 3 Crowd Density: {gate_density}%. Incident: {incident_report}. Provide a 3-step actionable dispatch protocol."
                response = model.generate_content(ops_prompt)
                st.warning("⚠️ Recommended AI Protocol:")
                st.write(response.text)
