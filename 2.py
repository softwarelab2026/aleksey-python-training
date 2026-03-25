import sys

NAME = 1

def print_file_contents(file_name: str) -> None:
    with open(file_name, 'r') as file:
        print(*file, sep='')

def main():
    print_file_contents(sys.argv[NAME])

if __name__ == "__main__":
    main()
