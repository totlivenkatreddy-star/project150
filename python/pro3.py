def logger(func):
    def wrapper(*args, **kwargs):
        print("getting details of employee")
        result= func(*args, **kwargs)
        print("employee detailes fetched")
        return result
    return wrapper
@logger
def employee_details(name, salary):
    return {"name": name,
            "salary":salary}
print(employee_details("venkat",100000))