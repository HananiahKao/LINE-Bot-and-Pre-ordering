#TextSendMessage, MessageEvent, TextMessage, StickerSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate,
from linebot.models import TemplateSendMessage, URITemplateAction, CarouselTemplate, CarouselColumn
def createMessage():
        message_to_send=TemplateSendMessage(
alt_text='Carousel template...',
template=CarouselTemplate(
          columns=[
          CarouselColumn(
               thumbnail_image_url='https://sunny-artistic-snapper.ngrok-free.app/static/OriginePoundCake.png',
                title='磅蛋糕',
                text='簡樸經典的美味',
                actions=[
                URITemplateAction(
                label='預購',
                uri='https://liff.line.me/2006681612-1ZmrzVWm?selected=%E5%8E%9F%E5%91%B3'
                ),
                ]
                ),
          CarouselColumn(
               thumbnail_image_url='https://sunny-artistic-snapper.ngrok-free.app/static/PassionFruitPoundCake.jpg',
                title='百香果磅蛋糕',
                text='滿溢熱帶果香，濃郁柔滑，讓每一口都心動不已！',
                actions=[
                URITemplateAction(
                label='預購',
                uri='https://liff.line.me/2006681612-1ZmrzVWm?selected=%E7%99%BE%E9%A6%99%E6%9E%9C'
                ),
                ]
                ),
          CarouselColumn(
               thumbnail_image_url='https://sunny-artistic-snapper.ngrok-free.app/static/LemonPoundCake.jpg',
                title='檸檬磅蛋糕',
                text='以檸檬的清香搭配蛋糕紮實的口感，讓每一口充滿驚嘆！',
                actions=[
                URITemplateAction(
                label='預購',
                uri='https://liff.line.me/2006681612-1ZmrzVWm?selected=%E6%AA%B8%E6%AA%AC'
                ),
                ]
                ),
          CarouselColumn(
               thumbnail_image_url='https://sunny-artistic-snapper.ngrok-free.app/static/EarlGrayTeaPoundCake.jpeg',
                title='伯爵磅蛋糕',
                text='香濃的伯爵茶配上富有嚼勁的磅蛋糕，組合出無與倫比的下午茶最佳選擇',
                actions=[
                URITemplateAction(
                label='預購',
                uri='https://liff.line.me/2006681612-1ZmrzVWm?selected=%E4%BC%AF%E7%88%B5'
                ),
                ]
                ),
                ]))
        return message_to_send
