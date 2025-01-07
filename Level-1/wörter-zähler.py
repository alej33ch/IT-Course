
# Schreibe ein Programm, das einen Text und ein Wort einliest und zählt, wie oft das Wort im Text vorkommt.
text = input("Schreib hier einen Text: ")
wort = input("Schreib hier das Wort zu zählen: ")

counter = text.lower().split().count(wort.lower())
print(f"Das Wort {wort} kommt {counter} mal vor.")


