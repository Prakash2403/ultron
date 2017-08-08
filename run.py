#!  /usr/bin/python3
from default_settings import default_settings
from ultron_cli import UltronCLI

if __name__ == '__main__':
    default_settings()
    try:
        UltronCLI().cmdloop()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        print("Goodbye")
        exit(0)
