from dotenv import load_dotenv
import os
load_dotenv()

GeminiAPIKey = os.getenv("Gemini_API_Key")
ModelName = "gemini-flash-latest"
MaxRetries = 3
TestTimeoutSec = 30