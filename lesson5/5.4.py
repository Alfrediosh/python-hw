from googletrans import Translator

with open("text_4_trans.txt", 'w', encoding='utf-8') as f:
    with open("text_4.txt", "r", encoding='utf-8') as f1:
        text = f1.read()
    f.write(Translator().trans(text, dest='ru').text)