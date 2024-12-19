import sys


def main():
    sys.stdout.write("$ ")

    cmd = input()
    sys.stdout.write(f"invalid_command: {cmd} not found\n") 

if __name__ == "__main__":
    main()
