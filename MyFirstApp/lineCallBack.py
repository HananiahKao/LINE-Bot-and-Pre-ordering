from MyFirstApp.lineMessages import createMessage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKKEN)
handler = WebhookHandler(settings.LINE_CHANNEKL_SECRET)
@csrf_exempt
def callBack(request):
    # get X-Line-Signature header value
    signature = request.headers['x-line-signature']

    # get request body as text
    body = request.body.decode('utf-8')
    print("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        #abort(400)
    return HttpResponse()
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text.endswith('tapping'):
        message_to_send=createMessage()
        line_bot_api.reply_message(event.reply_token,message_to_send)

