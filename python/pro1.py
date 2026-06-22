def logger(func):
    def wrapper():
        print("function executed started")
        func()
        print("function ended")
    return wrapper
@logger    
def save_data():
    print("data saved successfully in db ")
save_data()