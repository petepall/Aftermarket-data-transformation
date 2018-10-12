from easygui import fileopenbox, filesavebox

file_open: str = fileopenbox()
with open(file_open, 'r') as file_r:
    lines = file_r.readlines()

data: list = []
for line in lines[::-1]:
    word: list = line.split()

    if len(word) < 9:
        word.insert(3, "  ")

    newline = f"{word[0]:18}{word[1]:4}{word[2]:4}{word[3]:2}{word[4]:6}" \
        f"{word[5]:13}{word[6]:1}{word[7]:8}{word[8]:1}\n"
    data.append(newline)

header_line = (f"DMDUNIT           SALEPLANCOHISTSTQTY          "
               "TSTARTDATPERIOD\n")
file_save: str = filesavebox()
with open(file_save, 'w') as file_w:
    file_w.write(header_line)
    for line in data:
        file_w.write(line)
