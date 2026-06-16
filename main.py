from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# -------------------------
# 1. LOGIN PAGE (UI)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <h2>Login Page</h2>

    <form action="/login" method="post">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>
    """