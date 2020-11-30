def main():
    while True:
        new_idea = input("What is your new idea?")
        f = open("ideas.txt", "a")
        f.write("\n" + new_idea)
        f.close()
        f = open("ideas.txt", "r")
        lines = f.readlines()
        i = 1
        for line in lines:
            print(f'{i}. {line}')
            i += 1
        f.close()
    

if __name__ == '__main__':
    main()