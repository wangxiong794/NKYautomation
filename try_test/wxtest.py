# coding=utf-8
from wxpy import *
bot=Bot()
import Django
my_friend=bot.friends().search('敏敏')[0]
print(my_friend)