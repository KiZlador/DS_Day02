import sys
import os

class Research():

    def __init__(self, filename):
        self.f = filename

    def file_reader(self):

        if not os.path.exists(self.f):
            raise ValueError("File doesn't exists")
        
        with open(self.f, 'r') as file:
            lines = file.readlines()
            header = lines[0].strip().split(',')
            if header != "head,tail\n":
                raise ValueError("Wrong header format")

            for line in lines[1:]:
                if not (line == "0,1\n" or line == "1,0\n" or line == "0,1" or line == "1,0"):
                    raise ValueError("Wrong values")

            return(lines)

            

if __name__ == '__main__':
    r = Research(sys.argv[1])
    lines = r.file_reader()
    ans = ""
    for i in lines:
        ans += i
    print(ans)