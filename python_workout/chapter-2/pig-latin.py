def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower()  in vowels:
        print(word + 'way')
        return f"{word}way"
    print(f"{word[1:]}{word[0]}ay")
    return f"{word[1:]}{word[0]}ay"


pig_latin('Python')
pig_latin('Animal')