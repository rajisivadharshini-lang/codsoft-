print("=== Student Help Bot ===")

while True:

    question = input("You: ").lower()

    if question == "attendance":
        print("Bot: Maintain at least 75% attendance.")

    elif question == "exam":
        print("Bot: Prepare important questions and revise regularly.")

    elif question == "project":
        print("Bot: Choose a simple and useful project topic.")

    elif question == "placement":
        print("Bot: Improve coding, aptitude and communication skills.")

    elif question == "bye":
        print("Bot: All the best. Goodbye!")
        break

    else:
        print("Bot: Please ask about attendance, exam, project or placement.")