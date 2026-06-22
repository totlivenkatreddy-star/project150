# # # def decorator(func):
# # #     def additional_behaviour():
# # #         print("user entered details")
# # #         func()
# # #         print("loggedout")
# # #     return additional_behaviour    
# # # @decorator
# # # def login():
# # #     print("user logged in successfully")

# # # #login=decorator(login)
# # # login()
# # def decorator(func):
# #     def wrapper():
# #         print("card inserted in ATM")
# #         func()
# #         print("card removed in ATM")
# #     return wrapper    


# # def payment():
# #     print("payment completed")
# # payment=decorator(payment)  
# # payment()
# def decorator(func):
#     def wrapper():
#         print("database connection opened")
#         func()
#         print("database connection closed")
#     return wrapper

# def save_user():
#     print("User saved")
# save_user=decorator(save_user)
# save_user()    

