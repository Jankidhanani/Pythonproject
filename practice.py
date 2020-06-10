# # # # x=int(input("Enter hours"))
# # # # if x<=40:
# # # #     x=x*12
# # # #     print(x)
# # # # elif x>40:
# # # #     x=(40*12)+((x-40)*(12*1.5))
# # # #     print (x)

# # # # student=int(input("Enter your credit"))
# # # # if student>=120:
# # # #     print("Congradulations! You have enought credit to graduate")
# # # # elif student<120:
# # # #     print("Sorry! You don't have enought credit to graduate now")

# # # # for i in range(1,12):
# # # #     if i%2==0:
# # # #         print(i)
# # # #         break
# # # # else:
# # # #     print("not printed")

# # # # def name12(fname):
# # # #     print( + "Dhanani")

# # # # name12("Janki ")
# # # # name12("Sapana ")
# # # # name12("Dhaval ")

# # # def add():
# # #     a,b = 2,3
# # #     print("result is ", a+b)

# # # add()

# # # def sub():
# # #     a,b = 2,3
# # #     res = a-b
# # #     print (res)

# # # sub()

# # f=[1,5,6,10,7,16]
# # for i in f:
# #     if i%2==0:
# #         print(i)
# # else:
# #     print("there is no odd number")

# # items = [25,26,27,28]
# # square=list(map(lambda x:x**2, items))
# # print(square)

# # from functools import reduce
# # def minus():
# #     er=reduce(lambda t,y:t-y,[34,76,90])
# #     print(er)
# # #     return er
# # # minus ()

# y="consultadd training"

# x=[i for i in y if i not in 'aeiou']
# print ("without vowels this string is: ", "".join(x))

# e=[r for r in y if r in 'aeiou']
# d={"".join(e)}
# print("Vowels in this string are: ",d)

# def add():
#     a,b=10,20
#     print (a+b)

# add()

# def check(t):
#     d={}
#     for i in t:
#         # if i.isdigit():
#         if i in d:
#             d[i]+=1
#             print("EVEN")
#         else:
#             d[i]=1
#     return d

# print (check("123"))

# a,b =[1,2,3],[4,5,6]
# print (a+b)
# d=map(lambda a:a+=1, a+b)
# list(d)

# print('hello!world')
# print("hello! again")
# print("yaaay! printing")
# print("happily printing")
# print('happily learning')
# print('123456qwert')
# print('4j+5')
# print("3.3")
# print("string, float, integer and complex")
# print("tuple","dictionary","string","list")
# print("I am determined in mastering Python")
# print("I am mastering 'Python'")

# x = ('hfjdakah')
# print (type(x))

# print("i have", 5+2*3, "jeans.")
# print('is 4+5>=3*2?')
# print (4+5>=3*2)

# print(73*5000)

# s=10
# x='nisarga'
# r=5j+9
# f=28.45
# print(r,x,f,s)
# driver=10
# plumber=20
# people_in_surat = "5mn"
# my_home="india"
# my_city="surat"
# my_fav_city="mumbai"
# date="2nd June 2020"
# print(my_city, my_fav_city,my_home,plumber,driver,people_in_surat)
# print("I am living in", my_city, "but my favourite city is", my_fav_city)
# workers=driver+plumber
# print(workers)

# dear=("Pari")
# years=3
# like = ("ice cream")

# print ("Her name is %s" %dear)
# print ("We have been knowing each other since %d years" %years)
# print("she likes %s all the time" %like)

# flowers=5
# candles=12
# cake=1
# beers=6
# wine=1
# pizza=3
# order=("veggie")
# desserts = ("cake")
# str1=("format string")

# print("I have ordered %r %r pizzas, %r of beer bottles, %r cake and %d for decoration" %(pizza, order, beers, cake,flowers+candles))
# print("this called as %s"%str1)
# print("I have %r cake." %cake)
# print("I have %s cake." %cake)
# print("I have %d cake." %cake)
# print("I have %r as a %r." %(cake, desserts))

