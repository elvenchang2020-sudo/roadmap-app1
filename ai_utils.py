import os
import google.generativeai as genai

def get_summary(data_markdown):
    """Sends the data table to Gemini and returns the AI summary."""
    # Ensure your API key is in the environment (set in your Dockerfile or .env)
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Error: GEMINI_API_KEY is not configured."
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Analyze these productivity logs and provide a short, 
    insightful summary of the user's activity:
    
    {data_markdown}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"