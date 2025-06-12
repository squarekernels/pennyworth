import sys
import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def prompt_llm():
    verbose = False 

    if (len(sys.argv)) < 2: 
        exit(1)
        raise Exception("Usage: python3 main,.py <PROMPT>") 

    if (len(sys.argv) == 3 and sys.argv[2] == "--verbose"):
        verbose = True
    
    prompt = sys.argv[1]

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    if (verbose):
        print(f"User prompt: {prompt}")
        print(response.text)

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)
        
if __name__ == "__main__":
    prompt_llm()
