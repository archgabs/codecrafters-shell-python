import sys
import os
import subprocess

def main():
    valid_commands = ["echo", "exit", "type",]
    PATH = os.environ.get("PATH")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        cmd = input()
        
        match cmd.split(" ")[0]:
            case "exit":
                sys.exit(0)
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
                cmd_parts = cmd.split(" ")     # Divide o comando
                if len(cmd_parts) > 1:
                    executable = cmd_parts[0]       # Primeiro item é o executável
                    argument = cmd_parts[1]         # Segundo item é o argumento
                    paths = PATH.split(":")
                    
                    # Searchs for executable that matches the command name
                    for path in paths:
                        if os.path.isfile(f"{path}/{executable}"):
                            result = subprocess.run([f"{path}/{executable}", argument], shell=False, capture_output=True, text=True).stdout
                            break
                    
                    sys.stdout.write(result)
                else:
                    sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
