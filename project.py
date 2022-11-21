LANG = "EN"


def check_antwoord(antwoord):
    return antwoord == 42



def hello_world(lang):
    if lang == "NL":
        print("Hallo wereld!")
    elif lang == "FR":
        print("Bonjour le monde!")
    else:
        print("Hello world!")

hello_world("EN")

antwoord = input("Wat is het antwoord op de ultieme vraag van het leven, het universum, en alles?")
if check_antwoord(antwoord):
    print("Correct!")
else:
    print("Mogelijk heb je een andere vraag in je hoofd?")




def test():
    assert hello_world("NL") == "Hallo wereld!", "Test failed"

def main():
    print(hello_world(LANG))

#test()
main()




