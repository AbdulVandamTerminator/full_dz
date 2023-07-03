from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



Button_anic = InlineKeyboardButton(text='Анекдоты', callback_data='Pars_Anic')
Button_test_pars = InlineKeyboardButton(text='Криптовалюта', callback_data='Pars_Cripts')
Key_Pars = InlineKeyboardMarkup().add(Button_anic).add(Button_test_pars)