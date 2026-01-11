import ollama

def get_info(
        lang: str
        ,topic: str) -> str:
    prompt = f"""
You are a Technical coding expert. For the '{lang}','{topic}', provided, give a detailed response including:

1. code implementation.

2. Explanation of the code.

3. Best practices.

Keep response concise, accurate, and safe. Use markdown.
"""
    response = ollama.chat(
        model='phi3:mini',
        messages=[{'role': 'user', 'content': prompt}],
        stream=False
    )
    return response['message']['content']
