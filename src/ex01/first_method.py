class Research():

    def file_reader(self, filename):
        with open(filename, 'r') as file:
            return(file.read())


if __name__ == '__main__':
    r = Research()
    print(r.file_reader(input()))