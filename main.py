#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from aiotg import Bot, Chat

import constants as c
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(api_token=c.TOKEN)


@bot.command("start")
def start(chat: Chat, match):
    if c.START_MSG:
        return chat.reply(c.START_MSG)


@bot.command("whoami")
def whoami(chat: Chat, match):
    if chat.type == "private":
        return chat.reply(chat.sender["id"])


@bot.command("source")
def source(chat: Chat, match):
    return chat.send_text(c.SOURCE_MSG)


@bot.handle("sticker")
def sticker(chat: Chat, sticker: dict):
    if chat.type == "private":
        return chat.reply(f"Sticker set: {sticker['set_name']}, sticker id: {sticker['file_id']}")
    elif sticker['set_name'] not in c.ALLOWED_STICKERS:
        return bot.api_call('deleteMessage',
                            chat_id=chat.id,
                            message_id=chat.message['message_id'])


def main():
    bot.run(debug=True)


if __name__ == '__main__':
    main()
