# print("Ans. 1")

# w="1234abcd"
# print(w[::-1])

# print("OR")

# def reverse(stng):
#     new =''
#     length=len(stng)

#     while length > 0:
#         new+=stng[length-1]
#         length=length-1
#     return new

# print(reverse("Consultadd"))


# print("Ans. 2")
# q=input("Enter any value")
# count=0
# count1=0

# for i in q:
#     if i.islower():
#         count+=1
#     if i.isupper():
#         count1+=1

# print("Total lowercases are = ", count)
# print("Total uppercases are = ", count1)

# print("Ans. 3")
# x=[12,23,12,45,45,67,83,"we","we","w2e"]
# q=set(x)
# print(q)

# print("Ans. 4")
# print("Enter a hyphen separated sequence of words:")
# lst=[n for n in input().split('-')]  
# lst.sort()
# print("Sorted:")
# print('-'.join(lst))

# print("Ans. 5")
# x=input("Enter a sentence").upper()
# print(x)

# print("Ans. 6")
# x=[1,2,3,4]
# y=[5,6,7,8]

# w=list(map(lambda x,y:x+y, x,y))
# print(w)

# print("Ans. 8")

# def ans():
#     x=[i**2 for i in range(1,21)]
#     print (x)

# ans()

# print ("OR")

# def is_even():
#     list1=[]
#     for i in range(1,20):
#             print(i**2)
#     return list1

# print (is_even())

# print ("Ans.10")
# r=range(0,21)
# e=filter(lambda r:r%2==0, r)
# print(list(e))

# print("Ans. 11")

# r=[1,2,3,4,5,6,7,8,9,10]
# print("list has been created by using filter:")

# q=list(filter(lambda r:r%2==0, r))
# print(q)

# print("result has been derived by using map:")
# e=list(map(lambda x:x**2, q))
# print(e)

# print("Ans. 12")

# while True:
#     try:
#         x=int(input("Enter any value"))
#         y=int(input("Enter any value"))
#         res=x/y
#         print(res)
#         if res==0:
#             break
#         else:
#             print("division is = ", res)
#     except:
#         print("ZeroDivisionError, Try again")

# print("Ans. 14")
# print("1.")
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# print("2.")
# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()

