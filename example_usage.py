from telegram_decorator import telegram_updates
import time


@telegram_updates
def test_function(a):
    print('Running')
    for i in range(10):
        print('...')
    start = time.time()
    while time.time()-start < 7:
        pass
    print(a)


test_function('oi')
