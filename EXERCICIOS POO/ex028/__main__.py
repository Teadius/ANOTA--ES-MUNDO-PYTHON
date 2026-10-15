from termostato import *
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 15
    inspect(t,private=True,methods=True)


if __name__ == "__main__":
    main()
