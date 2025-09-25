class File():
    def gmailDoğrulama(self):
        with open("C:\\Users\\DELL\\Desktop\\MAİLLER.txt", "r", encoding="utf-8") as file:
            for satır in file:
                if(satır.endswith("@gmail.com\n")):
                    satır=satır.strip("\n")
                    print(satır)
                    print("****************************")

file=File()
file.gmailDoğrulama()

