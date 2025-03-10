class Must_read():
    
    def printf(self, file_name):
        with open(file_name, 'r') as file:
            print(file.read())


if __name__ == '__main__':
    first_class = Must_read()
    first_class.printf(input())