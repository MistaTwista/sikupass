from itertools import product

chars = '0123456789abcdefghijklmnopqrstuvwxyz' # chars to look for


def gen(chars, len_from=1, len_to=3, stopped_at=''):
    returned = False
    for length in range(len_from, len_to):
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            result = ''.join(attempt)
            if not returned:
                if stopped_at == '' or result == stopped_at:
                    returned = True
                continue
            yield result



for n in gen(chars, len_from=1, len_to=3, stopped_at='za'):
    f = open('somefile.txt', 'a')
    f.write(n+'\n')
    wait("1602886200199.png")
    click("1602886200199.png")
    type('muhaha'+Key.ENTER)
    #type(Key.ENTER)
    #type(Key.BACKSPACE)
    