import time
 
print("Welcome to the Elite 101 Chatbot!")
name = input("What is your name? \n")
age = int(input("How old are you? \n"))
print("How can I help you today? Enter a number. ")
query = int(input("1. Tell me today's weather.\n2. Tell me a joke.\n3. Tell me my name and what grade I could be in.\n4. Exit\n"))
if (query == 1):
    print("Today's weather is sunny, with temperatures above 100 degrees! Gotta love living in Texas!")
elif (query == 2):
    print("How do trees get online? ")
    time.sleep(2);
    print("They log in!")
elif (query == 3):
    print("Your name is ", name, ".")
    if (age < 11):
      print("You are likely in elementary school!")
    elif (age < 14):
      print("You are likely in middle school!")
    elif (age < 18):
      print("You are likely in high school!")
    else:
      print("This function is still under construction. Check back in later!")
elif (query == 4):
    print("Thanks for coming! See you later,", name,".")

