from fastapi import APIRouter


router = APIRouter(
    
    tags=["Users"]
)


users = [
    {
        "id": 1,
        "name": "Venkat",
        "email": "venkat@gmail.com"
    },
    {
        "id": 2,
        "name": "Ravi",
        "email": "ravi@gmail.com"
    }
]


# GET ALL USERS
@router.get("/users/")
def get_users():

    return users



# GET SINGLE USER BY ID
@router.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:

        if user["id"] == user_id:
            return user


    return {
        "message": "User not found"
    }