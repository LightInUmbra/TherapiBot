# Declare libraries/modules if any
import re
import unicodedata
import webbrowser
from datetime import datetime
from pathlib import Path

# Setting up arrays to scan words, kept in sync with index.html.
# English and Spanish are always checked together, since many people mix both.
# Spanish entries are written without accents because clean() removes them.
good = ["happy", "cheerful", "glad", "good", "great", "pleased", "thrilled", "blessed", "content", "joyful",
        "fine", "okay", "ok", "well",
        "bien", "feliz", "contento", "contenta", "alegre", "tranquilo", "tranquila", "genial", "excelente"]
bad = ["depressed", "sad", "upset", "suicidal", "worthless", "self harm", "selfharm", "down", "unhappy", "sorrow",
       "sorrowful", "troubled", "anxious", "anxiety attack", "anxiety", "bad", "awful", "terrible", "struggling",
       "mal", "triste", "deprimid", "ansios", "angustiad", "preocupad", "fatal", "horrible"]
negations = ["not", "no", "never", "isn't", "don't", "aren't", "wasn't", "nothing", "nunca", "nada", "ni"]
# Phrases that mean the user may be in danger; checked on EVERY answer.
# Covers how kids, teens and adults say it: slang ("kms", "unalive"), common misspellings,
# and phrases older adults often use ("I'm a burden", "tired of living").
crisis = ["suicid", "suicd", "sucid", "kill myself", "kms", "unalive", "end my life", "end it all",
          "want to die", "wanna die", "better off dead", "better off without me", "self harm", "selfharm",
          "self-harm", "hurt myself", "cut myself", "no reason to live", "no point in living", "no point living",
          "don't want to be here", "dont want to be here", "don't want to live", "dont want to live",
          "can't go on", "cant go on", "tired of living", "don't want to wake up", "dont want to wake up",
          "i'm a burden", "im a burden", "burden to everyone", "burden on everyone", "want to disappear",
          "matarme", "me quiero matar", "quitarme la vida", "acabar con mi vida", "acabar con todo",
          "quiero morir", "no quiero vivir", "no quiero seguir viviendo", "no vale la pena vivir",
          "mejor muerto", "mejor muerta", "estarian mejor sin mi", "hacerme dano", "lastimarme", "autolesion",
          "ya no puedo mas", "soy una carga", "no quiero despertar", "quiero desaparecer"]
yes = ["yes", "y", "ya", "yeah", "yea", "yep", "sure", "ok", "okay", "si", "claro", "vale", "dale", "sale"]
no = ["no", "n", "nope", "nah", "not really", "no im not", "no i am not", "im not", "nop", "nel", "para nada"]

# Vents are saved here, in the user's home folder, so they're easy to find again
journal_dir = Path.home() / "TherapiBot Journal"

# Wording follows 988 Lifeline, #BeThe1To and #chatsafe guidance (see README for sources)
# Kept to plain words so it works for anyone from age 10 to 60+
resources = ("  - Call or text 988 (US), or chat at chat.988lifeline.org\n"
             "    It's free, private and open 24/7, for any age. A trained counselor will listen.\n"
             "    You don't need to be in crisis or know exactly what to say.\n"
             "  - Veterans and service members: call 988 and press 1, or text 838255.\n"
             "  - Outside the US: findahelpline.com lists free helplines in your country.\n"
             "  - If you are in immediate danger or have hurt yourself, call 911 or your\n"
             "    local emergency number now.\n")
trusted_person = ("You could also talk to someone you trust: a parent or other family member, a\n"
                  "friend, a teacher or school counselor, a doctor, or a faith leader. If you're not\n"
                  "sure what to say, you could start with: \"I've been having a really hard time.\n"
                  "Can we talk?\"\n")
safety_plan = ("It can also help to make a safety plan: a short list of warning signs, things that\n"
               "help you cope, and people to call. The free Stanley-Brown Safety Plan walks you\n"
               "through it: sprc.org/resources/stanley-brown-safety-plan\n")


# main function where it will carry the code within all the code
def main():
    print("(If you are in crisis, call or text 988 in the US or visit findahelpline.com.\n"
          " In an emergency, call 911 or your local emergency number.)\n")
    try:
        welcome()
    except (KeyboardInterrupt, EOFError):
        print("\nTake care of yourself. You can come back anytime.")


def clean(text):
    # Lowercase, straight apostrophes, no accents: "Daño" -> "dano", "don’t" -> "don't"
    text = text.lower().replace("’", "'").replace("‘", "'")
    return unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode()


def is_crisis(text):
    text = clean(text)
    return any(phrase in text for phrase in crisis)


def is_good(mood):
    # "good" only counts if nothing bad or negated is mixed in ("not good", "good but anxious")
    mood = clean(mood)
    words = re.findall(r"[a-z']+", mood)
    return (any(word in good for word in words)
            and not any(word in negations for word in words)
            and not any(word in mood for word in bad))


def is_no(answer):
    # Only a clear "no" counts; "not sure", "maybe" or anything else is taken seriously
    return re.sub(r"[^a-z ]", "", clean(answer)).strip() in no


# Every question goes through here so a cry for help is never missed, no matter where it's typed
def ask(prompt=""):
    answer = input(prompt).strip()
    if is_crisis(answer):
        crisisHelp("It sounds like you might be going through something really painful.")
    return answer


