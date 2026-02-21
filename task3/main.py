from pathlib import Path
import sys
from colorama import init, Fore

# init colorama
init(autoreset=True)

def show_directory(path: Path, level: int = 0):
    # 1 space per level
    indent = " " * level  

    for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):

        if item.name.startswith("."):  # skip hidden (not sure if this is correct one)
            continue

        if item.is_dir():
            print(indent + Fore.YELLOW + f"📁 {item.name}")
            show_directory(item, level + 1)  # open directory

        elif item.is_file():
            print(indent + Fore.GREEN + f"📄 {item.name}")

        else:
            print(indent + Fore.MAGENTA + f"❓ {item.name}")


def main():
    # check if we have argv as a path
    if len(sys.argv) < 2:
        print(Fore.RED + "Please enter the path as an argument.")
        sys.exit(1)

    path_arg = sys.argv[1]
    path = Path(path_arg)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Directory {path} doesn't exist or is not a directory.")
        sys.exit(1)

    # display root
    print(Fore.CYAN + f"📦 {path.resolve()}\n")

    show_directory(path)


if __name__ == "__main__":
    main()