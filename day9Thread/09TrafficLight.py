# 红绿灯
import time, threading

event = threading.Event()


def light():
    count = 0
    event.set()  # green light
    while True:
        if 5 < count and 10 >= count:  # to red
            event.clear()  # clear flag red light
            print('\033[41;1m red light is on .... \033[0m')

        elif count >= 10:  # to green
            event.set()  # green light
            count = 0
        else:
            print('\033[42;1m green light is on .... \033[0m')
        time.sleep(1)
        count += 1
# light()


def car():
    while True:
        if event.is_set():  # green light
            print('cars running...')
            time.sleep(1)
        else:
            print('cars sees red light, stops.')
            event.wait()
            print('\033[34;1m green light is on, start running\033[0m')


light = threading.Thread(target=light,)
light.start()

car = threading.Thread(target=car,)
car.start()
