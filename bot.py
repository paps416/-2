import ollama

def chat():
    print("test bot")
    messages = []

    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "exit":
            print("bb")
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(model="dolphin-llama3", messages=messages)

        # ответ
        assistant_reply = response["message"]["content"]

        messages.append({"role": "assistant", "content": assistant_reply})

        print("Бот:", assistant_reply)

if __name__ == "__main__":
    chat()
