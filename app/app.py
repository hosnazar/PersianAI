import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="PersianAI", page_icon="🤖")
st.title("🤖 PersianAI آفلاین و رایگان")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="HooshvareLab/gpt2-fa",
        device=-1
    )

generator = load_model()

q = st.text_area("سؤال یا متن فارسی را بنویس:")

if st.button("پاسخ بده"):
    if not q.strip():
        st.warning("متن وارد کن.")
    else:
        with st.spinner("در حال تولید پاسخ..."):
            out = generator(
                q,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
            )
            st.write(out[0]["generated_text"])
