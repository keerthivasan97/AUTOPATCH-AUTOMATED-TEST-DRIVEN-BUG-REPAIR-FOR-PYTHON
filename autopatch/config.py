from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
MAX_RETRIES = 3
TEST_TIMEOUT_SECONDS = 30