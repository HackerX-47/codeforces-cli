from cfv2.imports import *

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_TOKEN"))

def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )

    return response.text