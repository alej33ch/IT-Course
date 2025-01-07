phrase = input("Enter a sentence:")
words = phrase.split()
print(f"The sentence has {len(words)} words.")


# Escribe un programa que cuente cuántas letras prohibidas hay en una frase. Las letras prohibidas son: a, u, i.
frase = input("Escribe una frase:")
palabrasProhibidas = "aui"

count= 0
for n in frase:
    if n in palabrasProhibidas:
        count += 1
print("Hay", count, "palabras prohibidas en la frase")
