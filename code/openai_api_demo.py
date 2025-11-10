from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    # Load environment variables (e.g., OPENAI_API_KEY)
    load_dotenv()

    client = OpenAI()

    # Keep the existing model and developer instruction to "talk like a pirate"
    model = "gpt-5"
    messages = [
        {
            "role": "developer",
            "content": "Talk like a 5yo kid.",
        }
    ]

    print("Chatbot ready. Type 'exit' or 'quit' to leave.\n")

    while True:
        try:
            user_text = input("You: ").strip()
            if not user_text:
                continue
            if user_text.lower() in {"exit", "quit", "q"}:
                print("Bot: Arrr, fair winds to ye! 🏴‍☠️")
                break

            # Add the user's message to the running conversation
            messages.append({"role": "user", "content": user_text})

            response = client.responses.create(
                model=model,
                reasoning={"effort": "low"},
                input=messages,
            )

            reply_text = response.output_text
            print(f"Bot: {reply_text}")

            # Keep context by appending the assistant's reply
            messages.append({"role": "assistant", "content": reply_text})

        except KeyboardInterrupt:
            print("\nBot: Arrr, I be shovin' off now!")
            break
        except Exception as e:
            # Don't crash the loop on transient errors
            print(f"Bot (error): {e}")


if __name__ == "__main__":
    main()
