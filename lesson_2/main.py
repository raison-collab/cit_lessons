def main():

    with open('students.txt', mode='r') as f:
        read_ = f.read()
        read_line_ = f.readline()
        read_lines_ = f.readlines()

    print('read', read_)
    print(read_line_)
    print(read_lines_)

# csv json

main()
