import sys
import os


def main():
    valid_commands = ["echo", "exit", "type",]
    PATH = os.environ.get("PATH")

    while True:
        sys.stdout.write("$ ")

        cmd = input()
        
        if cmd == "exit 0":
            break
        
        if cmd.startswith("type"):
            # Get the command after type
            usr_input = cmd.split(" ")[0]
            cmd = cmd.split(" ")[1]
            
            paths = PATH.split(":")
            cmd_path = None
            
            # Searchs for executable that matches the command name
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"

            if cmd in valid_commands:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
                continue
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
                continue 

            sys.stdout.write(f"{cmd}: not found\n") 
            continue

        if cmd[0:4] == "echo":
            sys.stdout.write(f"{cmd[5:]}\n") 
            continue

        sys.stdout.write(f"{cmd}: command not found\n") 


if __name__ == "__main__":
    main()
