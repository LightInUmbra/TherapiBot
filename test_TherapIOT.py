# Run with: python test_TherapIOT.py
from TherapIOT import is_crisis, is_good, is_no

# Crisis phrases must be caught anywhere in a sentence, any capitalization
for text in ["I feel suicidal", "i want to die", "Sometimes I think about SELF HARM", "I just wanna die lol",
             "everyone would be better off dead without me", "I've been thinking about suicide",
             # kids and teens
             "i want to kms", "thinking about how to unalive myself", "i feel sucidal", "I just want to disappear",
             # adults and older adults
             "I'm a burden to my family", "I'm tired of living", "I don't want to wake up tomorrow",
             "they'd be better off without me", "I can’t go on like this", "I don't want to be here anymore"]:
    assert is_crisis(text), text
for text in ["I'm tired", "school is hard", "I died laughing"]:
    assert not is_crisis(text), text

# Only clearly good moods skip the support path
for mood in ["good", "Great!", "pretty happy today", "fine"]:
    assert is_good(mood), mood
for mood in ["bad", "not good", "good but anxious", "I'm sad", "", "idk", "never been good"]:
    assert not is_good(mood), mood

# Only a clear "no" skips the crisis resources after asking about suicide
for answer in ["no", "No.", "nope", "No, I'm not", "not really"]:
    assert is_no(answer), answer
for answer in ["yes", "not sure", "maybe", "sometimes", "idk", "no... well, sometimes"]:
    assert not is_no(answer), answer

# Spanish, with or without accents
for text in ["Me quiero morir", "quiero matarme", "No quiero vivir más", "estoy pensando en el suicidio",
             "quiero hacerme daño", "quiero hacerme dano", "Soy una carga para mi familia", "ya no puedo más",
             "estarían mejor sin mí", "no quiero despertar mañana", "a veces quiero desaparecer"]:
    assert is_crisis(text), text
for text in ["estoy cansado", "la escuela está difícil", "me muero de risa"]:
    assert not is_crisis(text), text
for mood in ["Bastante bien", "feliz", "Estoy tranquila"]:
    assert is_good(mood), mood
for mood in ["No muy bien", "La estoy pasando muy mal", "triste", "estoy deprimida"]:
    assert not is_good(mood), mood
for answer in ["No", "para nada"]:
    assert is_no(answer), answer
for answer in ["Sí", "No sé", "tal vez"]:
    assert not is_no(answer), answer

print("All checks passed.")
