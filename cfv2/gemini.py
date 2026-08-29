from cfv2.imports import *

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_TOKEN"))

def ask_gemini(prompt):

    try:
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

    except Exception as e:

        if getattr(e, "code", None) == 429:

            print()
            print("────────────────────────────────────────")
            print("AI ANALYSIS")
            print("────────────────────────────────────────")
            print()
            print("Gemini API quota exhausted.")
            print()
            print("Free Tier daily request limit reached")
            print("for gemini-3.6-flash.")
            print()
            print("Try again tomorrow.")
            print()
            print("────────────────────────────────────────")

            return None

        return None