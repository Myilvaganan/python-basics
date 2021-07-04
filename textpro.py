

def sentence_maker(phrase):
    interrogative = ("how", "when", "where", "why", "what")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)



result = []

while True:
    userInput = input("Say Something: ")
    if userInput == "\end":
        break
    else:
        result.append(sentence_maker(userInput))


print(" ".join(result))
