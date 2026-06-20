# PersianAI

PersianAI یک نمونه رایگان و ساده از دستیار فارسی است که بدون API پولی روی Hugging Face Spaces اجرا می‌شود.

## اجرای محلی

```bash
pip install -r requirements.txt
streamlit run app.py
```

## اجرا روی Hugging Face Spaces

1. در GitHub این سه فایل را قرار بده:
   - `app.py`
   - `requirements.txt`
   - `README.md`
2. وارد Hugging Face شو.
3. Create new Space بزن.
4. SDK را روی Streamlit بگذار.
5. Hardware را روی CPU basic - Free بگذار.
6. فایل‌ها را آپلود کن یا ریپو GitHub را وصل کن.

## محدودیت

این نسخه از مدل `HooshvareLab/gpt2-fa` استفاده می‌کند. کیفیت آن مثل ChatGPT نیست، اما بدون API و بدون هزینه اجرا می‌شود.
