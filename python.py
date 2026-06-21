# # # # def welcome():
# # # #     print("helllo welcome to the python ")

# # # # x= welcome() 
# # # # print(x)  

# # # def login():
# # #     print("loginn successfully"
# # #           )
# # # def run_function(a):
# # #     a()
    
# # # run_function(login)

# # def outer():
# #     def inner():
# #         print("inner inside")
# #     inner()
# # outer()        

# def main():
#     print("this is main function")

#     def display():
#         print("display")
#     display()
# main()   

def message():
    def inner():
        print(" python developer")
    return inner
x= message()
x()