import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def show_dir_content(directory):
    try:
        path = Path(directory)
        if not path.is_dir():
            print(f"{Fore.RED}Error: {directory} is not a valid directory.")
            return

        print(f"{Fore.BLUE}Directory structure of {directory}:")
        for item in path.iterdir():
            if item.is_dir():
                print(f"{Fore.CYAN}[Dir] {item.name}")
            elif item.is_file():
                print(f"{Fore.GREEN}[File] {item.name}")

    except FileNotFoundError:
        print(f"{Fore.RED}Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
       path = sys.argv[1]
       show_dir_content(path)
    else:
       print(f"Usage: python {sys.argv[0]} <path>")