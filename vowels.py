
def vowels(word):
    vowels = ['a','e','i','o','u']

    found = []
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    
    for l in found:
        print(l)

vowels("Milliways")