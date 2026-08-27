from cfcli.imports import *

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_TOKEN"))

print(os.getenv("GEMINI_TOKEN"))
def ask_gemini(prompt):
    print("DEBUG: Gemini function called")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text