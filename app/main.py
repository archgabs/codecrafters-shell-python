import sys


def main():
    while True:
        sys.stdout.write("$ ")

        cmd = input()
        
        if cmd == "exit 0":
            break

        sys.stdout.write(f"{cmd}: command not found\n") 


if __name__ == "__main__":
    main()
