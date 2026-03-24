from google import genai


def gemini(prompt="Explain how AI works in a few words"):

    client = genai.Client(api_key="AIzaSyDJhUCZzpzgAccfmCKo6G4rMksy4bLhLlc")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )

    return response.text
