import sys


def main():
    if len(sys.argv) == 1:
        while True:
            ask_for_new_idea()
    elif len(sys.argv) == 2 and sys.argv[1] == "--list":
        print_lines_with_leading_numbers()
    elif len(sys.argv) == 2 and sys.argv[1] == "--delete":
        print("Specify a number after --delete")
    elif len(sys.argv) == 3 and sys.argv[1] == "--delete" and sys.argv[2].isnumeric():
        lines2 = copy_content_into_list()
        check_if_correct(sys.argv[2], lines2)
        delete_line_from_file(lines2, sys.argv[2])
        print_lines_with_leading_numbers()
    elif len(sys.argv) == 3 and sys.argv[1] == "--delete" and not sys.argv[2].isnumeric():
        print("Specify a number after --delete")
    else:
        exit()


def copy_content_into_list():
    f = open("ideas.txt", "r")
    lines2 = f.readlines()
    f.close()
    return lines2


def delete_line_from_file(lines2, second_arg):
    f = open("ideas.txt", "w")
    f.write('')
    f.close()
    lines2.pop(int(second_arg)-1)
    f = open("ideas.txt", "a")
    for line in lines2:
        f.write(line)
    f.close()


def check_if_correct(second_arg, lines2):
    if int(second_arg) >= (len(lines2)-1) or int(second_arg) <= 0:
        exit()


def ask_for_new_idea():
    new_idea = input("What is your new idea?")
    f = open("ideas.txt", "a")
    f.write("\n" + new_idea)
    f.close()
    print_lines_with_leading_numbers()


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