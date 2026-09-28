# TherapiBot
This is a small chat bot I made using python to work under the command line. It opens as an EXE file format, and is used to provide help for the user whenever in a state of negativity.

The purpose of this "Chat Bot" is for the user to get help, as well as to express their emotions with the comfort of privacy; no one has to know what they express, and they choose whether they would like to save their "Venting Session" or not. If they [The User] chooses not to disclose anything to the bot, there are preset options. This was made with the intention of helping college and high school students that are undergoing problems in relation to suicide, depression, and no self-confidence. This was only an idea I had for my local hackathon, and I do plan to update this chat bot and make it more useable. I hope this chat bot helps anyone that needs it. It isn't my best work, but I'm proud of it.

> **TherapiBot is a friendly listener, not a therapist.** If you are in crisis, call or text **988** in the US, or find a free helpline in your country at **[findahelpline.com](https://findahelpline.com)**. If you are in immediate danger, call your local emergency number.

# Use it in your browser
**[Open TherapiBot](https://lightinumbra.github.io/TherapiBot/)** on any phone or computer, with nothing to install. Everything stays on your device: nothing you type is sent or stored anywhere, and a saved vent downloads as a text file.

# Use it in the terminal
You need [Python 3.8 or newer](https://www.python.org/downloads/). Download `TherapIOT.py` and run:

```
python TherapIOT.py
```

Nothing is installed and nothing is sent anywhere. If you choose to save a vent, it goes into a `TherapiBot Journal` folder in your home folder, named with the date and time so older entries are never overwritten.

Whatever you type, TherapiBot watches for signs you might be in danger and shows crisis resources right away.

To check that crisis detection still works after changing the code, run `python test_TherapIOT.py`.

# History
Originally written in 2010 and updated over the years. Refreshed in 2026: the old 1-800 hotline was replaced with 988 and international resources, crisis detection now covers every answer instead of a single menu choice, venting takes any number of lines, and journal saving is safer.
