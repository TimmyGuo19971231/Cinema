import sys

import book
import group
import show


def get_files(filename) -> list:
    with open(filename,"r",encoding="utf-8") as file:
        return [i.rstrip("\n") for i in file.readlines()]


room1 = get_files("room1.txt")
room2 = get_files("room2.txt")
room3 = get_files("room3.txt")
movie1 = get_files("movie1.txt")
movie2 = get_files("movie2.txt")
movie3 = get_files("movie3.txt")

if sys.argv[2] == "--show" and len(sys.argv) == 4:
    show.main()
elif sys.argv[2] == "--book":
    book.main()
elif sys.argv[2] == "--group":
    group.main()