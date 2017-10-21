from aiotg import Bot, Chat
from db import KekDB
from typing import List


class QuoteManager(object):
    def __init__(self):
        """
        Load and preprocess quotes from db
        """
        self.db = KekDB()

        db_quotes = self.db.get_quotes_sync()
        self.quotes: List[dict] = list(filter(any, map(self.preprocess_quote, db_quotes)))

    def preprocess_quote(self, db_quote: dict) -> dict:
        """
        Check quotes from db, apply some default values, throw incorrect quotes
        """
        pass


class HistoryLogger(object):
    db = KekDB()

    @staticmethod
    def log(chat: Chat):
        """
        Prepare message and write it to db
        """
        chat_id = chat.id
        message = chat.message
        text = chat.message.get('text')
        sticker = chat.message.get('sticker')
        timestamp = chat.message['date']

        # anonymize
        message.pop('from')
        message.pop('chat')

        HistoryLogger.db.log_history(chat_id, message, text, sticker, timestamp)
