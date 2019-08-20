﻿# sessiyabot/core/analyzer
# - longpoll chat, text anaizer engine and keybord browser
# Маракулин Андрей @annndruha
# 2019
import time
import traceback

import psycopg2

from data import dictionary as dict
from func import vkontakte_functions as vk
from func import datetime_functions as dt
from core import engine as eng
from core import keybords as kb

def message_analyzer(user):
    try:
        user.message = (user.message).lower()
        l = len(user.message)

        attach = None
        open_kb = False

        if   (l <= 0):
            ans = dict.errors['null_length']
        elif (l >= 300):
            ans = dict.errors['big_lenght']

        elif ((l == 1) or (l == 2)):
            for keyword in dict.small_message:
                if (user.message == keyword):
                    ans = dict.small_message[keyword]
                else:
                    ans = dict.errors['hm']
        elif ((l > 2) and (l < 300)):
            ans_exist = False
            for keyword in dict.answer:
                if (user.message.find(keyword) >= 0):
                    ans = dict.answer[keyword]
                    ans_exist = True
            for keyword in dict.hello:
                if (user.message.find(keyword) >= 0):
                    ans = dict.hello[keyword]
                    ans_exist = True
                    open_kb = True
            for keyword in dict.functions:
                if (user.message.find(keyword) >= 0):
                    k = dict.functions[keyword]
                    if k == 0:
                        ans = eng.sessiya_mesage(user)
                    if k == 1:
                        ans = eng.time(user)
                    if k == 2:
                        ans = eng.date(user)
                    if k == 3:
                        ans = eng.stop(user)
                    if k == 4:
                        ans = eng.tz(user)
                    if k == 5:
                        ans, attach = dict.cheer(user)
                    if k == 6:
                        ans, attach = dict.cheer(user, True)
                    ans_exist = True

            if ((ans_exist == False) and (user.message.find('?') >= 0)):
                ans = dict.random_answer()
            elif ans_exist == False:
                ans = dict.random_not_found()
                #ans = eng.find_in_wiki(user_id, user.message)
        if open_kb:
            kb.main_page(user.user_id, ans)
        else:
            vk.write_msg(user.user_id, ans, attach)
    except psycopg2.Error:
        raise err
    except OSError as err:
        raise err
    except BaseException as err:
        ans = dict.errors['im_broken']
        vk.write_msg(user.user_id, ans)
        print(str(time.strftime("---[%Y-%m-%d %H:%M:%S] Unknown Exception (message_analyzer), description:", time.localtime())))
        traceback.print_tb(err.__traceback__)
        print(str(err.args))