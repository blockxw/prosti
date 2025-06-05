vowels = "aeiouAEIOU"

text = input("Введи будь-який англійський текст: ")

vowel_letters = []
consonant_letters = []

for ch in text:
    if ch in vowels:
        vowel_letters.append(ch)
    elif ch.isalpha():
        consonant_letters.append(ch)

print("Голосні літери:", ''.join(vowel_letters))
print("Їх кількість:", len(vowel_letters))
print("Приголосні літери:", ''.join(consonant_letters))
