browser = str(input("enter browser name\n"))
browser = browser.lower()   #to print in lower case
match browser:
    case "chrome":
        print("execute code of chrome browser")
    case "firefox":
        print("execute code of firefox browser")
    case _ :
        print("No browser found")