import mac_say # pip install mac_say
import datetime


def welcome():  # welcome function to welcome
    print("Hello!")
    mac_say.say("Hello!")


hour = int(datetime.datetime.now().hour)


def wishme():  # WISHME FUNCTION which wishes according to time
    if hour >= 0 and hour < 12:
        mac_say.say("Good Morning!")
        print('Good Morning!')
    elif hour >= 12 and hour < 18:
        mac_say.say("Good Afternoon!")
        print("Good Afternoon!")
    else:
        mac_say.say("Good evening!")
        print("Good Evening!")


hi = ("hi", "hello", "hey")  # These are keywords
time = ("time", "hours")  # These are keywords


def main():  # main function to work and reply on keywords


    user_input = input("Type: ".lower())
    user_words = user_input.split()

    for word in user_words:

        if word in hi:  # response on keyword time
            mac_say.say("Hello")
            print("Hello")
            return main()
        
        elif word in time:  # response on keywords hi
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {strTime}")
            mac_say.say(f"The Time is {strTime}")
            return main()


if __name__ == "__main__":  # main function to run all function in order
    welcome(), wishme(), main()
