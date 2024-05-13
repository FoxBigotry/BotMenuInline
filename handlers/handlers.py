from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboard.keyboards as kb
from settings import system_messages

router = Router()


@router.message(CommandStart())
async def step_one_height(message: Message):
    await message.answer('Привет!\nУчимся делать меню на инлайн кнопках для начала вызови меню командорй /menu')


@router.message(Command("help"))
async def help_message(message: Message):
    await message.bot.send_message(message.chat.id,
                                   system_messages.HELP_MESSAGE,
                                   parse_mode="HTML")


@router.message(Command('menu'))
async def command_menu(message: Message):
    await message.answer('Menu', reply_markup=kb.menu_keyboard.as_markup())


@router.callback_query(F.data == 'back_to_menu_btn')
async def back_to_menu_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Menu',
                                     reply_markup=kb.menu_keyboard.as_markup())


@router.callback_query(F.data == 'how_work_btn')
async def how_work_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Make personal diets,'
                                     'track calories to control you weight or just chat with bot to discuss you food '
                                     'preferenses, habits and goals',
                                     reply_markup=kb.back_keyboard.as_markup())


@router.callback_query(F.data == 'my_diet_btn')
async def my_diet_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('вызываем /diet_plan,  кнопку назад убрать после добавки логики',
                                     reply_markup=kb.back_keyboard.as_markup())


@router.callback_query(F.data == 'track_calories_btn')
async def track_calories_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('-> come back soon',
                                     reply_markup=kb.back_keyboard.as_markup())


@router.callback_query(F.data == 'my_preferences_btn')
async def my_preferences_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('вызываем /miniapp,  кнопку назад убрать после добавки логики',
                                     reply_markup=kb.back_keyboard.as_markup())


@router.callback_query(F.data == 'commands_btn')
async def commands_btn(callback: CallbackQuery):
    await callback.answer('')
    await help_message(callback.message)
    await callback.message.edit_text('Existing commands:',
                                     reply_markup=kb.back_keyboard.as_markup())


@router.callback_query(F.data == 'settings_btn')
async def settings_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Settings menu',
                                     reply_markup=kb.settings_keyboard.as_markup())


@router.callback_query(F.data == 'communc_time_btn')
async def communc_time_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('вызываем /set_daily_time, кнопка остаётся',
                                     reply_markup=kb.back_settings_keyboard.as_markup())


@router.callback_query(F.data == 'language_btn')
async def language_btn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('вызываем /languege, кнопка остаётся',
                                     reply_markup=kb.back_settings_keyboard.as_markup())

