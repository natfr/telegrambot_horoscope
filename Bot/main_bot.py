from Bot.admin import admin, admin_see_users, send_message_start, text_approval, admin_approval, admin_dontknow
from Bot.analytics import analytics_bot
from Bot.buttons import (get_zodiac_keyboard, get_time_horoscope_keyboard, get_type_horoscope_keyboard, start_again, \
                         first_keybord, buttons_zodiac, TITLES_zodiac, buttons_type, TITLES_type, buttons_time,
                         TITLES_time)
from Bot.horoscope import get_url, parse
from Bot.settings import Base_url, Bot_key
from telegram import Bot, Update
from telegram.ext import Updater, CallbackQueryHandler, Filters, MessageHandler, CommandHandler, ConversationHandler
from telegram.utils.request import Request

import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)


def start(update, context):
    """
    Command 'Start' will result in an initial phrase.
    """
    print(f'Новый запрос от : {update.message.from_user}.')

    # Analytics
    analytics_bot(user_info=update.message.from_user)

    update.message.reply_text(
        text=f'Привет, {update.message.from_user.first_name}. Хочешь узнать, что звезды подготовили для тебя?',
        reply_markup=first_keybord()
    )


def button(update, context):
    """
    The function returns the horoscope to a user basing on his request.
    """
    # Analytics
    analytics_bot(user_info=update.effective_message.from_user)

    query = update.callback_query
    user_request = query.data

    if user_request == 'callback_button22_firststart':
        query.edit_message_text(text='Выбери свой знак задиака:', reply_markup=get_zodiac_keyboard())

    if user_request in buttons_zodiac:
        context.user_data['zodiac'] = TITLES_zodiac[user_request].split(' ', 1)[0]

        query.edit_message_text(
            text="Выбранный знак зодиака: {}. \nВыбери тип гороскопа:".format(
                context.user_data['zodiac']),
            reply_markup=get_type_horoscope_keyboard())

    elif user_request in buttons_type:
        context.user_data['type'] = TITLES_type[user_request].split(' ', 1)[0]
        query.edit_message_text(
            text="Выбранный знак зодиака: {}. \nВыбранный тип гороскопа: {}. \nТебя интересует гороскоп на :".format(
                context.user_data['zodiac'],
                context.user_data['type']),
            reply_markup=get_time_horoscope_keyboard())

    elif user_request in buttons_time:
        context.user_data['time'] = TITLES_time[user_request].split(' ', 1)[0]
        query.edit_message_text(
            text="Знак зодиака: {}. \nТип гороскопа: {}. \nПериод прогнозирования : {}. \nПрогноз: ".format(
                context.user_data['zodiac'],
                context.user_data['type'],
                context.user_data['time'])
                 + str(parse(get_url(
                context.user_data['zodiac'],
                context.user_data['type'],
                context.user_data['time']))),
            reply_markup=start_again())

    elif user_request == 'callback_button21_start':
        update.effective_message.reply_text(text=f'Привет. Хочешь узнать, что звезды подготовили для тебя?',
                                            reply_markup=first_keybord())  # Обратите внимание: используется `effective_message`


def main():
    """
    Bot's initialisation.
    """
    print('Start')

    bot = Bot(
        request=Request(connect_timeout=0.5),
        token=Bot_key,
        base_url=Base_url,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    print(updater.bot.get_me())

    admin_send_message = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Отправить сообщение)$'), send_message_start),
            # ^ - начало строки, $ - конец строки,
        ],
        states={
            'admin_text': [MessageHandler(Filters.text, text_approval)],
            'admin_approval': [MessageHandler(Filters.regex('^(Да|Нет)$'), admin_approval)],  # | или
        },
        fallbacks=[CommandHandler('cancel', admin_dontknow)]
    )

    updater.dispatcher.add_handler(admin_send_message)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('admin', admin))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(Все пользователи)$'), admin_see_users))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    logging.info('Бот стартовал')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
