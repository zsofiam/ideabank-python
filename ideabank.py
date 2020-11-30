import sys
""" print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: ", str(sys.argv))
print("Second argument:", sys.argv[1]) """


def main():
    if len(sys.argv) == 1:
        while True:
            new_idea = input("What is your new idea?")
            f = open("ideas.txt", "a")
            f.write("\n" + new_idea)
            f.close()
            print_lines_with_leading_numbers()
    elif len(sys.argv) == 2 and sys.argv[1] == "--list":
        f = open("ideas.txt", "r")
        lines = f.readlines()
        i = 1
        for line in lines:
            print(f'{i}. {line}')
            i += 1
        f.close()
    elif len(sys.argv) == 3 and sys.argv[1] == "--delete":
        f = open("ideas.txt", "r")
        lines2 = f.readlines()
        print(lines2)
        f.close()
        f = open("ideas.txt", "w")
        f.write('')
        f.close()
        lines2.pop(int(sys.argv[2])-1)
        f = open("ideas.txt", "a")
        for line in lines2:
            f.write(line)
        f.close()
        print_lines_with_leading_numbers()
    else:
        exit()


def print_lines_with_leading_numbers():
    f = open("ideas.txt", "r")
    lines = f.readlines()
    i = 1
    for line in lines:
        print(f'{i}. {line}')
        i += 1
    f.close()


if __name__ == '__main__':
    main()