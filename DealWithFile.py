from docx import Document
import os
file = Document("D:\\GithubLocalRepo\\dictation\\WordLists.docx")
curentnum = 0
for line in file.paragraphs:
    list = line.text.split(' ')
    if(list[0] == "Word"):
        curentnum = list[2]
    else:
        if not line == "":
            fr = open("List{}.txt".format(str(curentnum)), "a")
            fr.write(line.text)
            fr.write('\n')
for i in range(35):
    filename = "List{}.txt".format(str(i+1))
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()