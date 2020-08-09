#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict


_ARTICLES_RU = {}


_NUM_STRING_RU = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто'
}


_FRACTION_STRING_RU = {
    2: 'половина',
    3: 'третья',
    4: 'четвёртая',
    5: 'пятая',
    6: 'шестая',
    7: 'седьмая',
    8: 'восьмая',
    9: 'девятая',
    10: 'десятая',
    11: 'одиннадцатая',
    12: 'девнадцатая',
    13: 'тринадцатая',
    14: 'четырнадцатая',
    15: 'пятнадцатая',
    16: 'шестнадцатая',
    17: 'семнадцатая',
    18: 'восемндцатая',
    19: 'девятнадцатая',
    20: 'двадцатая'
}


_LONG_SCALE_RU = OrderedDict([
    (100, 'сто'),
    (1000, 'тысяча'),
    (1000000, 'миллион'),
    (1e12, "миллиард"),
    (1e18, 'триллион'),
    (1e24, "квадриллион"),
    (1e30, "квинтиллион"),
    (1e36, "секстиллион"),
    (1e42, "септиллион"),
    (1e48, "октиллион"),
    (1e54, "нониллион"),
    (1e60, "дециллион"),
    (1e66, "ундецеллион"),
    (1e72, "дуодециллион"),
    (1e78, "тредециллион"),
    (1e84, "кваттордециллион"),
    (1e90, "квиндециллион"),
    (1e96, "сексдециллион"),
    (1e102, "септдециллион"),
    (1e108, "октодециллион"),
    (1e114, "новемдециллион"),
    (1e120, "вигинтиллион"),
    (1e306, "unquinquagintillion"),
    (1e312, "duoquinquagintillion"),
    (1e336, "sesquinquagintillion"),
    (1e366, "unsexagintillion")
])


_SHORT_SCALE_RU = OrderedDict([
    (100, 'сто'),
    (1000, 'тысяча'),
    (1000000, 'миллион'),
    (1e9, "миллиард"),
    (1e12, 'триллион'),
    (1e15, "квадриллион"),
    (1e18, "квинтиллион"),
    (1e21, "секстиллион"),
    (1e24, "септиллион"),
    (1e27, "октиллион"),
    (1e30, "нониллион"),
    (1e33, "дециллион"),
    (1e36, "ундецеллион"),
    (1e39, "дуодециллион"),
    (1e42, "тредециллион"),
    (1e45, "кваттордециллион"),
    (1e48, "квиндециллион"),
    (1e51, "sedecillion"),
    (1e54, "septendecillion"),
    (1e57, "octodecillion"),
    (1e60, "novendecillion"),
    (1e63, "vigintillion"),
    (1e66, "unvigintillion"),
    (1e69, "uuovigintillion"),
    (1e72, "tresvigintillion"),
    (1e75, "quattuorvigintillion"),
    (1e78, "quinquavigintillion"),
    (1e81, "qesvigintillion"),
    (1e84, "septemvigintillion"),
    (1e87, "octovigintillion"),
    (1e90, "novemvigintillion"),
    (1e93, "trigintillion"),
    (1e96, "untrigintillion"),
    (1e99, "duotrigintillion"),
    (1e102, "trestrigintillion"),
    (1e105, "quattuortrigintillion"),
    (1e108, "quinquatrigintillion"),
    (1e111, "sestrigintillion"),
    (1e114, "septentrigintillion"),
    (1e117, "octotrigintillion"),
    (1e120, "noventrigintillion"),
    (1e123, "quadragintillion"),
    (1e153, "quinquagintillion"),
    (1e183, "sexagintillion"),
    (1e213, "septuagintillion"),
    (1e243, "octogintillion"),
    (1e273, "nonagintillion"),
    (1e303, "centillion"),
    (1e306, "uncentillion"),
    (1e309, "duocentillion"),
    (1e312, "trescentillion"),
    (1e333, "decicentillion"),
    (1e336, "undecicentillion"),
    (1e363, "viginticentillion"),
    (1e366, "unviginticentillion"),
    (1e393, "trigintacentillion"),
    (1e423, "quadragintacentillion"),
    (1e453, "quinquagintacentillion"),
    (1e483, "sexagintacentillion"),
    (1e513, "septuagintacentillion"),
    (1e543, "ctogintacentillion"),
    (1e573, "nonagintacentillion"),
    (1e603, "ducentillion"),
    (1e903, "trecentillion"),
    (1e1203, "quadringentillion"),
    (1e1503, "quingentillion"),
    (1e1803, "sescentillion"),
    (1e2103, "septingentillion"),
    (1e2403, "octingentillion"),
    (1e2703, "nongentillion"),
    (1e3003, "millinillion")
])


_ORDINAL_BASE_RU = {
    1: 'первый',
    2: 'второй',
    3: 'третий',
    4: 'четвёртый',
    5: 'пятый',
    6: 'шестой',
    7: 'седьмой',
    8: 'восьмой',
    9: 'девятый',
    10: 'десятый',
    11: 'одиннадцатый',
    12: 'двенадцатый',
    13: 'тринадцатый',
    14: 'четырнадцатый',
    15: 'пятнадцатый',
    16: 'шестнадцатый',
    17: 'семнадцатый',
    18: 'восемндцатый',
    19: 'девятнадцатый',
    20: 'двадцатый',
    30: 'тридцатый',
    40: "сороковой",
    50: "пятидесятый",
    60: "шестидесятый",
    70: "семидесятый",
    80: "восьмидесятый",
    90: "девяностый",
    1e2: "сотый",
    1e3: "тысячный"
}


_SHORT_ORDINAL_RU = {
    1e6: "миллионный",
    1e9: "миллиардный",
    1e12: "триллиардный",
    1e15: "quadrillionth",
    1e18: "quintillionth",
    1e21: "sextillionth",
    1e24: "septillionth",
    1e27: "octillionth",
    1e30: "nonillionth",
    1e33: "decillionth"
    # TODO > 1e-33
}
_SHORT_ORDINAL_RU.update(_ORDINAL_BASE_RU)


_LONG_ORDINAL_RU = {
    1e6: "millionth",
    1e12: "billionth",
    1e18: "trillionth",
    1e24: "quadrillionth",
    1e30: "quintillionth",
    1e36: "sextillionth",
    1e42: "septillionth",
    1e48: "octillionth",
    1e54: "nonillionth",
    1e60: "decillionth"
    # TODO > 1e60
}
_LONG_ORDINAL_RU.update(_ORDINAL_BASE_RU)
