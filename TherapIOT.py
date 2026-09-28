# Declare libraries/modules if any
import re
import webbrowser
from datetime import datetime
from pathlib import Path

# Setting up arrays to scan words
good = ["happy", "cheerful", "glad", "good", "great", "pleased", "thrilled", "blessed", "content", "joyful",
        "fine", "okay", "ok", "well"]
bad = ["depressed", "sad", "upset", "suicidal", "worthless", "self harm", "selfharm", "down", "unhappy", "sorrow",
       "sorrowful", "troubled", "anxious", "anxiety attack", "anxiety", "bad", "awful", "terrible"]
negations = ["not", "no", "never", "isn't", "don't", "aren't", "wasn't", "nothing"]
# Phrases that mean the user may be in danger; checked on EVERY answer
crisis = ["suicid", "kill myself", "end my life", "end it all", "want to die", "wanna die", "better off dead",
          "self harm", "selfharm", "self-harm", "hurt myself", "cut myself", "no reason to live"]
yes = ["yes", "y", "ya", "yeah", "yea", "yep", "sure", "ok", "okay"]

# Vents are saved here, in the user's home folder, so they're easy to find again
journal_dir = Path.home() / "TherapiBot Journal"


# main function where it will carry the code within all the code
def main():
    print("(TherapiBot is a friendly listener, not a therapist. If you are in crisis,\n"
          " call or text 988 in the US, or find a helpline anywhere at findahelpline.com.)\n")
    try:
        welcome()
    except (KeyboardInterrupt, EOFError):
        print("\nTake care of yourself. I'll be here whenever you need me.")


def is_crisis(text):
    text = text.lower()
    return any(phrase in text for phrase in crisis)


def is_good(mood):
    # "good" only counts if nothing bad or negated is mixed in ("not good", "good but anxious")
    words = re.findall(r"[a-z']+", mood.lower())
    return (any(word in good for word in words)
            and not any(word in negations for word in words)
            and not any(word in mood.lower() for word in bad))


# Every question goes through here so a cry for help is never missed, no matter where it's typed
def ask(prompt=""):
    answer = input(prompt).strip()
    if is_crisis(answer):
        crisisHelp()
    return answer


# Shown the moment anything the user types sounds like they may be in danger
def crisisHelp():
    print("\nIt sounds like you're carrying something really heavy right now.\n"
          "You don't have to go through this alone. Please reach out to a real person:\n"
          "  US: call or text 988 (988lifeline.org)\n"
          "  Anywhere else: findahelpline.com\n"
          "  If you are in immediate danger, call your local emergency number.\n")


# Welcome function in charge of guiding the user to however they feel.
def welcome():
    name = ask("Hello...\nOh! I'm sorry! I haven't asked for your name. So talk to me:\nWhat is your name?\n")
    # breaks down code in case if misspelled name or desires to use a different name
    if ask("Oh, your name is " + name + "?\n").lower() in yes:
        print("Alright! Sweet!")
    else:
        name = ask("Oh? So what is your name?\n") or name
        print("Alright then, " + name + ".\nGlad to meet you. I will do everything I can to help.")
    # mood will determine feeling [state of mind] of user; will use arrays to find words similar to, if not the same
    mood = ask("So, how is everything?\n"
               "Good or Bad?\n")
    if is_good(mood):
        # takes to good mood function
        goodMood()
    else:
        # takes to get the user help needed
        badMood()


# very short function for defining the user in a good state of mind.
def goodMood():
    print("That's good! I am assuming everything is going well for you then!\n"
          "Keep up the good work!\n")
    input("Press Enter to Exit: ")


# Function to give suicide prevention resources to user if feelings get to this point
# Gives number and website information upon request
def suicideHelper():
    if ask("Would you like me to open 988lifeline.org now?\n").lower() in yes:
        webbrowser.open_new_tab("https://988lifeline.org/")
    print("Whatever you're going through, things can change, and people want to help you through it.\n"
          "Reaching out is a strong thing to do.\n")


# Bad mood function meant for the user to navigate when in need of support
def badMood():
    # Prompts the user if they would like to vent their stress.
    print("Oh, I'm sorry to hear. Would you like to vent?\n"
          "Venting is useful when you're in a bad state of mind.\n"
          "It's better to let stress out in a positive way, like writing or\n"
          "singing. So how about it? Would you like to type about it?\n"
          "I'm all ears!\n"
          "yes or no?")
    if ask().lower() in yes:
        vent()
        return
    # Alternatives to venting
    # area for offering information
    print("If no, then its okay. Any reason in particular you feel the way you feel?\n"
          "What's going on? I could be of some help, depending of what you need.\n"
          "Are you...(or feeling)\n"
          "Suicidal, depressing moments, no confidence?\n")
    reason = ask().lower()
    if is_crisis(reason):
        # ask() already showed the crisis resources; offer to open the site
        suicideHelper()
    elif "depress" in reason:
        # Attempts to get the user to show at least a bit of a smile
        print("We all have our ups and downs. Some of us may have it worse. Some of us may\n"
              "experience a close one's death, or maybe someone's house burned down. We\n"
              "all have horrid days, and some of us lives. Some people spend most of their\n"
              "teens being bullied only for being different. What makes all those people,\n"
              "including you, different are the fact you guys are fighters and come out\n"
              "doing better than ever. Don't give up! You should read these empowering quotes\n"
              "from the google search engine.")
        input("Press Enter: ")
        # Opens a new tab for positive quotes
        webbrowser.open_new_tab("https://www.google.com/search?tbm=isch&safe=active&q=quotes+on+never+giving+up")
        print("Hope this helped you feel a bit better!")
    elif "confide" in reason:
        # Serves to be a confidence booster
        print("We've all been to a point where we have lost ourselves.\n"
              "So, this motivational video from Will Smith should help.\n"
              "Watch it.")
        input("Press enter to open the video on YouTube.")
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=ft_DXwgUXB0")
    else:
        print("Well, it's okay. I understand if you don't trust me. All I want you to know\n"
              "is that I am here to listen.\n")
    # Asks the user to politely finish the program
    while "thank" not in ask("Type in \"Thank You\" to exit.\n").lower():
        pass
    print("You're welcome. Take care of yourself!")


# Lets the user type as much as they want, then offers to save it
def vent():
    print("I'm glad. You can start typing now.\n"
          "[Press Enter on an empty line when you're done]:")
    lines = []
    while line := ask():
        lines.append(line)
    if not lines:
        print("That's okay. Sometimes it's hard to find the words.")
        input("Press Enter: ")
        return
    # This is in case the user would like to save whatever they typed up
    if ask("Would you like to save your typing?\nYes or no?\n").lower() in yes:
        save("\n".join(lines) + "\n", ask("Title name? (optional)\n"))
    else:
        print("Alright. I'll see you soon then!")
        input("Press Enter: ")


def save(text, title):
    # Keeps only safe characters so any title works as a file name, and dates it so nothing is overwritten
    title = "".join(c for c in title if c.isalnum() or c in " -_").strip() or "vent"
    path = journal_dir / f"{datetime.now():%Y-%m-%d %H-%M-%S} {title}.txt"
    try:
        journal_dir.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")
    except OSError as error:
        # Never lose what the user wrote: show it back so they can copy it somewhere
        print(f"Sorry, I couldn't save your file ({error}). Here's what you wrote so you can copy it:\n\n{text}")
    else:
        # Thanks the user for self awareness
        print(f"Saved to {path}\n"
              "Thank you for dedicating time to yourself. You needed it.\n"
              "Hope you get better soon!")
    input("Press Enter. ")


# Runs the entire code
if __name__ == "__main__":
    main()
