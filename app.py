from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# instantiate app
app = Flask(__name__)

elliot_bot = ChatBot("ElliotBot",
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     # database = mongodb_name,
                     database_uri = mongodb://heroku_0qzdzq26:2loj02asa4p59eql251u9r6780@ds013202.mlab.com:13202/heroku_0qzdzq26)

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
