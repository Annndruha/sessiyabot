﻿# Sessiya_bot: chat_module - Text analysis engine
# Маракулин Андрей @annndruha
# 2019

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from data import config
from data import dictionary as dict
from func import chat_functions as chf
from core import keybords as kb


vk = vk_api.VkApi(token=config.access_token)# Auth with community token
longpoll = VkLongPoll(vk)# Create a longpull variable

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': vk_api.utils.get_random_id()})

def vk_user_get(user_id):
    return vk.method('users.get', {'user_ids': user_id})

def message_analyzer(user_id,request, user_first_name, user_last_name):
    try:
        request = (request).lower()
        l = len(request)
        if   (l <= 0):
            ans = dict.chat_ans[-1]
        elif (l > 299):
            ans = dict.chat_ans[-2]
        elif (l == 1):
            for keyword in dict.one_letter_word:
                if (request == keyword):
                    ans = dict.one_letter_word[keyword]
                else:
                    ans = dict.chat_ans[0]
        elif (l == 2):
            for keyword in dict.two_letter_word:
                if (request == keyword):
                    ans = dict.two_letter_word[keyword]
                else:
                    ans = dict.chat_ans[0]

        elif ((l > 2) and (l <= 299)):
            ans_exist = 0
            for keyword in dict.answer:
                if (request.find(keyword) >= 0):
                    ans = dict.answer[keyword]
                    ans_exist = 1
            for keyword in dict.functions:
                if (request.find(keyword) >= 0):
                    k = dict.functions[keyword]
                    if k == 0:
                        ans = chf.chat_sessiya_mesage(user_id)
                    if k == 1:
                        ans = chf.chat_time(user_id, request, user_first_name, user_last_name)
                    if k == 2:
                        ans = chf.chat_date(user_id, request, user_first_name, user_last_name)
                    if k == 3:
                        ans = chf.chat_stop(user_id, request)
                    if k == 4:
                        ans = chf.chat_tz(user_id, request, user_first_name, user_last_name)
                    if k == 5:
                        ans = dict.random_wish()
                    ans_exist = 1
            if ((ans_exist == 0) and (request.find('?') >= 0)):
                ans = dict.random_answer()
            elif ans_exist == 0:
                ans = chf.chat_find_in_wiki(user_id, request)
        return ans

    except:
        print('Chat module: Unknown exception')
        ans = dict.chat_ans[-3]
        return ans

def longpull_loop():
    while True:
        print('Chat module: Start')
        #try:
        kb.main_page(478143147, 'Главное меню:')
        for event in longpoll.listen():# Longpull loop
            if ((event.type == VkEventType.MESSAGE_NEW) and (event.to_me)):

                user_id = event.user_id
                message = event.text
                vk_user = vk_user_get(user_id)
                user_first_name = (vk_user[0])['first_name']
                user_last_name = (vk_user[0])['last_name']
                try:
                    payload = event.payload
                except:
                    payload = None

                if payload == None:
                    ans = message_analyzer(user_id, message, user_first_name, user_last_name)
                    write_msg(event.user_id, ans)
                else:
                    page = payload.split('"')[1]
                    argument = payload.split('"')[3]

                    if page == 'next_page':
                        if argument == 'notify_page':
                            kb.notify_page(user_id)
                        elif argument == 'month_page':
                            kb.month_page(user_id)
                        elif argument == 'day_page1':
                            kb.day_page1(user_id, argument)
                        elif argument == 'day_page2':
                            kb.day_page2(user_id, argument)
                        elif argument == 'day_page3':
                            kb.day_page3(user_id, argument)
                        elif argument == 'hour_page1':
                            kb.hour_page1(user_id)
                        elif argument == 'hour_page2':
                            kb.hour_page2(user_id)
                        elif argument == 'tz_page':
                            kb.tz_page(user_id)

                    elif page == 'hour_page':
                        kb.minute_page(user_id, argument)
                    elif page == 'minute_page':
                        ans = chf.chat_time(user_id, argument, user_first_name, user_last_name)
                        kb.main_page(user_id, ans)

                    elif (page == 'month_page'):
                        kb.day_page1(user_id, argument)
                    elif page == 'date_page':
                        print('eeeee')
                        kb.main_page(user_id, ans)
                    elif page == 'notify_page':
                        if argument == 'start':
                            ans = chf.chat_time(user_id, argument, user_first_name, user_last_name)
                        elif argument == 'stop':
                            ans = chf.chat_stop(user_id, argument)
                        kb.main_page(user_id, ans)
                    elif page =='tz_page':
                        ans = chf.chat_tz(user_id, argument, user_first_name, user_last_name)
                        kb.main_page(user_id, ans)
                    elif page =='cancel':
                        kb.main_page(user_id, 'Главное меню:')




        #except:
            #print('Longpull loop: Unknown exception')

longpull_loop()