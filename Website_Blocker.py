import ctypes
import sys
import os


def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def blockIt(website):

    try:

        f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'a+')

        f.seek(0)
        contents = f.read()

        if(website in contents):
            print("Website Already Blocked!")
        else:
            local_host = "127.0.0.1"
            f.write("\n")

            if('www' in website):
                domain = website.replace('www.', '')
                f.write(local_host + " " + website + "\n")
                f.write(local_host + " " + domain + "\n")
            else:
                f.write(local_host + " " + website + "\n")
                f.write(local_host + " www." + website + "\n")

            print("Blocked")

        f.close()
        return True
    except:
        return False


def unblockIt(website):

    try:

        f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r+")
        content = f.read()
        f.close()

        if website in content:
            elem = content.split("\n")
            newElem = []

            for line in elem:
                if(website not in line):
                    newElem.append(line)

            finalContent = "\n".join(newElem)

            f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w+")
            f.write(finalContent)
            f.close()

            print("Website Unblocked Successfully\n")
        else:
            print("website is not in blocked list\n")

        return True

    except:
        return False


def main():

    if(not isAdmin()):
        print("Access Denied, Asking for permission")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    else:
        print("Website Blocker:\n\n")
        print("Enter a choice to continue:\n")
        choice = input("Block (1) / Unblock (2) ? : ")

        if(choice == '1'):
            web = input("Enter a website link to Block: ")

            if(not blockIt(web)):
                print("Error in blocking the website!")
                print("Please try again after some time..........")

        elif(choice == '2'):
            web = input("Enter a website link to Unblock: ")

            if(not unblockIt(web)):
                print("Error in Unblocking the website!")
                print("Please try again after some time..........")

        else:
            print("Wrong Choice!")
            print("Better Luck Next Time")

    os.system("pause")


if(__name__ == '__main__'):
    main()
