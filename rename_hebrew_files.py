# הקובץ צריך להיות נקי ממפתח קשיח
import os
from openai import OpenAI
from openai import APIError

# API_KEY = "YOUR_OPENAI_API_KEY" # ודא ששורה זו או שורה דומה לה **נמחקה** או הוחלפה ב-os.environ.get("OPENAI_API_KEY")

DIRECTORY_PATH = "."
MODEL_NAME = "gpt-3.5-turbo"

# --- אתחול לקוח OpenAI ---
try:
    # מומלץ: OpenAI יחפש את המפתח במשתנה סביבה בשם OPENAI_API_KEY
    client = OpenAI() 
except ValueError as e:
    # ...
    exit()

# ... שאר הקוד