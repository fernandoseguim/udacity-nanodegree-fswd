import time
import webbrowser


def add_break_time(seconds):
    time.sleep(seconds)


def open_browser(url):
    webbrowser.open(url)


def main():
    print("This program started on {}".format(time.ctime()))
    count_breaks = 3

    while count_breaks > 0:
        add_break_time(5)
        open_browser("https://youtu.be/JkqTJivc0Pc")
        count_breaks -= 1

if __name__ == '__main__':
    main()
