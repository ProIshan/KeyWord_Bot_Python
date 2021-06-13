import datetime   



def welcome():  #welcome function to welcome
    print("Hello!")
  


hour = int(datetime.datetime.now().hour)


def wishme():  # WISHME FUNCTION which wishes according to time
    if hour >= 0 and hour < 12:
    
        print('Good Morning!')
    elif hour >= 12 and hour < 18:
  
        print("Good Afternoon!")
    else:
    
        print("Good Evening!")


hi = ("hi", "hello", "hey") #These are keywords
time = ("time", "hours") # These are keywords


def main():  # main function to work and reply on keywords

    user_input = input("Type: ".lower())
    user_words = user_input.split()

    for word in user_words:

        if word in hi:  # response on keywords hi
        
            print("Hello")
            return main()

        elif word in time:  # response on keyword time
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {strTime}")
 
            return main()


if __name__ == "__main__":   # main function to run all function in order
    welcome(), wishme(), main()
