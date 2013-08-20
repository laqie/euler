def speech(number):
    NUMBERS = (
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen')
    TENS = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred'
    }
    result = ''
    if number >= 100:
        result += (NUMBERS[number // 100] + ' ' + TENS[100] + ' ')
        number %= 100
        if number > 0:
            result += 'and  '

    if number >= 20:
        result += (TENS[number // 10 * 10]) + ' '
        number %= 10

    if 0 < number < 20:
        result += (NUMBERS[number])

    return result.strip()


# print len(speech(342).replace(' ', ''))
# print len(speech(115).replace(' ', ''))
th = len("onethousand")
r = 0
for i in xrange(1, 1000):
    r += len(speech(i).replace(' ', ''))

print r + th