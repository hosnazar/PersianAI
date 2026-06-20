import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="هوش مصنوعی فارسی", page_icon="🤖")
st.title("🤖 هوش مصنوعی فارسی")
st.caption("نسخه وب رایگان با OpenRouter Free Models")

api_key = st.secrets.get("OPENROUTER_API_KEY", "")

if not api_key:
    st.error("OPENROUTER_API_KEY در Secrets تنظیم نشده است.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "تو یک دستیار فارسی دقیق، فنی و مفید هستی. پاسخ‌ها را فارسی و شفاف بده."
        }
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("سؤال خود را بنویس...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=st.session_state.messages,
            temperature=0.4,
        )

        answer = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": answer})

        with st.chat_message("assistant"):
            st.write(answer)

    except Exception as e:
        st.error(f"خطا: {e}")
