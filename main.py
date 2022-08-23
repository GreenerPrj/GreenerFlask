from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask,request
from flask_cors import CORS,cross_origin
app = Flask('__name__')
CORS(app,resource={r"/api/*":{"origins":"*"}})
bot = ChatBot('chatterbot',storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

@app.route('/')
@cross_origin()
def Home():
    return str('Welcom Home')


@app.route('/user',methods=['POST']) # 접속하는 url
def user():
    jsony = request.json
    data = jsony['user_input']
    return str(bot.get_response(data))

if __name__=="__main__":
  app.run(host='127.0.0.1',port=8000,debug=True)