# coding: utf-8
from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import requests
import time
import logging
import constants as c
from threading import Thread
from Queue import Queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Властелин здесь!')


def delete_thread_func():
    while True:
        msg = delete_queue.get()
        print 'deleting sticker:', msg['msg_id']
        if msg is None:
            break
        addr = 'https://api.telegram.org/bot%s/deleteMessage?chat_id=%s&message_id=%s' % (c.token,
                                                                                          msg['chat_id'],
                                                                                          msg['msg_id'])
        r = requests.post(addr)
        sleep_time = 0.5
        while r.status_code != 200:
            print 'fail:', msg['msg_id'], r.status_code
            r = requests.post(addr)
            time.sleep(sleep_time)
            if sleep_time<=5:
                sleep_time *= 2
        print 'success:', msg['msg_id']


delete_queue = Queue()
delete_thread = Thread(target=delete_thread_func)
delete_thread.start()


def sticker(bot, update):
    if update.message.chat.type == 'private':
        print(update.message.sticker.file_id)
    else:
        if update.message.sticker.file_id not in c.allowed_stickers:
            print(update.message.message_id)
            delete_queue.put({'chat_id': update.message.chat.id, 'msg_id': update.message.message_id})
        else:
            sticker = update.message.sticker.file_id
            r = random.random()
            res = None
            print r
            for x in c.quotes_dict:
                probability = x[0] if type(x[0]) is float else c.default_probability
                if probability >= r:
                    for var in filter(lambda t: type(t) is list or type(t) is tuple, x):
                        if sticker in var:
                            res = c.quotes_dict[x]
                            break
                if res:
                    break
            if res:
                return reply_some(res, bot, update, reply_enabled=False)


def text(bot, update):
    if update.message.chat.type == 'private':
        return
    else:
        text = update.message.text.lower().strip().replace('  ', ' ')
        for symbol in c.del_symbols:
            text = text.replace(symbol, '')
        r = random.random()
        res = None
        for x in c.quotes_dict:
            probability = x[0] if type(x[0]) is float else c.default_probability
            if probability >= r:
                for var in filter(lambda t: type(t) is str or type(t) is unicode, x):
                    if text == var or text.startswith(var + ' ') or text.endswith(' ' + var) or ' ' + var + ' ' in text:
                        res = c.quotes_dict[x]
                        break
            if res:
                break
        if res:
            return reply_some(res, bot, update)


def reply_some(reply, bot, update, reply_enabled=True):
    reply = reply.split('\n')
    reply = random.choice(reply).strip()
    if '@' in reply or not reply_enabled:
        bot.send_message(chat_id=update.message.chat.id,
                         text=reply.replace('@', update.message.from_user.name))
    else:
        update.message.reply_text(reply)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def error_callback(bot, update, error):
    print('telegramerror')


def main():
    updater = Updater(c.token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.sticker, sticker))
    dp.add_handler(MessageHandler(Filters.text, text))
    dp.add_error_handler(error_callback)

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()
    delete_queue.put(None)


if __name__ == '__main__':
    main()
