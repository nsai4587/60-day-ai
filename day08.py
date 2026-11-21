# today's topic is how AI model reads the text and what is an AI model:
import random

#possible next words after "The patient feels.. "

words = ["better", "tried", "happy", "purple"]
chances = [60, 25, 14, 1]

def pick_word (temperature: float) -> str:
    adjusted = [c**(1 / temperature ) for c in chances]
    return random.choices(words, weights= adjusted)[0]

print("Low temperatuer (0.2):")
for i in range(5):
    print("  The patient feels", pick_word(0.2))
    
print("High temperature (2.0):")
for i in range(5):
    print("  The patient feels", pick_word(2.0))
    