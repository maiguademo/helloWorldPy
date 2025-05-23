from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola Mundo desde helloWorldPy en Railway!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

