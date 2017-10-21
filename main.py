#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from aiotg import Bot, Chat

from models import HistoryLogger

import constants as c
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(api_token=c.TOKEN)


@bot.command("start")
def start(chat: Chat, match):
    """
    Hello, it's me!
    """
    if c.START_MSG:
        return chat.reply(c.START_MSG)


@bot.command("whoami")
def whoami(chat: Chat, match):
    """
    [For debug purposes only] Get telegram user id
    """
    if chat.type == "private":
        return chat.reply(chat.sender["id"])


@bot.command("source")
def source(chat: Chat, match):
    """
    Sends link to bot repository on github and so on
    """
    return chat.send_text(c.SOURCE_MSG)


@bot.handle("sticker")
def sticker(chat: Chat, sticker: dict):
    """
    Handle stickers
    In private chat: debug purposes only
    In groups: deletes some stickers (whitelist of stickersets), may react to usage of others
    """
    # HistoryLogger.log(chat)
    if chat.type == "private":
        return chat.reply(f"Sticker set: {sticker['set_name']}, sticker id: {sticker['file_id']}")
    if sticker['set_name'] not in c.ALLOWED_STICKERS:
        return bot.api_call('deleteMessage',
                            chat_id=chat.id,
                            message_id=chat.message['message_id'])

@bot.default
def text(chat: Chat, text: str):
    """
    Handle all text messages
    """
    # HistoryLogger.log(chat)
    pass


def main():
    """
    Go, go, go!
    """
    bot.run(debug=True)


if __name__ == '__main__':
    main()
