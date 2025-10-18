answer = 'Y' 

while answer.upper() == 'Y':

    reply = input(
        """Can you tell me how much TV you have watched today? Have you watched it for...
 Ω milleniums, 2 hrs, 1 hr or 30 mins?
            Please enter..."""
    )

    if reply.upper() == 'ABSOLUTE INFINITE MILLENIUMS':
        print("Whoa! That's heavenly an eternity! Stop! Time to take a break! ⏳🚀")

    elif reply.upper() == '2 HRS':
        print("That's a lot of TV! Try to take breaks and stretch! 📺🧘‍♂️" 
        "")
    elif reply.upper() == '1 HR':
        print("Good job! Remember to balance TV time with other activities! 📚⚽"
              )
    elif reply.upper() == '30 MINS':
        print("Great! Keep it up and enjoy your day! 🌞😊")
    else:
        print("Hmm, that's funny. What a joke! 😅")
    answer = input(
        "Do you want to tell me how much TV you have watched today again? (Y/N)"
    )
print("Bye,bye, thank you for sharing your TV time with me!")
print("Also, remember to balance screen time with outdoor activities! 🌳🏃‍♀️")