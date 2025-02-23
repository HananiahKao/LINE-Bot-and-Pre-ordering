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
    from MyFirstApp.lineMessages import createMessage, textMessage
    from DatabaseManager import DBManager
    if event.message.text == '將此群組設為管理者群組':
        if event.source.type == 'group':
            DBManager().write_value('admin_group_id', event.source.group_id)
            line_bot_api.push_message(event.source.group_id,textMessage('已將此群組設為管理者群組！'))
        else:
            line_bot_api.push_message(event.source.user_id,textMessage('這裡不是一個群組！'))

