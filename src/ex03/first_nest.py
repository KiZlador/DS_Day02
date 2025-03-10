import sys 
import os

class Research():

    def __init__(self, filename):
        self.f = filename

    def file_reader(self, has_header = True):

        if not os.path.exists(self.f):
            raise ValueError("File doesn't exists")
        
        with open(self.f, 'r') as file:
            lines = file.readlines()
            if not has_header and (lines[0] != "0,1\n" and lines[0] != "1,0\n" and lines[0] != "1,1\n" and lines[0] != "0,0\n"):
                raise ValueError("Wrong header format")
            ans = []
            if has_header:
                lines = lines[1:]
            for line in lines:
                if not (line == "0,1\n" or line == "1,0\n" or line == "0,1" or line == "1,0"):
                    raise ValueError("Wrong values")
                ans.append(line.strip().split(','))
            return(ans)
    
    class Calculations():

        @staticmethod
        def counts(values):
            ans = [0, 0]

            for i in values:
                ans[0] += int(i[0])
                ans[1] += int(i[1])

            return ans
        
        @staticmethod
        def fractions(counts):
            ans = []
            ans.append(100*(counts[0]/(counts[0] + counts[1])))
            ans.append(100*(counts[1]/(counts[0] + counts[1])))
            return ans




if __name__ == '__main__':
    r = Research(sys.argv[1])
    f = open(sys.argv[1], 'r')
    prob_header = f.readline()
    f.close()
    c = r.Calculations()
    data = r.file_reader(has_header = (prob_header == "head,tail\n"))
    counts = c.counts(data)
    proc = c.fractions(counts)
    print(data)
    print(counts[0], counts[1])
    print(proc[0], proc[1])