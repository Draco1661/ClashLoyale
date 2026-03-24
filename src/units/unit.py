import os

class Unit:
    def __init__(self):
        list_files=os.listdir("definitions")
        for file in list_files:
            if file.endswith(".json"):
                self.fichier=list_files.index(file)

test1=Unit()
print(test1.fichier)