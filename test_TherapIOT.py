# Run with: python test_TherapIOT.py
from TherapIOT import is_crisis, is_good, is_no

# Crisis phrases must be caught anywhere in a sentence, any capitalization
for text in ["I feel suicidal", "i want to die", "Sometimes I think about SELF HARM", "I just wanna die lol",
             "everyone would be better off dead without me", "I've been thinking about suicide"]:
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

print("All checks passed.")
