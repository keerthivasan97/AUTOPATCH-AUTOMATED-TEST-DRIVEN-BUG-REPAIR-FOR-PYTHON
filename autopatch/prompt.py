from google import genai
from autopatch.config import GeminiAPIKey, ModelName
client =genai.Client(api_key=GeminiAPIKey) #from config.py env variable

def generate_fix(traceback_text:str,src_code:str)->str:
    prompt = f"""following code code has a bug.therefore code is not working properly. please fix the bug and return only the fixed code without any explanation.
    TRACEBACK:
    {traceback_text}

    SOURCE CODE:
    {src_code}

    Return ONLY the complete corrected version of this file's code, exactly ONCE. do not repeat the code. Do not include explanations, markdown code fences, or diff formatting.
    Output the corrected Python code a single time, with nothing before or after it."""
    response = client.models.generate_content(
        model=ModelName,
        contents=prompt
    )
    return response.text.strip()