import streamlit as st
import httpx

st.set_page_config(page_title="هوش مصنوعی ایرانی", page_icon="🇮🇷", layout="centered")
st.title("🇮🇷 هوش مصنوعی فارسی")
st.caption("نسخه MVP واقعی: رابط فارسی + API + مدل محلی از طریق Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("پیام خود را بنویسید...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    history = [m for m in st.session_state.messages[:-1] if m["role"] in ["user", "assistant"]]

    with st.chat_message("assistant"):
        with st.spinner("در حال پردازش..."):
            try:
                response = httpx.post(
                    "http://localhost:8000/chat",
                    json={"message": prompt, "history": history},
                    timeout=180,
                )
                response.raise_for_status()
                answer = response.json()["answer"]
            except Exception as exc:
                answer = f"خطا: {exc}"
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
