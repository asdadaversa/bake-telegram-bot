from aiogram import Router
from aiogram import F
from aiogram import flags
from states import Gen
import text
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionMiddleware

from kb import *
from secondary_functions.ai_text import *

router = Router()
router.message.middleware(ChatActionMiddleware())


@router.callback_query(F.data == "vopros_callback")
async def input_openai_message(callback: types.Message, state: FSMContext):
    await state.set_state(Gen.openai_vopros)
    await callback.message.answer("Начните диалог с ботом ")
    await callback.message.answer(text.gen_exit, reply_markup=exit_kb)


@router.message(F.text == "Ответ на один вопрос")
async def input_openai_message(message: types.Message, state: FSMContext):
    await state.set_state(Gen.openai_vopros)
    await message.answer("начните диалог с ботом")


@router.message(Gen.openai_vopros)
@flags.chat_action("typing")
async def openai_vopros(message: types.Message, state: FSMContext):
    await message.answer(f"{generate_openai_tekst(message.text)}")
    await message.answer("Выйти в меню", reply_markup=exit_kb)
