from dotenv import load_dotenv
import os
load_dotenv()

GeminiAPIKey = os.getenv("Gemini_API_Key")
ModelName = "gemini-2.5-flash"
MaxRetries = 3
TestTimeoutSec = 30