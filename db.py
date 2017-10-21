import motor.motor_asyncio
from typing import Dict


class KekDB(object):
    def __init__(self):
        """
        Connect to MongoDB
        """
        self.client = motor.motor_asyncio.AsyncIOMotorClient()
        self.db = self.client['svh']

        self.quotes = self.db['quotes']

        self.quote_log = self.db['qlog']
        self.history_log = self.db['history']

    def close(self):
        """
        Close connection to MongoDB
        """
        self.client.close()

    def get_quotes_sync(self, options: dict = {}) -> list:
        """
        [blocking] Get all quotes from db or some of them filtered by options
        """
        cursor = self.quotes.find(options)
        return cursor.to_list()

    def log_quote(self, user_id: str, quote_id: str, timestamp: int):
        """
        Logs quote usage without caring about result
        :param user_id: user to whom quote applied
        :param quote_id: id of quote applied (see self.quotes collection)
        :param timestamp: when the quote was sent
        """
        self.quote_log.insert_one({
            'user': user_id,
            'quote': quote_id,
            'time': timestamp
        })

    def log_history(self, chat_id: int, message: dict, text: str, sticker: dict, timestamp: int):
        """
        Logs chat messages anonymously without caring about result
        Used to collect training data (to make bot more kekable)
        :param chat_id: chat where message sent
        :param message: raw message object
        :param text: message text
        :param sticker: raw sticker object
        :param timestamp: telegram time
        """
        self.history_log.insert_one({
            'chat': chat_id,
            'message': message,
            'text': text,
            'sticker': sticker,
            'time': timestamp
        })
