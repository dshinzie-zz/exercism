def numeral(arabic_input):
    CONVERSION = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        49: 'XLIX',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    roman = ''
    for number in sorted(CONVERSION.keys())[::-1]:
        while arabic_input >= number:
            roman += CONVERSION[number]
            arabic_input -= number
    return roman
