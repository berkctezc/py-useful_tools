import pyperclip as pc #pip install pyperclip


def paragraphFormatter(string):
    stringReplaced = string.replace(chr(10), " ").replace(chr(13), " ")
    # ASCII(10)-> Line Feed (Linux,macOSX) / ASCII(13)-> Carriage Return (pre-macOSX)

    pc.copy(stringReplaced)
    print("Got rid of end lines | String copied to clipboard (to reset the clipboard press - )")
    return stringReplaced


def main():

    allparagraphs=""

    while True: 
        parag = input("paragraph: ")

        if parag == "-":
            parag.replace("-","")
            print("Clipboard reset")
            allparagraphs = ""
            
        allparagraphs = allparagraphs+" "+parag
        ret = paragraphFormatter(allparagraphs)
        #print(ret)
        


main()
