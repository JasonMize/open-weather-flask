from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {
        "full_name": "Matt Smith",
        "username": "mattsmith1",
    }


    return """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello {full_name}</h1>
    <p>
        Your username is {username}
</body>
</html>
""".format(full_name=user["full_name"],
    username=user["username"])