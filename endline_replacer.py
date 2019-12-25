import pyperclip as pc #pip install pyperclip


def paragraphFormatter(string):
    stringReplaced = string.replace(chr(10), " ").replace(chr(13), " ")
    # ASCII(10)-> Line Feed (Linux,macOS) / ASCII(13)-> Carriage Return

    pc.copy(stringReplaced)
    print("Got rid of end lines | String copied to clipboard (to reset the clipboard press - )")
    return stringReplaced


def main():

    allparagraphs=""

    while True: 
        parag = input("paragraph: ")
        allparagraphs = allparagraphs+" "+parag
        ret = paragraphFormatter(allparagraphs)
        #print(ret)
        if parag == "-":
            allparagraphs = ""


main()
