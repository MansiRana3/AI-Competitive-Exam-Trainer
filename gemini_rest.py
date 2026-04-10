# gemini_rest.py
import requests
from config import GEMINI_API_KEY, GEMINI_REST_BASE_URL


def call_gemini_rest(prompt: str) -> str:
    """
    Sends a single message to Gemini using raw HTTP POST.
    Zero-shot prompting — just a direct question, no setup.
    """

    url = f"{GEMINI_REST_BASE_URL}?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    print(f"\n📤 Sending to Gemini (REST): {prompt}")
    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        error_msg = response.json().get("error", {}).get("message", "Unknown error")
        raise Exception(f"❌ API Error {response.status_code}: {error_msg}")

    response_data = response.json()

    gemini_reply = response_data["candidates"][0]["content"]["parts"][0]["text"]

    print(f"📥 Gemini replied: {gemini_reply}")
    return gemini_reply


if __name__ == "__main__":
    answer = call_gemini_rest("What is the capital of France?")
    print(f"\n✅ Final answer: {answer}")
