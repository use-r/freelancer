
import win32api
import time


def main():
    while True:
        x, y = win32api.GetCursorPos()
        print('x :', x, 'y :', y)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
