import random as rn
def read_file(filename):
    data_list=[]
    file=open(filename,"r")
    for line in file:
        data_list.append(line)
    file.close()
    return data_list
def getnum(l):
    x = rn.randint(0, (len(l) - 1))
    return x

def cont(l):
    answer = input("would you like to continue?, Yes or No").lower().strip()
    if answer == "yes":
        x=getnum(l)
        print(" another random name is " + l.pop(x))
        cont(l)
    elif answer == "no":
        print("Finished")
    else:
        print("Please type Yes or No")
        cont(l)

def main():
    list=read_file('names.txt')
    x=rn.randint(0, (len(list)-1))
    print("The first random name is " + list.pop(x))
    cont(list)

main()