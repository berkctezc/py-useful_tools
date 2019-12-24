import pyperclip as pc
import importlib


def paragraphFormatter(string):
    stringReplaced = string.replace(chr(10), " ").replace(chr(13), " ").replace('\\n', ' ')

    pc.copy(stringReplaced)
    print("Corrected String copied to clipboard")
    return stringReplaced

def main():
    
    allparagraphs=" "

    while allparagraphs!="":
        allparagraphs = allparagraphs+" "+input("paragraph: ")
        ret=paragraphFormatter(allparagraphs)
        print(ret)

main()
