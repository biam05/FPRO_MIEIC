from flask import Flask, request
from sympy import diff
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route("/")
def f1():
    return """<h1>Calcular derivada</h1>
<form action="/derivada">
<input name="f">
<input type="submit">
</form>
"""

@app.route("/derivada")
def f2():
    f = request.args['f']
    f = parse_expr(f)
    df = diff(f)
    return str(df)

app.run()
