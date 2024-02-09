def spell_checker():
    user_input = input("Write text: ")
    words = user_input.split()
    with open("wordlist.txt") as tiedosto:
        for line in tiedosto:
            correct_word = line.strip()
            for i, word in enumerate(words):
                if word.lower() == correct_word.lower():
                    words[i] = correct_word if word.islower() else correct_word.capitalize()
                    break
    corrected_text = ' '.join(words)
    for word in words:
        if word.lower() not in [w.lower() for w in open("wordlist.txt").read().split()]:
            corrected_text = corrected_text.replace(word, f"*{word}*") 
    print(corrected_text)            
spell_checker()    