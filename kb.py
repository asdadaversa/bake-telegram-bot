from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = [
    [types.KeyboardButton(text="Генерация картинки по запросу")],
    [types.KeyboardButton(text="Ответ на один вопрос")],
    [types.KeyboardButton(text="obmenka")],
    [types.KeyboardButton(text="pogoda")],
    [types.KeyboardButton(text="crypta")],
    [types.KeyboardButton(text="lukashenko")],
    [types.KeyboardButton(text="bake")],
    [types.KeyboardButton(text="brat_bake")],
    [types.KeyboardButton(text="Меню")],
]

start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_kb,  resize_keyboard=True)


main_menu_keyboard = [
    [InlineKeyboardButton(text="Генерация картинки по запросу", callback_data="gen_image_inline")],
    [InlineKeyboardButton(text="Задай вопрос боту", callback_data="vopros_callback")],
    [InlineKeyboardButton(text="Обмен валют", callback_data="obmenka_inline")],
    [InlineKeyboardButton(text="Курсы криптовалют", callback_data="crypta_inline")],
    [InlineKeyboardButton(text="Погода", callback_data="pogoda_inline")],
    [InlineKeyboardButton(text="Лукашенко отжигает", callback_data="lukashenko_inline")],
    [InlineKeyboardButton(text="Информация о Баке", callback_data="bake_inline")],
    [InlineKeyboardButton(text="Информация о брате Баке", callback_data="brat_bake_inline")],
]
main_menu = InlineKeyboardMarkup(inline_keyboard=main_menu_keyboard)


lukashenho_inline_keyboard = [
    [InlineKeyboardButton(text="Нажми меня если хочешь картинку", callback_data="lukashenko_kartinka")],
    [InlineKeyboardButton(text="Нажми меня если хочешь ссылку", callback_data="lukashenko_ssulka")],
]

lukasheno_keyboard = InlineKeyboardMarkup(inline_keyboard=lukashenho_inline_keyboard)


obmenka_kb = [
    [types.KeyboardButton(text="USD")],
    [types.KeyboardButton(text="EUR")],
    [types.KeyboardButton(text="AUD")],
    [types.KeyboardButton(text="SEK")],
    [types.KeyboardButton(text="PLN")],
    [types.KeyboardButton(text="GBP")],
    [types.KeyboardButton(text="Другая валюта")],
    [types.KeyboardButton(text="Меню")]
]
obmenka_keyboard = types.ReplyKeyboardMarkup(keyboard=obmenka_kb,  resize_keyboard=True)


kb_pogoda = [
    [types.KeyboardButton(text="Киев")],
    [types.KeyboardButton(text="Львов")],
    [types.KeyboardButton(text="Париж")],
    [types.KeyboardButton(text="Рим")],
    [types.KeyboardButton(text="Барселона")],
    [types.KeyboardButton(text="Другой город")],
    [types.KeyboardButton(text="Меню")]
]
keyboard_pogoda = types.ReplyKeyboardMarkup(keyboard=kb_pogoda,  resize_keyboard=True)


kb_crypta = [
    [types.KeyboardButton(text="Меню")],
    [types.KeyboardButton(text="Другая монета")],
    [types.KeyboardButton(text="BTC")],
    [types.KeyboardButton(text="ETH")],
    [types.KeyboardButton(text="SOL")],
    [types.KeyboardButton(text="XRP")],
    [types.KeyboardButton(text="ADA")],
    [types.KeyboardButton(text="DOGE")],
    [types.KeyboardButton(text="SHIB")],

]
keyboard_crypta = types.ReplyKeyboardMarkup(keyboard=kb_crypta,  resize_keyboard=True)


main_kb = [[types.KeyboardButton(text="Меню")]]
main_keyboard = types.ReplyKeyboardMarkup(keyboard=main_kb,  resize_keyboard=True)

exit_kb_inline_keyboard = [
    [InlineKeyboardButton(text="Выйти в меню", callback_data="menu")],

]
exit_kb = InlineKeyboardMarkup(inline_keyboard=exit_kb_inline_keyboard)
