
import datetime  # importing library to check current date/time



def welcome():  #welcome function to welcome
    print("Hello!")



hour = int(datetime.datetime.now().hour) # keeping current time in a variable


def wishme():  # WISHME FUNCTION which wishes according to time
    if hour >= 0 and hour < 12: # if time is between 0 to 12hrs 
        print('Good Morning!')  # print Good Morning
    elif hour >= 12 and hour < 18: # else if time is between 12 to 18hrs 
        print("Good Afternoon!") # print Good Afternoon
    else: # if none of above statements true
        print("Good Evening!")  # print Good Evening


hi = ("hi", "hello", "hey") # These are keywords
time = ("time", "hours") # These are keywords


def main():  # main function to work and reply on keywords

    user_input = input("Type: ".lower()) # taking input and making it lower case
    user_words = user_input.split() # splitting the input sentence in words

    for word in user_words: # using for loop for checking if there is any matching keyword in sentence 

        if word in hi:  # response on keywords hi
            print("Hello")
            return main()

        elif word in time:  # response on keyword time
            strTime = datetime.datetime.now().strftime("%H:%M") # keeping current time in a variable
            print(f"The time is {strTime}") # printing current time
            return main()


if __name__ == "__main__":   # main function to run all function in order
    welcome(), wishme(), main()
