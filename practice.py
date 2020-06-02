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
#         if i.isdigit():
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#     return d

# print (check("janki12234"))

a,b =[1,2,3],[4,5,6]
print (a+b)
d=map(lambda a:a+=1, a+b)
list(d)
