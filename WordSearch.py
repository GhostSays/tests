text = input("Insira o texto: ").upper()
keyword = input("Digite a palavra a ser procurada: ").upper()

keyword_widght = len(keyword)
text_widght = len(text)
cont = 0
i = 0

while i+keyword_widght <= text_widght:
    print(text[i:i+keyword_widght])
    if text[i:i+keyword_widght] == keyword:
        cont += 1
    i += 1
print(f"Há {cont} palavras {keyword.capitalize()} no texto inserido.")