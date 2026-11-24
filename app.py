from flask import Flask

app = Flask(__name__)

@app.get("/")
def inicio():
    return  {
        "mensagem": "API de chamados em funcionamento"        
    }


# uv run flask run