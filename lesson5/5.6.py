result = {}
with open("text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_timing = []
        lesson = ([el for el in line.split(" ")])
        for el in lesson:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)