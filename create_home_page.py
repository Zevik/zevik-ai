import os
import re

# --- הגדרות ---

SITE_DIRECTORY = "sites"  # הנתיב לתיקייה עם קבצי ה-HTML

# --- פונקציה ליצירת קובץ ה-index.html ---

def create_homepage(site_directory: str):
    """
    יוצר את הקובץ index.html עם קישורים לכל קבצי ה-HTML בתיקייה שצוינה.
    """
    
    print("\n--- יוצר עמוד בית (index.html) ---")
    
    # שלב 1: איסוף כל קבצי ה-HTML בתיקיית ה-sites
    html_files = []
    try:
        # עובר על כל הקבצים בתיקייה
        for filename in os.listdir(site_directory):
            # מוסיף לרשימה רק קבצי HTML שאינם index.html
            if filename.lower().endswith(".html") and filename.lower() != "index.html":
                html_files.append(filename)
    except FileNotFoundError:
        print(f"*** שגיאה: התיקייה '{site_directory}' לא נמצאה. ודא שהיא קיימת ובדיוק באותו מיקום של סקריפט הפייתון.")
        return

    if not html_files:
        print(f"לא נמצאו קבצי HTML בתיקייה '{site_directory}'. לא נוצר עמוד בית.")
        return

    # שלב 2: יצירת תוכן ה-HTML
    
    # הטקסט שלפני רשת הכפתורים
    html_start = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Art Styles Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        h1 {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .buttons-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }}
        .art-button {{
            background: white;
            border: none;
            padding: 20px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-decoration: none;
            display: block;
            color: #333;
            font-size: 1.1em;
            font-weight: 600;
            text-align: center;
        }}
        .art-button:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .art-button:active {{
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Art Styles Gallery 🎨</h1>
        <div class="buttons-grid">
"""

    # יצירת הקישורים
    buttons_html = ""
    for filename in html_files:
        # שם התצוגה: מנקה סיומת, מחליף קו תחתון ברווח, הופך אות ראשונה לגדולה.
        name_base = os.path.splitext(filename)[0]
        display_name = name_base.replace('_', ' ').title()
        
        # הנתיב לקובץ הוא sites/filename.html
        # os.path.join בונה נתיב: sites/filename.html
        # .replace(os.sep, '/') הופך את התו המפריד של מערכת ההפעלה (למשל \) ל- / ב-HTML
        relative_path = os.path.join(site_directory, filename).replace(os.sep, '/')
        
        buttons_html += f'            <a href="{relative_path}" class="art-button">{display_name}</a>\n'

    # הטקסט שאחרי רשת הכפתורים
    html_end = """
        </div>
    </div>
</body>
</html>
"""

    # שלב 3: כתיבת הקובץ index.html
    # הקובץ נכתב בתיקייה הראשית (מעל ה-sites)
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_start)
            f.write(buttons_html)
            f.write(html_end)
            
        print(f"עמוד הבית נוצר בהצלחה: index.html ({len(html_files)} קישורים).")
    except Exception as e:
        print(f"*** שגיאה בכתיבת index.html: {e}")

def main():
    create_homepage(SITE_DIRECTORY)
    print("\n--- סיום מושלם! ---")


if __name__ == "__main__":
    main()