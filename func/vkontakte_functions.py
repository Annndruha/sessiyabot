# sessiyabot/func/vk_functions
# - vk functions
# Marakulin Andrey @annndruha
# 2019
import time
import datetime

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
from vk_api.utils import get_random_id

from data import config
from data import ru_dictionary as dict

vk = VkApi(token=config.access_token)# Auth with community token
longpoll = VkLongPoll(vk)# Create a longpull variable
class User:
    def __init__(self, user_id, message, first_name, last_name):
        self.user_id = user_id
        self.message = message
        self.first_name = first_name
        self.last_name = last_name

# Use in notify message to protect user from two notify messages in the same
# minute
def datetime_to_random_id():
    delta = datetime.timedelta(hours = 3) # MoscowUTC
    tzone = datetime.timezone(delta)
    now = datetime.datetime.now(tzone)
    i = datetime.datetime.strftime(now, '%y%m%d%H%M')
    return int(i)

def reconnect():
    global vk
    global longpoll
    vk = VkApi(token=config.access_token)
    longpoll = VkLongPoll(vk)

def user_get(user_id):
    return vk.method('users.get', {'user_ids': user_id})

def write_msg(user_id, message=None, attach=None, parse_links = False):
    params = {'user_id': user_id, 'random_id': get_random_id()}

    if message is not None and attach is not None:
        params['message']=message
        params['attachment']=attach
    elif message is not None and attach is None:
        params['message']=message
    elif message is None and attach is not None:
        params['attachment']=attach
    if parse_links == False:
        params['dont_parse_links']=1

    vk.method('messages.send', params)

def write_notify_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': datetime_to_random_id()})

def send_keyboard(user_id, kb, message):
    vk.method('messages.send', {'user_id': user_id, 'keyboard': kb, 'message': message, 'random_id': get_random_id()})

# Sending message to admin when followers count change: Followers monitor
members_ids = None
members_count = None
def get_members():
    global members_ids
    global members_count
    members = vk.method('groups.getMembers', {'group_id':'sessiyabot'})
    members_count = int(members['count'])
    members_ids = members['items']

def update_members():
    global members_ids
    global members_count
    members = vk.method('groups.getMembers', {'group_id':'sessiyabot'})
    new_members_count = int(members['count'])

    if members_count > new_members_count:
        new_ids = members['items']
        ex = False
        i = 0
        while i <= new_members_count and ex == False:
            if new_ids[i] != members_ids[i]:
                user = user_get(members_ids[i])
                message = '&#10006; Отписался: [id' + str(members_ids[i]) + '|' + (user[0])['first_name'] + ' ' + (user[0])['last_name'] + ']\nЧисло ботающих: ' + str(new_members_count)
                write_msg(478143147,message)
                write_msg(members_ids[i], dict.other['unfollow'])
                ex = True
            i+=1
        members_count = new_members_count
        members_ids = members['items']

    if members_count < new_members_count:
        new_ids = members['items']
        ex = False
        i = 0
        while i <= members_count and ex == False:
            if new_ids[i] != members_ids[i]:
                user = user_get(new_ids[i])
                message = '&#10133; Новый подписчик: [id' + str(new_ids[i]) + '|' + (user[0])['first_name'] + ' ' + (user[0])['last_name'] + ']\nЧисло ботающих: ' + str(new_members_count)
                write_msg(478143147,message)
                ex = True
            i+=1
        members_count = new_members_count
        members_ids = members['items']

def followers_monitor():
    time.altzone = 3
    while True:
        get_members()
        print(str(time.strftime("===[%Y-%m-%d %H:%M:%S] FOLLOWERS MONITOR START", time.gmtime())))
        try:
            while True:
                update_members()
                time.sleep(20)
        except BaseException as err:
            print(str(time.strftime("---[%Y-%m-%d %H:%M:%S] BaseException (followers_monitor), description:", time.gmtime())))
            print(err.args)
            time.sleep(120)