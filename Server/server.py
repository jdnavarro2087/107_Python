from flask import Flask

app = Flask(__name__) #name of folder

@app.get("/")
def home():
    return "hello from flask"


app.run(debug=True) #This applies changes to code, live
