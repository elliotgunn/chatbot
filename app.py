from flask import Flask, render_template, request
from chatterbot import Chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("ElliotBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
    inputtext = request.args.get("msg")
    return str(english_both.get_response(inputtext))

if __name__ == "__main__":
    app.run()
