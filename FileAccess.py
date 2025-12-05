class FileAccess:
    def __init__(self, filepath, mode='r'):
        self.filepath = filepath
        self.mode = mode
       

    def print_file_contents(self):
        try:
            number = 0
            CHUNKSIZE = 1024
            with open(self.filepath, self.mode) as file:
               while contents:=file.read(CHUNKSIZE):
                   pos=contents.find("*",0)
                   while pos>=0:
                       number+=1
                       pos=contents.find("*",pos+1)
            #    for contents in file:
            #         # number+=contents.count("*")
            #         pos=contents.find("*",0)
            #         while pos>=0:
            #             number+=1
            #             pos=contents.find("*",pos+1)
            #             # print(f'{number} line -----------:{contents}')


               print(f'Total lines containing [*]: {number}')
        except FileNotFoundError:
            print(f"Error: The file {self.filepath} was not found.")
        except IOError:
            print(f"Error: Could not read the file {self.filepath}.")
if __name__ == "__main__":
    filepath = './data/demo_file.txt'
    file_access = FileAccess(filepath, 'r')
    file_access.print_file_contents()

    test="2123123"
    print(test.find("*"))