import time
from pygame import mixer
import datetime
import random

def func1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return func1(n-1)+func1(n-2)

def fun3(a):
    if a==0:
        return 1
    elif a==1:
        return a
    else:
        return fun3(a-1)*a
print('Welcome to python program')
while True:
    print('Press 1. for Dictionary ')
    print('Press 2. for Health-management')
    print('Press 3. for Random game')
    print('Press 4. for stone,papper and scissor')
    print('Press 5. for fabbonic series')
    print('Press 6. for Odd and even indicator ')
    print('Press 7. for factorial using recurison and alteration method')
    print('press 9 to exit') 

    # dictionary program

    num1=int(input('Enter your input: '))
    if num1==1:
        print('Welcome to python dictionary')   
        dict1={'democracy':'The place where the leader was elected by people','metal':'The substance which become positively charged by losing electrons','non-metal':'The substance which become negatively after gaing electrons','weathering':'The process of Fornmation of soil after a long-period of time','geography':'The study of earth and material presentin it',}
        print('Enter name to find answer')
        while True:
            print('democracy','metal','non-metal','geography','weathering')
            str1=str(input())
            if str1=='exit':
                break;
            else:
                print(dict1[str1])

    #   dictionary program end

    #   health management


    elif num1==2:
        print('welcome to health management')
        client=('nikhil','harry','rohan')
        str2=str(input("Enter your name: "))
        if str2=='harry':
            while True:
                print('Want you want to to ?')
                print('Meal')
                print('Exercise')
                print('exit')
                inp=str(input())
                if inp=='meal':
                    print('write what you eat')
                    meal=str(input())
                    with open('harry.txt','a') as hy:
                        hy.write(f'{datetime.datetime.now()}:{meal}\n')
                elif inp=='exercise':
                    print('write your exercise')
                    exe=str(input())
                    with open('harry-exe.txt','a') as hy:
                        hy.write(f"{datetime.datetime.now()}:{exe}\n")
                else:
                    print('thank for using')
                    break;
        elif str2=='nikhil':
            while True:
                print('Want you want to to ?')
                print('Meal')
                print('Exercise')
                print('exit')
                inp=str(input())
                if inp=='meal':
                    print('write what you eat')
                    meal=str(input())
                    with open('harry.txt','a') as hy:
                        hy.write(f'{datetime.datetime.now()}:{meal}\n')
                elif inp=='exercise':
                    print('write your exercise')
                    exe=str(input())
                    with open('harry-exe.txt','a') as hy:
                        hy.write(f"{datetime.datetime.now()}:{exe}\n")
                else:
                    print('thank for using')
                    break;
        elif str2=='rohan':
            while True:
                print('Want you want to to ?')
                print('Meal')
                print('Exercise')
                print('exit')
                inp=str(input())
                if inp=='meal':
                    print('write what you eat')
                    meal=str(input())
                    with open('harry.txt','a') as hy:
                        hy.write(f'{datetime.datetime.now()}:{meal}\n')
                elif inp=='exercise':
                    print('write your exercise')
                    exe=str(input())
                    with open('harry-exe.txt','a') as hy:
                        hy.write(f"{datetime.datetime.now()}:{exe}\n")
                else:
                    print('thank for using')
                    break;
        else:
            print('you are not in python gym')

    elif num1==3:
        print('welcome to python random-game')
        a1=random.randint(1,10)
        i=0
        while i<=10:
            a2=int(input('Enter your input: '))
            if a2>a1:
                print('your input is very larger please try smaller interger')
            elif a2<a1:
                print('your input is small please try large integer ')
            else:
                print('your input is match you win')
                break;
            i=i+1


    elif num1==4:
        print('welcome to python stone,papper and scissor')
        computer_choice=['stone','papper','scissor']
        i=0
        c=0
        u=0
        while i<=10:
            com= random.choice(computer_choice)
            user=str(input('Enter: '))
            print(com)
            if com=='stone' and user=='papper':
                u=u+1
            elif user=='stone' and com=='papper':
                c=c+1
            elif com=='scissor' and user=='papper':
                c=c+1
            elif com=='papper' and user=='scissor':
                u=u+1
            elif com=='stone' and user=='scissor':
                c=c+1
            elif com=='scissor' and user=='stone':
                u=u+1
            elif com=='stone' and user=='stone':
                c=c+1
                u=u+1
            elif com=='papper' and user=='papper':
                c=c+1
                u=u+1
            elif com=='scissor' and user=='scissor':
                c=c+1
                u=u+1
            else:
                print('please try again')
            i=i+1
        if u>c:
            print('you won')
        elif c>u:
            print('you lost')
        else:
            print('match tie')
    elif num1==5:
        print('welcome to python fibbonic series')
        i=int(input('Enter your number: '))
        print(func1(i))
    elif num1==6:
        print('welcome tp python odd and even indicator')
        o=int(input('Enter your number: '))
        if o%2==0:
            print('Even number')
        else:
            print('Odd number')
        a=input()
        
    elif num1==7:
        print('factorial using recurison and alteration method')
        user=int(input('enter your interger to find fatorial: '))
        factorial=1
        for i in range(1,user+1):
            factorial=factorial*i
        print(factorial)
        print(fun3(user))

    else:
        break;