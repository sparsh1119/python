# def length(list):
#     count =0
#     for i in list:
#         count+=1
#     print(count)

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# list = [1,2,3,4,5,2]
# # length(list)
# # print_len(list)
# print_list(list)

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# factorial(6)

# def convert(n):
#     print(n*83)
# convert(1000)

# def type(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")

# n = int(input())
# type(n)

# def sum(n):
#     if(n==0):
#         return 0
#     return n+sum(n-1)

# print(sum(10))

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ['mango', 'apple', 'banana','litchi','blurberry']
print_list(fruits)
