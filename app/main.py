import sys


def main():
    sys.stdout.write("$ ")
    try:
        input()
    except:
        print("Command Not Found.")


if __name__ == "__main__":
    main()
