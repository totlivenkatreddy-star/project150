from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# -------------------------
# LOGIN PAGE
# -------------------------
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <html>
    <head>
        <title>Login</title>
        <style>
            body { font-family: Arial; text-align:center; background:#f2f2f2; margin-top:100px; }
            .box { background:white; padding:30px; width:300px; margin:auto; border-radius:10px; }
            input { width:90%; padding:10px; margin:10px; }
            button { width:100%; padding:10px; background:green; color:white; border:none; }
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
        </div>
    </body>
    </html>
    """

# -------------------------
# LOGIN CHECK
# -------------------------
@app.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):

    if username == "venkat" and password == "1234":
        return dashboard()

    return "<h2>Login Failed ❌ <a href='/'>Try again</a></h2>"


# -------------------------
# DASHBOARD PAGE
# -------------------------
def dashboard():
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
                cursor:pointer;
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
                cursor:pointer;
                width:150px;
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

# -------------------------
# PROFILE PAGE
# -------------------------
@app.get("/profile", response_class=HTMLResponse)
def profile():
    return """
    <h2>Profile 👤</h2>
    <p><b>Name:</b> Venkat Reddy</p>
    <p><b>Age:</b> 25</p>
    <p><b>Email:</b> venkat@gmail.com</p>
    <br>
    <a href="/login">Back</a>
    """

# -------------------------
# ORDERS PAGE
# -------------------------
@app.get("/orders", response_class=HTMLResponse)
def orders():
    return """
    <h2>Orders 📦</h2>
    <p>🕐 Pending Orders: 2</p>
    <p>✅ Delivered Orders: 3</p>
    <br>
    <a href="/login">Back</a>
    """

# -------------------------
# SETTINGS PAGE
# -------------------------
@app.get("/settings", response_class=HTMLResponse)
def settings():
    return """
    <h2>Settings ⚙</h2>

    <ul>
        <li>👤 Manage Profile</li>
        <li>💳 Payments</li>
        <li>📧 Change Email</li>
        <li>📱 Change Number</li>
        <li>🚪 Logout</li>
    </ul>

    <a href="/">Logout</a>
    """