# with open('note.txt','w') as file:
#     file.write(" hello..")

class ManagedFile:
    def __init__(self,filename):
        print("Init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("exit")
with ManagedFile('note.txt') as file:
    print(" do some task")
    file.write("I writing note in note,txt")