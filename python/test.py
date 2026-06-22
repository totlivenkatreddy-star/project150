# # # def outer():
# # #     def inner():
# # #         print("inner function")

# # #     inner()

# # #  outer()
# #========================================================
# # def outer():


# #     def inner():
# #         print("this is inner function")


# #     return inner()
# # result= outer()
# # print(result)    
# #==========================================================
# #decorators manually 

# def decorator(func):
#     def wrapper():
#         print("before functon")
#         func()
#         print("after function")
#     return wrapper


# def hello():
#     print("hello venkat")

# hello = decorator(hello)

# hello()
#=======================================================
