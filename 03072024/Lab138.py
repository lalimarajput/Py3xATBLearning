
# How to write to a file
with open('TestData.txt','a') as file:
    file.write("Hello How are you")
    print("Hello How are you")
    file.close()