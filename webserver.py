
import flask
import os
app = flask.Flask(__name__)

debug = False

    

@app.route('/', methods=['GET'])
def index():
    return ('<h1>This is a website.</h1>')   



@app.route('/' + token, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "got Message bro"


@app.route('/hook')
def webhook():
    url = url
    bot.remove_webhook()
    bot.set_webhook(url + token)
    return f"Webhook set to {url}"


if debug == True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000))) 