# Connects the user with real people the moment they may be in danger
def crisisHelp(opening):
    print(f"\n{opening}\n"
          "You deserve support from a real person, and I'm only a program. Please reach out:\n"
          f"{resources}\n{trusted_person}")


# Welcome function in charge of guiding the user to however they feel.
def welcome():
    print("Hi, I'm TherapiBot.\n"
          "I'm a simple program, not a person or a therapist. I can't fix things, but I can\n"
          "give you a private place to sort through your thoughts, and point you toward\n"
          "real people who can help.\n")
    name = ask("What should I call you? (A nickname is fine, or just press Enter.)\n")
    # mood will determine feeling [state of mind] of user; will use arrays to find words similar to, if not the same
    mood = ask(("Thanks, " + name + "." if name else "Okay.") + " How are you feeling today?\n")
    if is_good(mood):
        goodMood()
    else:
        notGood()
        goodbye(name)


# very short function for defining the user in a good state of mind.
def goodMood():
    print("I'm glad to hear that. If a harder day comes, I'm here, and so are the\n"
          "counselors at 988 and findahelpline.com.\n")
    input("Press Enter to close.")


# Asks directly about suicide: asking does not put the idea in someone's head, and it can bring relief
def notGood():
    print("I'm sorry things are hard right now.")
    answer = ask("I ask everyone this, so please don't be alarmed: are you having any thoughts\n"
                 "of suicide or of hurting yourself? (yes / no / not sure)\n")
    if is_no(answer):
        print("Okay. Thank you for answering. I know it's a personal question.")
    else:
        if not is_crisis(answer):  # ask() already showed the resources if it was
            crisisHelp("Thank you for telling me. That takes courage, and I'm glad you did.")
        if ask("Would you like me to open the 988 chat in your browser? (yes / no)\n").lower() in yes:
            webbrowser.open_new_tab("https://chat.988lifeline.org/")
        print("I'm here while you reach out.")
    menu()


# Lets the user pick what would help, as many times as they like
def menu():
    while True:
        choice = ask("\nWhat would help most right now?\n"
                     "  1) Write about what's on my mind\n"
                     "  2) Calm my mind with a short exercise\n"
                     "  3) Find someone to talk to\n"
                     "  4) I'm done for now\n").lower()
        if choice.startswith("1") or "write" in choice:
            write()
        elif choice.startswith("2") or "calm" in choice:
            ground()
        elif choice.startswith("3") or "talk" in choice:
            talk()
        elif choice.startswith("4") or "done" in choice:
            return
        else:
            print("Sorry, I didn't catch that. You can type a number from 1 to 4.")


# Expressive writing: putting feelings into words can ease stress
def write():
    print("\nThis is your space. Write whatever is on your mind. Spelling and grammar don't\n"
          "matter, and no one else will see it. It can help to write about what happened\n"
          "and how it made you feel.\n"
          "[Press Enter on an empty line when you're done]")
    lines = []
    while line := ask():
        lines.append(line)
    if not lines:
        print("That's okay. Sometimes it's hard to find the words.")
        return
    print("Thank you for putting that into words. That isn't always easy.")
    # This is in case the user would like to save whatever they typed up
    if ask("Would you like to save what you wrote? It stays on this computer. (yes / no)\n").lower() in yes:
        save("\n".join(lines) + "\n", ask("Title name? (optional)\n"))


def save(text, title):
    # Keeps only safe characters so any title works as a file name, and dates it so nothing is overwritten
    title = "".join(c for c in title if c.isalnum() or c in " -_").strip() or "journal"
    path = journal_dir / f"{datetime.now():%Y-%m-%d %H-%M-%S} {title}.txt"
    try:
        journal_dir.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")
    except OSError as error:
        # Never lose what the user wrote: show it back so they can copy it somewhere
        print(f"Sorry, I couldn't save your file ({error}). Here's what you wrote so you can copy it:\n\n{text}")
    else:
        print(f"Saved to {path}")


# 5-4-3-2-1 grounding: brings attention back to the present when thoughts are racing
def ground():
    steps = ["Let's slow things down together. Take a slow breath in through your nose,\n"
             "and let it out slowly. When you're ready, name 5 things you can see.",
             "Good. Now 4 things you can feel, like your feet on the floor or your clothes.",
             "3 things you can hear.",
             "2 things you can smell. If nothing comes to mind, think of two smells you like.",
             "And 1 thing you can taste, or take one more slow, deep breath."]
    print()
    for step in steps:
        ask(step + "\n")
    if "better" in ask("Well done. How are you feeling now? (better / the same / worse)\n").lower():
        print("I'm glad. You can use this exercise anytime, anywhere.")
    else:
        print("That's okay. It doesn't always help right away, and that's not your fault.\n"
              "When feelings are this heavy, talking to someone can help.")


def talk():
    print(f"\nTalking to someone can help, even if you're not in crisis.\n{resources}\n{trusted_person}\n{safety_plan}")
    if ask("Would you like me to open the 988 chat in your browser? (yes / no)\n").lower() in yes:
        webbrowser.open_new_tab("https://chat.988lifeline.org/")


def goodbye(name):
    print(f"\nThank you for taking this time for yourself{', ' + name if name else ''}. Hard feelings can\n"
          "change, especially with support. You can come back anytime, and 988 is there 24/7.")
    input("Press Enter to close.")


# Runs the entire code
if __name__ == "__main__":
    main()
