import sys
import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def prompt_llm():
    if (len(sys.argv)) < 2: 
        raise Exception("Usage: python3 main,.py <PROMPT>") 
    prompt = sys.argv[1]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=prompt
    )

    print(response.text)

    print("Prompt tokens:",response.usage_metadata.prompt_token_count)
    print("Response tokens:",response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    prompt_llm()