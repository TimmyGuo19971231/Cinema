import sys
import book
import group
import show


def error_mes():
    print("Sorry. This program does not recognise the switch options.\nBye.")
    sys.exit(1)


print("-=-=-=-=-=-=-=-=-=-=-=-=-=-="
      "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      "\n~ Welcome to Pizzaz cinema ~"
      "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
if sys.argv[1] == "--show":
    if len(sys.argv) == 3 and ":" in sys.argv[2]:
        show.main()
    else:
        print("Sorry. This program does not recognise the time format entered.\n\nBye.")
        sys.exit(1)
elif sys.argv[1] == "--book":
    book.main()
elif sys.argv[1] == "--group":
    group.main()
else:
    error_mes()
