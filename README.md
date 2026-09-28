# My Personal Notes
Thank you to everyone/anyone who stumbles across this tool. If you haven't seen my main GitHub page, my name is Umbra Ortiz. I developed this program back in 2010 as a kid learning about Python, the reality of our world, and the harshness that came with it.
It started out as a tool for myself as a kid in order to vent to something. Unfortunately, as a child, I didn't have what was necessary to get the help I needed nor did I have any friends to talk to. As time went on, I found myself to be in a constant state of negativity. I decided that I didn't want to stay in that, so I built a small little command line chat bot. It got me through some rough times and was able to help me vent to something, even though I knew no one was on the other end. At least I wasn't harbouring so much negativity in my heart. Over the years, I decided to polish this tool up for others to use, and eventually I used it for a hackathon. Some time later, I abandoned it and left it on my GitHub page. Revisiting it, I decided it needed a makeover. So, I gave it one. I hope this tool helps others the way it has helped me.

With that out of the way, here's the actual project notes:

# TherapiBot
This is a small chat bot I made using python to work under the command line. It opens as an EXE file format, and is used to provide help for the user whenever in a state of negativity.

The purpose of this "Chat Bot" is for the user to get help, as well as to express their emotions with the comfort of privacy; no one has to know what they express, and they choose whether they would like to save their "Venting Session" or not. If the user chooses not to disclose anything to the bot, there are pre-set options. This was made with the intention of people that are undergoing problems in relation to suicide, depression, and no self-confidence.

> **TherapiBot is a simple program, not a person or a therapist.** If you are in crisis, call or text **988** in the US, or find a free helpline in your country at **[findahelpline.com](https://findahelpline.com)**. If you are in immediate danger, call 911 or your local emergency number.

# What it does
TherapiBot is for anyone having a hard time, from kids around age 10 to adults 60 and older. It checks in on how you're feeling. If you're having a hard time, it asks directly whether you're having thoughts of suicide or self-harm, and connects you with real people if you are. Then it offers three things:
- **Write about it:** a private space to put your thoughts into words, which you can save if you want.
- **Calm my mind:** a short 5-4-3-2-1 grounding exercise.
- **Find someone to talk to:** what 988 and other helplines are like (including the Veterans Crisis Line), a simple way to start the conversation with someone you trust, and a link to a free safety plan.

The web version is in **English and Spanish**. It opens in Spanish on devices set to Spanish, or use **[TherapiBot en español](https://lightinumbra.github.io/TherapiBot/?lang=es)**. Crisis detection understands both languages in every conversation, since many people mix them.

On the web version, the **Leave quickly** button jumps to a neutral page, for anyone worried that someone will see their screen.

# Use it in your browser
**[Open TherapiBot](https://lightinumbra.github.io/TherapiBot/)** on any phone or computer, with nothing to install. Everything stays on your device: nothing you type is sent or stored anywhere, and saved writing downloads as a text file.

# Use it in the terminal
You need [Python 3.8 or newer](https://www.python.org/downloads/). Download `TherapIOT.py` and run:

```
python TherapIOT.py
```

Nothing is installed and nothing is sent anywhere. If you choose to save your writing, it goes into a `TherapiBot Journal` folder in your home folder, named with the date and time so older entries are never overwritten.

Whatever you type, TherapiBot watches for signs you might be in danger and shows crisis resources right away.

To check that crisis detection still works after changing the code, run `python test_TherapIOT.py`.

# History
Originally written in 2010 and updated over the years. Refreshed in 2026: the old 1-800 hotline was replaced with 988 and international resources, crisis detection now covers every answer instead of a single menu choice, venting takes any number of lines, and journal saving is safer. The wording was then rewritten to follow current suicide prevention guidance, and a web version was added.

# Why it says what it says
The wording follows published guidance. If you change it, please keep to these principles:
- **Ask about suicide directly.** Asking does not increase risk and may reduce suicidal thoughts. ([#BeThe1To](https://bethe1to.com/bethe1to-steps-evidence/))
- **Take it seriously, and never minimize or compare.** Avoid "at least..." and "others have it worse". ([#chatsafe](https://www.orygen.org.au/chat-safe/responding-to-someone-who-may-be-suicidal))
- **Focus on hope, actions and resources,** never on suicide itself. ([Action Alliance Framework for Successful Messaging](https://suicidepreventionmessaging.org/safety))
- **Explain what reaching out is like,** so it feels less scary: 988 is free, confidential, and not only for emergencies. ([988 Lifeline](https://988lifeline.org/get-help/what-to-expect/))
- **Offer coping strategies and people to contact,** the core of a safety plan. ([Stanley-Brown Safety Plan](https://sprc.org/resources/stanley-brown-safety-plan/), [grounding](https://www.nhsinform.scot/healthy-living/mental-wellbeing/breathing-and-relaxation-exercises/grounding-exercises/), [expressive writing](https://www.apa.org/news/podcasts/speaking-of-psychology/expressive-writing))
- **Use plain words that work for every age,** and recognize how different ages talk about suicide: kids and teens might say "kms" or "unalive", while older adults might say "I'm a burden" or "tired of living". When you add a phrase, add a test for it in `test_TherapIOT.py`.
- **Be honest that it's a program,** and point toward human care, not away from it. ([APA health advisory, 2025](https://www.apa.org/news/press/releases/2025/11/ai-wellness-apps-mental-health))