# print("Marry had a little lamb.")
# print("His flees were as white as %s" %"snow")
# print("Anywhere marry went")
# print("." * 10)

# end1=("C")
# end2=("h")
# end3=("e")
# end4=("e")
# end5=("s")
# end6=("e")
# end7=("B")
# end8=("u")
# end9=("r")
# end10=('g')
# end11=('e')
# end12=("r")

# print (end1+end2+end3+end4+end5+end6), 
# print (end7+end8+end9+end10+end11+end12)

# formatter = "%r %r %r %r"
# print(formatter %(1,2,3,4))
# print(formatter %('true','false','true','false'))
# print(formatter %('head','tail','head','tail'))
# print(formatter %('printing','printing','printing','printing'))
# print(formatter %(formatter, formatter,formatter,formatter))
# print(formatter % (
#     "This is format string.",
#     "I am practicing to master it.",
#     "Printing, printing and printing",
#     "Coding, coding and coding"
# ))

# days =("\\nMon\nTue\nWed\nThur\nFri\nSat\nSun")
# months=("\nJan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug\nSept\nOct\nNov\nDec")
# print("These are %s : " %days)
# print("These are %s : " %months)

#triple double quotes together and it is giving result all three lines in seperate lines.
# print("""
#     i am going somewhere.
#     i am going for tracking.
#     i am going to measure peak by feet.
#     montains and sky attract me immenselly.
#     I feel worth to climb monutains as I feel it takes me nearer to sky.
# """)

# #doing double quotes to every single lines returning all lines in one line format.
# print(
#     "i am going somewhere.",
#     "i am going for tracking.",
#     "i am going to measure peak by feet."
# )

# print("I am 5\"3' tall")
# print('I am 5"3\' tall')

# if all value are correct and you want to quit the loop, enter break command 

# while True:
#     try:
#         q=int(input("Enter any value"))
#         w=int(input ("Enter any value"))
#         e=q+w
#         print("sum is = ", e)
#         break
#     except:
#         print("Enter only integer value")

# def min(x):
#     return x*2-4
# x=[3,4,5]
# e=map(min, x)
# print(list(e))
# print(min(x))
# der = map(min, [3,4,5])
# list(der)
# print(min(x))


d=[4,5,6]
r=[5,6,7]
t=[3,4,5]
# min=[]

# for i in d:
#     min.append (i-2)
# print(min)

# s=list (map(lambda x,y,t:x*y+t, d,r,t))
# print(s)

# K=filter(lambda x:x<=0, range(-10,10,2))
# print(list(K))

# from functools import reduce
# E=reduce(lambda r,t:r-t, [1,2,3,5,6,8,9])
# print(E)

# while True:
#     try:
#         int1=int(input("enter any value"))
#         int2=int(input("enter any value"))
#         res = int1+int2
#         print("addition is = ", res)
#         break
#     except Exception as e:
#         print(e)
#         print("enter only integer value")

# while True:
#     try:
#         s=int(input("enter any value"))
#         d=int(input("enter any value"))
#         res = s+d
#     except ValueError:
#         print("please enter only integer value")

#     except NameError:
#         print("please provide correct name")

#     else:
#         print(res)

# with open("data.txt",'a') as fh:
#     t=fh.write("practicing with block")
#     print (t)

# def revstr(string1):
#     return 
    
# i=input("Enter a string")
# e=i.split()
# # print (e)
# f=[i[::-1] for i in e]
# r=" ".join((f))
# print(r)

# di=open("data.txt","r")
# fi=di.read()
# ki=fi[1:150:2]
# print(ki)
# print(len(ki))

# f=input("enter a value")
# d=f.split()
# g=[i[::-1] for i in d]
# r=" ".join(g))
# print(r)

# try:
#     rd=open("data.txt","r")
#     op=rd.read()
#     print(op)

# except:
#     print("please give correct file name")

# finally:
#     rd.close()

from sys import argv
nameofprogram, filename = argv

# it's like x,y=10; we are providing same value to two variables

print("name of the program is ", nameofprogram)
print("name of the file is ", filename)

with open(filename) as gh:
    print (gh.read())
   