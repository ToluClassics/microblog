from myapp import app

@app.route("/")
@app.route("/index")

def index():
    user = {'username':'Odunayo'}
    return '''
<html>
<head>
    <title></title>
</head>
<body>
    <h1>Hello, ''' + user['username'] + '''</h1>
</body
</html>
    '''