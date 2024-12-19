import sys
import os


def main():
    valid_commands = ["echo", "exit", "type",]
    PATH = os.environ.get("PATH")

    while True:
        sys.stdout.write("$ ")
        cmd = input()
        
        match cmd.split(" ")[0]:
            case "exit 0":
                break

            case "echo":
                sys.stdout.write(f"{cmd[5:].strip()}\n") 

            case "type":
                # Get the command after type
                usr_input = cmd.split(" ")[0]
                cmd = cmd.split(" ")[1]
                
                paths = PATH.split(":")
                cmd_path = None
                
                # Searchs for executable that matches the command name
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"

                # Tests if string it's a bultin program, else will write it's path
                if cmd in valid_commands:
                    sys.stdout.write(f"{cmd} is a shell builtin\n")
                    continue 

                if cmd_path:
                    sys.stdout.write(f"{cmd} is {cmd_path}\n")
                    continue 

                sys.stdout.write(f"{cmd}: not found\n") 
                

            case _:
                inputs = cmd.split(" ")
                sys.stdout.write(f"Hello {inputs[1]}! The secret code is {input[2]}.\n")  


if __name__ == "__main__":
    main()
