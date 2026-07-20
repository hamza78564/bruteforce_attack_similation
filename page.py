#!/usr/bin/env python3
from flask import Flask, request, render_template_string
app =Flask(__name__)
login_html = '''
<form method="post" action="/login">
Password: <input type="password" name="password">
<input type="submit" value="Login">
</form>
'''

@app.route('/', methods=['GET'])
def index():
    return login_html
@app.route('/login', methods=['POST'])
def login():
    password= request.form.get('password')
    if password =='secret123':
        return 'Login Successful!'
    else:
        return 'Invaild Password', 401
if __name__ =='__main__':
    app.run(port=5000)