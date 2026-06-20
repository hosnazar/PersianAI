import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(
    page_title="PersianAI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 PersianAI")
st.caption("نسخه رایگان، بدون API، مناسب اجرا روی Hugging Face Spaces")

MODEL_NAME = "HooshvareLab/gpt2-fa"

@st.cache_resource(show_spinner=True)
def load_model():
    return pipeline(
        task="text-generation",
        model=MODEL_NAME,
        device=-1,
    )

try:
    generator = load_model()
except Exception as e:
    st.error("مدل بارگذاری نشد.")
    st.exception(e)
    st.stop()

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("تنظیمات")
    max_tokens = st.slider("طول پاسخ", 40, 220, 120, 10)
    temperature = st.slider("خلاقیت", 0.2, 1.2, 0.7, 0.1)
    top_p = st.slider("Top-p", 0.5, 1.0, 0.9, 0.05)
    if st.button("پاک کردن گفتگو"):
        st.session_state.history = []
        st.rerun()

st.info(
    "این نسخه از مدل فارسی کوچک استفاده می‌کند. کیفیت آن مثل ChatGPT نیست، "
    "اما بدون API و بدون هزینه اجرا می‌شود."
)

for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

prompt = st.chat_input("سؤال یا متن فارسی را بنویس...")

if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.write(prompt)

    instruction = (
        "متن زیر را ادامه بده و تا حد ممکن فارسی، منسجم و مفید پاسخ بده:\n\n"
        f"کاربر: {prompt}\n"
        "پاسخ:"
    )

    with st.chat_message("assistant"):
        with st.spinner("در حال تولید پاسخ..."):
            try:
                set_seed(42)
                output = generator(
                    instruction,
                    max_new_tokens=max_tokens,
                    do_sample=True,
                    temperature=float(temperature),
                    top_p=float(top_p),
                    repetition_penalty=1.15,
                    pad_token_id=generator.tokenizer.eos_token_id,
                )
                generated = output[0]["generated_text"]
                answer = generated.replace(instruction, "").strip()

                if not answer:
                    answer = "پاسخ تولید نشد. سؤال را کوتاه‌تر و واضح‌تر بنویس."

                st.write(answer)
                st.session_state.history.append(("assistant", answer))
            except Exception as e:
                st.error("خطا در تولید پاسخ.")
                st.exception(e)
