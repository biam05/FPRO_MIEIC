from flask import Flask, request
from sympy import diff
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route("/")
def f1():
    return """<h1>Introduz codigo</h1>
<form action="/evaluation">
<textarea name="code" cols="80" rows="20"></textarea>
<input type="submit">
</form>
"""

@app.route("/evaluation")
def f2():
    code = request.args['code']
    myglobals = {}
    code = exec(code, myglobals)
    resultado = myglobals['f']()
    return str(resultado)

app.run()
