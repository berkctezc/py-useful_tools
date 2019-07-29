import pyperclip as pc # for sending output to clipboard (install with pip)
import importlib

# Phone Number Formatter for Turkish Phone Numbers
## country = "+90"
## to do (add more countries)


def phoneFormatter(no):
    noReplaced = no.replace(" ", "").replace("(", "").replace(")", "")
    no = noReplaced

    #####
    if (no == "exit" or no == "quit" or no == "close"):  # exit
        print("Thanks for using my app. Exiting...")
        quit()
    elif (no == "reload" or no == "restart"):  # restart
        # to do (reloadding in python)
        print("App Reloaded")  # pseudo
    #####

    elif (no[0] == "+" and no[1] == "9" and no[2] == "0"):
        formattedNo = noReplaced
    elif (no[0] == "9" and no[1] == "0"):
        formattedNo = "+"+noReplaced
    elif (no[0] == "0"):
        formattedNo = "+9"+noReplaced
    else:
        formattedNo = "+90"+noReplaced

    pc.copy(formattedNo)
    print("Corrected Phone Number Copied To Your Clipboard")
    return formattedNo

# Title Case Name Formatter


def nameFormatter(name):
    # to do (gonna add regex)
    return name.title()


def main():
    counter = 0

    switch = input(
        "Type 'name' for NAME FORMATTING or 'phone' for PHONE FORMATTING: ")

    if (switch == "name"):
        print("--NAME FORMATTER--")

        while True:

            print("You have formatted", counter, "name(s) this session")
            counter += 1
            name = input("name: ")
            print(nameFormatter(name))

    elif (switch == "phone"):
        print("--PHONE FORMATTER--")

        while True:

            print("You have formatted ", counter, " number(s) this session")
            counter += 1
            no = input("phone: ")
            print(phoneFormatter(no))
    else:
        print("only 'name'/'phone' entries are accepted")


main()
