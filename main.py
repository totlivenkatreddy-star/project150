from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# SIMPLE SESSION STORE
sessions = {}

# -------------------------
# LOGIN PAGE (WITH CSS + FORGOT PASSWORD)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <html>
    <head>
        <title>Login</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                margin-top: 100px;
            }

            .box {
                background: white;
                padding: 30px;
                width: 300px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }

            input {
                width: 90%;
                padding: 10px;
                margin: 10px 0;
            }

            button {
                width: 100%;
                padding: 10px;
                background: green;
                color: white;
                border: none;
                cursor: pointer;
            }

            .forgot {
                display: block;
                margin-top: 10px;
                font-size: 14px;
                color: blue;
                text-decoration: none;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>Login</h2>
            <form action="/login" method="post">
                <input name="username" placeholder="Username"><br>
                <input name="password" type="password" placeholder="Password"><br>
                <button>Login</button>
            </form>

            <a class="forgot" href="/forgot-password">Forgot Password?</a>
        </div>
    </body>
    </html>
    """

# -------------------------
# LOGIN ACTION
# -------------------------
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):

    if username == "venkat" and password == "1234":
        sessions["user"] = username
        return RedirectResponse("/dashboard", status_code=302)

    return HTMLResponse("<h2>Login Failed ❌</h2><a href='/'>Try again</a>")


# -------------------------
# FORGOT PASSWORD PAGE
# -------------------------
@app.get("/forgot-password", response_class=HTMLResponse)
def forgot_password_page():
    return """
    <html>
    <head>
        <title>Forgot Password</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                margin-top: 100px;
            }

            .box {
                background: white;
                padding: 30px;
                width: 300px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }

            input {
                width: 90%;
                padding: 10px;
                margin: 10px 0;
            }

            button {
                width: 100%;
                padding: 10px;
                background: orange;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>Reset Password</h2>
            <form action="/send-reset-link" method="post">
                <input name="email" type="email" placeholder="Enter your email"><br>
                <button>Send Reset Link</button>
            </form>
        </div>
    </body>
    </html>
    """

# -------------------------
# SEND RESET LINK ACTION
# -------------------------
@app.post("/send-reset-link")
def send_reset_link(email: str = Form(...)):
    return HTMLResponse(f"""
        <h2>Reset Link Sent 📩</h2>
        <p>If this email exists: <b>{email}</b>, you will receive a reset link.</p>
        <a href="/">Back to Login</a>
    """)


# CHECK LOGIN
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
    <html>
    <head>
        <title>Dashboard</title>
        <style>
            body { margin:0; font-family:Arial; }

            .header {
                background:#2c3e50;
                color:white;
                padding:15px;
                display:flex;
                justify-content:space-between;
            }

            .menu a {
                color:white;
                margin:0 15px;
                text-decoration:none;
                font-weight:bold;
            }

            .content {
                text-align:center;
                margin-top:80px;
            }

            .card {
                display:inline-block;
                padding:20px;
                margin:10px;
                background:#f4f4f4;
                border-radius:10px;
                width:150px;
                cursor:pointer;
            }

            .footer {
                position:fixed;
                bottom:0;
                width:100%;
                background:#2c3e50;
                color:white;
                text-align:center;
                padding:10px;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <div><b>Dashboard</b></div>
            <div class="menu">
                <a href="/profile">👤 Profile</a>
                <a href="/orders">📦 Orders</a>
                <a href="/settings">⚙ Settings</a>
                <a href="/logout">🚪 Logout</a>
            </div>
        </div>

        <div class="content">
            <h1>Welcome Venkat 👋</h1>

            <a href="/profile"><div class="card">👤 Profile</div></a>
            <a href="/orders"><div class="card">📦 Orders</div></a>
            <a href="/settings"><div class="card">⚙ Settings</div></a>
        </div>

        <div class="footer">© 2026 FastAPI App</div>

    </body>
    </html>
    """


# PROFILE
@app.get("/profile", response_class=HTMLResponse)
def profile():
    if not check_login():
        return RedirectResponse("/")
    return "<h2>Profile 👤</h2><a href='/dashboard'>Back</a>"


# ORDERS
@app.get("/orders", response_class=HTMLResponse)
def orders():
    if not check_login():
        return RedirectResponse("/")
    return "<h2>Orders 📦</h2><a href='/dashboard'>Back</a>"


# SETTINGS
@app.get("/settings", response_class=HTMLResponse)
def settings():
    if not check_login():
        return RedirectResponse("/")
    return "<h2>Settings ⚙</h2><a href='/dashboard'>Back</a>"


# LOGOUT
@app.get("/logout")
def logout():
    sessions.clear()
    return RedirectResponse("/")