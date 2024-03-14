from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    openai_vopros = State()
    openai_image = State()
    obmenka = State()
    pogoda = State()
    crypta = State()
    bake = State()
    brat_bake = State()
    lukashenko = State()
