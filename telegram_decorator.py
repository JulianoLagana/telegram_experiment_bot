import functools
from datetime import datetime
import traceback
import telegram
import json


user_data = json.load(open('telegram_config.json', 'r'))
bot = telegram.Bot(token=user_data['token'])


def send_message(text, **kwargs):
    bot.send_message(chat_id=user_data['chat_id'], text=text, **kwargs)


def telegram_updates(_fun=None, *, send_start_message=True):
    def telegram_decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            if send_start_message:
                send_message(f'Starting function {fun.__name__}.')

            # Run the wrapped function
            try:
                return_value = fun(*args, **kwargs)
            except Exception as e:
                error_msg = traceback.format_exc()
                send_message(f"Something went wrong! Your function {fun.__name__} has just crashed. "
                             f"The exception raised was: \n\n{error_msg}\n\n"
                             f"Total running time: {datetime.now()-start}")
                raise e
            else:
                t_time = datetime.now()-start
                send_message(f'The function {fun.__name__} has finished. \n\n'
                             f'Total running time: {t_time}')
                return return_value
        return wrapper

    if _fun is None:
        return telegram_decorator
    else:
        return telegram_decorator(_fun)

