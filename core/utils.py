def clean_text(text):
    import re
    return re.sub(r"[^\w\s]", "", text.lower().strip())
