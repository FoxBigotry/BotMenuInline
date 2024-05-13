from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_button(text: str, callback_data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=callback_data)


def create_row(*buttons: InlineKeyboardButton) -> list:
    return [button for button in buttons]


def create_keyboard(max_width: int, *rows: list) -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.max_width = max_width
    for row in rows:
        keyboard.row(*row)
    return keyboard


menu_keyboard = create_keyboard(2,
                                create_row(
                                    create_button('How does it work', 'how_work_btn'),
                                    create_button('My diet', 'my_diet_btn'),
                                    create_button('Track calories', 'track_calories_btn'),
                                    create_button('My preferences', 'my_preferences_btn'),
                                    create_button('Commands', 'commands_btn'),
                                    create_button('Settings', 'settings_btn')
                                )
                                )

back_keyboard = create_keyboard(1,
                                create_row(
                                    create_button('↑', 'back_to_menu_btn')
                                )
                                )

settings_keyboard = create_keyboard(2,
                                    create_row(
                                        create_button('Communication time', 'communc_time_btn'),
                                        create_button('Language', 'language_btn'),
                                        create_button('↑', 'back_to_menu_btn')
                                    )
                                    )

back_settings_keyboard = create_keyboard(2,
                                         create_row(
                                             create_button('↻ Back to settings', 'settings_btn'),
                                             create_button('↑', 'back_to_menu_btn')
                                         )
                                         )

