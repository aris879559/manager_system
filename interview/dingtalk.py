# -*- coding: utf-8 -*-
# @Author: wei
from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings

def send(messagge, at_mobiles=[]):
    #引用settings里面配置的钉钉群消息通知的webhook地址
    webhook = settings.DINGTALK_WEB_HOOK
    # secret = settings.DINGTALK_SECRET

    #初始化机器人小丁, 方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook)

    #方式二： 勾选“加签”选项时使用（v1.5以上新功能）
    # xiaoding = DingtalkChatbot(webhook, secret=secret)
    # xiaoding = DingtalkChatbot(webhook, access_token=access_token)

    #发送消息,@所有人,使用钉钉注册的手机号进行@
    xiaoding.send_text(msg=('面试通知： %s' % messagge), at_mobiles=at_mobiles)
