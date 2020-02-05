# Declare libraries/modules if any
import os
import webbrowser

# Setting up arrays to scan words
good = ["happy", "cheerful", "glad", "good", "great", "pleased", "thrilled", "blessed", "content", "joyful"]
bad = ["depressed", "sad", "upset", "suicidal", "worthless", "self harm", "selfharm", "down", "unhappy", "sorrow",
       "sorrowful", "troubled", "anxious", "anxiety attack", "anxiety"]

# main function where it will carry the code within all the code
def main():
    welcome()

# Welcome function in charge of guiding the user to however they feel.
def welcome():
    name = str(input("Hello...\nOh! I'm sorry! I haven't asked for your name. So talk to me:\nWhat is your name?\n")).lower()
    print("Oh, you're name is", name + "?")
    answerOne = str(input("")).lower()
    # breaks down code in case if misspelled name or desires to use a different name
    while answerOne:
        if answerOne == "yes" or answerOne == "ya" or answerOne == "yeah" or answerOne == "yea":
            print("Alright! Sweet!")
            break
        else:
            print("Oh? So what is your name?")
            while True:
                name = str(input(""))
                if name == "":
                    break
                print("Alright then, " + name + ".\nGlad to meet you. I will do everything I can to help.")
                break
            break
    # mood will determine feeling [state of mind] of user; will use arrays to find words similar to, if not the same
    mood = str(input("So, how is everything?\n"
                     "Good or Bad?\n")).lower()
    if mood in good:
        # takes to good mood function
        goodMood()
    else:
        while mood not in good:
            # takes to get the user help needed
            badMood()
            break

# very short function for defining the user in a good state of mind.
def goodMood():
    print("That's good! I am assuming everything is going well for you then!\n"
          "Keep up the good work!\n")
    input("Press Enter to Exit: ")

# Function to give suicide prevention resources to user if feelings get to this point
# Gives number and website information upon request
def suicideHelper():
    print("Here is the suicide hotline number, in case something goes wrong: 1(800) 273 8255.")
    print("https://suicidepreventionlifeline.org/")
    rip = input("Would you like to go there now?")
    if "yes" in rip:
        webbrowser.open_new_tab('https://suicidepreventionlifeline.org/')
    else:
        pass
    print("Remember: everything in life may be fixed, except for your death;\n"
          "there is no solution to death..\n")
    return

# Bad mood function meant for the user to navigate when in need of support
def badMood():
    # Prompts the user if they would like to vent their stress.
    print("Oh, I'm sorry to hear. Would you like to vent?\n"
          "Venting is useful when you're in a bad state of mind.\n"
          "It's better to let stress out in a positive way, like writing or\n"
          "singing. So how about it? Would you like to type about it?\n"
          "I'm all ears!\n"
          "yes or no?")
    vent = input("").lower()
    if "yes" in vent:
        # IF user agrees, the program will record whatever data the user types in.
        print("I'm glad. You can start typing now [Once you're done typing\n"
              "if you still have space left, slowly and continuously press\n"
              "the \"Enter\" key]{MAX 20 LINES}:")
        # Creates a mini function to get one input for multiple lines without overriding
        no_of_lines = 20
        lines = ""
        for i in range(20):
            lines += input() + "\n"
            space = lines
    else:
        # Alternatives to venting
        # area for offering information
        print("If no, then its okay. Any reason in particular you feel the way you feel?\n"
              "What's going on? I could be of some help, depending of what you need.\n"
              "Are you...(or feeling)\n"
              "Suicidal, depressing moments, no confidence?\n")
        reason = input("").lower()
        if "suicidal" in reason:
            # Helps with suicide and goes through suicide function
            suicideHelper()
        elif "depress" in reason:
            # Attempts to get the user to show at least a bit of a smile
            print("We all have our ups and downs. Some of us may have it worse. Some of us may\n"
                  "experience a close one's death, or maybe someoone's house hurned down. We \n"
                  "all have horrid days, and some of us lives. Some people spend most of their\n"
                  "teens being bullied only for being different. What makes all those people,\n"
                  "including you, different are the fact you guys are fighters and come out \n"
                  "doing better than ever. Don't give up! You should read these empowering quotes\n"
                  "from the google search engine.")
            input("Press Enter: ")
            # Opens a new tab for positive quotes
            webbrowser.open_new_tab('https://www.google.com/search?safe=off&hl=en&biw=1476&bih=723&tbm=isch&sxsrf=ACYBGNQsBJxuajVxUeERnTvD67t74hUECQ%3A1571568286588&sa=1&ei=njqsXdG8I8mc_QabxIHwAg&q=quotes+on+never+giving+up&oq=quotes+on+never+&gs_l=img.3.0.0l10.62394.67938..68967...2.0..0.712.5252.8j0j2j0j4j3j1......0....1..gws-wiz-img.......35i39j0i67j0i10.wrcYoLIaChM')
            print("Hope this helped you feel a bit better!")
            input("press start.")
        else:
            if "confide" in reason:
                # Serves to be a confidence booster
                print("We've all been to a point where we have lost ourselves. \n"
                      "So, this motivational video from Will Smith should help.\n"
                      "Watch it.")
                input("Press enter to open the video on YouTube.")
                webbrowser.open_new_tab('https://www.youtube.com/watch?v=ft_DXwgUXB0')
            else:
                print("Well, it's okay. I understand if you don't trust me. All I want you to know\n"
                      "is that I am here to listen.\n")
        while True:
            # Asks the user to politely finish the program. makes an infinite loop and terminates the program once thank you is typed
            y = input("Type in \"Thank You\" to exit.\n").lower()
            if y == "thank you":
                os.system(exit())
    print("Would you like to save your typing?\nYes or no?\n")
    # This is in case the user would like to save whatever they typed up
    optTwo = input("").lower()
    if optTwo == "yes":
        # makes a title for the file
        mewt = input("Title name?\n")
        # sets the file to create then write
        file = open(mewt+".txt", "w")
        # Writes information to the text document
        file.write(space)
        # Closes the document
        file.close()
        # Thanks the user for self awareness
        print("Thank you for dedicating time to yourself. You needed it.\n"
              "Hope you get better soon!")
        input("Press Enter. ")
    else:
        print("Alright. I'll see you soon then!")
        input("Press Enter: ")

# Runs the entire code
main()