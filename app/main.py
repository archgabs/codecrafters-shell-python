import sys


def main():
    valid_commands = ["echo", "exit", "type",]

    while True:
        sys.stdout.write("$ ")

        cmd = input()
        
        if cmd == "exit 0":
            break
        
        if cmd.startswith("type") and cmd[5:].strip() in valid_commands:
           sys.stdout.write(f"{cmd[5:].strip()} is a shell builtin\n")
           continue 

        if cmd[0:4] == "echo":
            sys.stdout.write(f"{cmd[5:]}\n") 
            continue

        sys.stdout.write(f"{cmd}: command not found\n") 


if __name__ == "__main__":
    main()
