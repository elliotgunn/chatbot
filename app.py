from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# instantiate app
app = Flask(__name__)

elliot_bot = ChatBot("ElliotBot",
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     # database = mongodb_name,
                     database_uri = mongodb://heroku_12345678:random_password@ds029017.mLab.com:29017/heroku_12345678)

trainer = ChatterBotCorpusTrainer(elliot_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    """ Displays the index page accessible at '/'
    """
    return render_template("base.html")

@app.route("/get")
def get_response():
    input = request.args.get("msg")
    return str(elliot_bot.get_response(input))

if __name__ == "__main__":
    app.run()
