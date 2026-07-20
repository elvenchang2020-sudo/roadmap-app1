import os
import google.generativeai as genai

# define a AI summary function with Gemini API
def get_summary(log_data):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Error: No available API key"
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    以下のデータを読み取り、ユーザーが使ったアプリ（Executable_name列）と具体的な内容（Win_title列）から、
    ユーザーの仕事内容を推測し、簡潔にポイントで説明してください。"
    
    {log_data}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"