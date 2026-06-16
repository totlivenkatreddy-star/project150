from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# -------------------------
# SIMPLE SESSION STORAGE
# -------------------------
sessions = {}

# -------------------------
# LOGIN PAGE
# -------------------------
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <h2>Login Page</h2>
    <form action="/login" method="post">
        <input name="username" placeholder="Username"><br><br>
        <input name="password" type="password" placeholder="Password"><br><br>
        <button>Login</button>
    </form>
    """

# -------------------------
# LOGIN ACTION (CREATE SESSION)
# -------------------------
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):

    if username == "venkat" and password == "1234":
        sessions["user"] = username
        return RedirectResponse("/dashboard", status_code=302)

    return HTMLResponse("<h3>Login Failed ❌</h3><a href='/'>Try again</a>")

# -------------------------
# CHECK LOGIN
# -------------------------
def check_login():
    return sessions.get("user")

# -------------------------
# DASHBOARD
# -------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    if not check_login():
        return RedirectResponse("/")

    return """
    <h2>Dashboard</h2>

    <a href="/profile">Profile</a> |
    <a href="/orders">Orders</a> |
    <a href="/settings">Settings</a> |
    <a href="/logout">Logout</a>

    <h3>Welcome Venkat 👋</h3>
    """

# -------------------------
# PROFILE
# -------------------------
@app.get("/profile", response_class=HTMLResponse)
def profile():
    if not check_login():
        return RedirectResponse("/")

    return """
    <h2>Profile 👤</h2>
    <p>Name: Venkat Reddy</p>
    <p>Age: 25</p>
    <p>Email: venkat@gmail.com</p>
    <a href="/dashboard">Back</a>
    """

# -------------------------
# ORDERS
# -------------------------
@app.get("/orders", response_class=HTMLResponse)
def orders():
    if not check_login():
        return RedirectResponse("/")

    return """
    <h2>Orders 📦</h2>
    <p>Pending: 2</p>
    <p>Delivered: 3</p>
    <a href="/dashboard">Back</a>
    """

# -------------------------
# SETTINGS
# -------------------------
@app.get("/settings", response_class=HTMLResponse)
def settings():
    if not check_login():
        return RedirectResponse("/")

    return """
    <h2>Settings ⚙</h2>
    <ul>
        <li>Manage Profile</li>
        <li>Payments</li>
        <li>Change Email</li>
        <li>Change Number</li>
        <li><a href="/logout">Logout</a></li>
    </ul>
    """

# -------------------------
# LOGOUT (CLEAR SESSION)
# -------------------------
@app.get("/logout")
def logout():
    sessions.clear()
    return RedirectResponse("/")