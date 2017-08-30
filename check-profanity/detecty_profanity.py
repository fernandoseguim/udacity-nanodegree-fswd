from urllib import request, parse


def read_text():
    file = open("movie_quotes.txt")
    quotes = file.readline()
    while quotes:
        print(quotes)
        check_profanity(quotes)
        quotes = file.readline()

    file.close()


def check_profanity(text):
    param = {'q':text}
    url = "http://www.wdylike.appspot.com/?" + parse.urlencode(param)
    conn = request.urlopen(url)
    output = conn.read()
    print(output)
    conn.close()

read_text()
