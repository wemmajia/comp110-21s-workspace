"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Returns random fortune string."""
    fortune: str = ""
    x: int = randint(0, 3)
    if x == 0:
        fortune = "A beautiful, smart, and loving person will be coming into your life."
    else:
        if x == 1:
            fortune = "Your life will be happy and peaceful."
        else:
            if x == 2:
                fortune = "Soon life will become more interesting."
            else:
                fortune = "You will fail."
    return fortune

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
