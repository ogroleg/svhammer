# coding: utf-8
from __future__ import unicode_literals

token = '123456789:dfghdfghdflugdfhg-77fwftfeyfgftre'  # bot access_token
sn_stickers = ('CADAgADDwAu0BX', 'CAADA',
               'CDAgADEQADfvu0Bh0Xd-rAg', 'CAADAgAADfvu0Bee9LyXSj1_fAg',)  # ids
some2_stickers = ('CAADAKwADd_JnDFPYYarHAg', 'CAADAgADJmEyMU5rGAg')
allowed_stickers = sn_stickers + some2_stickers
max_allowed_stickers_in_row = 3
default_probability = 0.01  # value hidden
del_symbols = '`~1234567890!@#'  # symbols to ignore
start_msg = 'я тут!'
source_msg = ''
min_sleep_time = 0.5
max_sleep_time = 5
sleep_multiplier = 2
quotes_dict = {  # examples
    (0.6, 'університет', 'университет'): """ну що тут сказати
    цитата2
    @, що Ви мали на увазі?""",  # before sending @ will be replaced by username or name
    (0.75, sn_stickers): """стікер зі мною детектед
    а я непогайно тут виглядаю
    цитата3"""}
