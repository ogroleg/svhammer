# coding: utf-8
from __future__ import unicode_literals

token = '123456789:dfghdfghdflugdfhg-77fwftfeyfgftre'  # bot access_token
sn_stickers = ('CADAgADDwAu0BX', 'CAADA',
               'CDAgADEQADfvu0Bh0Xd-rAg', 'CAADAgAADfvu0Bee9LyXSj1_fAg',)  # ids
some2_stickers = ('CAADAKwADd_JnDFPYYarHAg', 'CAADAgADJmEyMU5rGAg')
allowed_stickers = sn_stickers + some2_stickers
default_probability = 0.01  # value hidden
del_symbols = '`~1234567890!@#'  # symbols to ignore
quotes_dict = {  # examples
    (0.6, 'університет', 'университет'): """ну що тут сказати
    цитата2
    @, що Ви мали на увазі?""",  # before sending @ will be replaced by username or name
    (0.75, sn_stickers): """стікер зі мною детектед
    а я непогайно тут виглядаю
    цитата3"""}
