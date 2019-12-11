# sessiyabot/core/online_monitor.py
# Monitor to plot statistics of users online
# Marakulin Andrey @annndruha
# 2019

import time
import datetime
import traceback

import psycopg2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from data import config
from func.database_functions import connection
from func.vkontakte_functions import vk


def day_plot(id):
    # Check user in members
    if not vk.method('groups.isMember', {'group_id':'sessiyabot', 'user_id':id}):
        raise KeyError('Member doesnt subscribe')

    # Load data from database
    with connection.cursor() as cur:
        cur.execute("select * from sessiyabot.day_bins where id =%s;", (id,))
        data = cur.fetchall()
    if len(data)<5:
        raise NameError('Small member data')

    # Parse data
    u_id, year, month, day, hour, sum_minutes = np.transpose(data)
    hours_bins = list(hour)
    sum_minutes = list(sum_minutes)
    hours_labels = list(map(str, map(int, hours_bins)))

    # Setting plot and update temp.png
    fig, axs = plt.subplots()
    axs.bar(hours_labels, sum_minutes, label = 'Статистика за последние сутки', align='edge', color='#8b00ff')
    axs.legend()

    plt.xticks(ticks=range(0,len(hours_labels)), labels = hours_labels,  size='small')
    plt.xlabel('Часы')
    plt.ylabel('Минут в сети')
    plt.xlim([0,len(hours_labels)])
    plt.savefig('data/temp.png', dpi=120, bbox_inches='tight')
    #plt.show()

    time_online = str(datetime.timedelta(minutes= int(sum(sum_minutes))))
    return 'За последние сутки вы были онлайн: '+ time_online.split(':')[0]+'ч '+time_online.split(':')[1]+'м'


def yesterday_plot(id):
    # Check user in members
    if not vk.method('groups.isMember', {'group_id':'sessiyabot', 'user_id':id}):
        raise KeyError('Member doesnt subscribe')

    # Load data from database
    with connection.cursor() as cur:
        cur.execute("select * from sessiyabot.yesterday_bins where id =%s;", (id,))
        data = cur.fetchall()
    if len(data)<5:
        raise NameError('Small member data')


    # Parse data
    u_id, year, month, day, hour, sum_minutes = np.transpose(data)
    hours_bins = list(hour)
    sum_minutes = list(sum_minutes)
    hours_labels = list(map(str, map(int, hours_bins)))

    # Setting plot and update temp.png
    fig, axs = plt.subplots()
    lbl = 'Статистика за '+str(int(day[0]))+'.'+str(int(month[0]))+'.'+str(int(year[0]))
    axs.bar(hours_labels, sum_minutes, label = lbl, align='edge', color='#8b00ff')
    axs.legend()
    plt.xticks(ticks=range(0,len(hours_labels)), labels = hours_labels,  size='small')
    plt.xlabel('Часы')
    plt.ylabel('Минут в сети')
    plt.xlim([0,len(hours_labels)])
    plt.savefig('data/temp.png', dpi=120, bbox_inches='tight')
    #plt.show()

    time_online = str(datetime.timedelta(minutes= int(sum(sum_minutes))))
    return 'Вчера вы были онлайн: '+ time_online.split(':')[0]+'ч '+time_online.split(':')[1]+'м'


def week_plot(id):
    # Check user in members
    if not vk.method('groups.isMember', {'group_id':'sessiyabot', 'user_id':id}):
        raise KeyError('Member doesnt subscribe')

    # Load data from database
    with connection.cursor() as cur:
        cur.execute("select * from sessiyabot.week_bins where id =%s;", (id,))
        data = cur.fetchall()
    if len(data)<3:
        raise NameError('Small member data')

    # Parse data
    u_id, year, month, day, sum_hours = np.transpose(data)
    days_bins = list(day)
    sum_hours = list(sum_hours)

    days_labels = []
    for i, d in enumerate(days_bins):
        days_labels.append(str(int(d))+'.'+str(int(month[i])))

    # Setting plot and update temp.png
    fig, axs = plt.subplots()
    axs.bar(days_labels, sum_hours, label = 'Статистика за последнюю неделю', color='#8b00ff')
    axs.legend()
    plt.xticks(ticks=range(0,len(days_labels)), labels = days_labels)
    plt.ylabel('Часов в сети')
    plt.savefig('data/temp.png', dpi=120, bbox_inches='tight')

    time_full = str(datetime.timedelta(hours= sum(sum_hours)))
    time_per_day = sum(sum_hours)/len(sum_hours)
    tpd = str(datetime.timedelta(hours= time_per_day))
    return 'За последнюю неделю вы бесполезно потратили: '+ time_full.split(':')[0]+'ч '+time_full.split(':')[1]+'м\nВ среднем в день: '+ tpd.split(':')[0]+'ч '+tpd.split(':')[1]+'м'

#day_plot(478143147)