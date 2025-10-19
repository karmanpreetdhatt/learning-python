answer = 'Y'
while answer.upper() == 'Y':

    reply = input(
        """Can you tell me how much time you have studied today? Have you studied for...
    Ω eternities, 5 hrs, 3 hrs or 1 hr?
            Please enter..."""
    )
    if reply.upper() == 'ABSOLUTE INFINITE ETERNITIES':
        print("Wow! That's impressive dedication! Remember to take breaks! 📚🌟" 
        "")
    elif reply.upper() == '5 HRS':
        print("Great effort! Make sure to balance study with rest! 🧠💤" 
        "")
    elif reply.upper() == '3 HRS':
        print("Good job! Keep up the consistent study habits! 📖👍" 
        "")
    elif reply.upper() == '1 HR':
        print("Nice! Every bit counts, keep going! 🚀😊" 
        "")
    else:
        print("Hmm,that seems interesting. Are you sure about that? 🤔" 
        "")
    answer = input(
        "Do you want to tell me how much time you have studied today again? (Y/N)"
    )
print("Bye,bye, thank you for sharing your study time with me!")
print("Also, remember to balance study time with relaxation! 🧘‍♀️")