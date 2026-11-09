from google import genai
from loadset import gemini_api_key

def get_connection():

    client = genai.Client(api_key=gemini_api_key)
    return client

def get_response(prompt):
    client = get_connection()
    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
    )

    print("Response:", response.output_text)

def main():
    print("*" *50)
    print("Welcome to the Gemini API Chatbot!")
    print("*" *50, "\n")

    while True:
        prompt = input("Gemini-flash :")
        get_response(prompt)
        print()
        print("="*50)
        print()

        choice = input("Do you want to continue? (y/n): ")
        if choice != 'y':
            print("Exiting the chatbot. Goodbye!")
            break

if __name__ == "__main__":
    main()