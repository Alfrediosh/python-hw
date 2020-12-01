my_text = open("text_1.txt", "w", encoding='utf-8')

line = " "
while line:
    line = input("введите текст или оставьте так: ")
    my_text.write(f"{line}\n") if line != ' ' else my_text.close()