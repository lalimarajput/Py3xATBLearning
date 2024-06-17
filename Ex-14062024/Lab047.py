for i in range(10):
    if i ==5:
        pass
    else:
        print(i)  #5 will be skipped

#and or

for i in range(1,10):
    if i%3==0: #rem=0
        print(i)
    else:
        print(i*2)