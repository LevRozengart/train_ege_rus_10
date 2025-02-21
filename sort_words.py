import json
i_words = list()
e_words = list()
with open("i.txt", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip(",").split(", ")
        line = list(map(lambda x: x.replace("\n", ""), line))
        i_words.extend(line)
with open("e.txt", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip(",\n").split(", ")
        line = list(map(lambda x: x.replace("\n", ""), line))
        e_words.extend(line)
with open("bd.json", "w", encoding="utf-8") as file:
    json.dump({0: i_words, 1: [i for i in e_words if i]}, file, ensure_ascii=False, indent=2)
