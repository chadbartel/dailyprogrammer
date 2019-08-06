def pronounce_hex(hex_val):
    """
    
    :param hex_val:
    :return:
    """
    hex_val_trunc = hex_val.lstrip('0x')
    hex_dict = {'1': 'Eleventy', '2': 'Twenty', '3': 'Thirty',
                '4': 'Fourty', '5': 'Fifty', '6': 'Sixty',
                '7': 'Seventy', '8': 'Eighty', '9': 'Ninety',
                'A': 'Atta', 'B': 'Bibbity', 'C': 'City',
                'D': 'Dickety', 'E': 'Ebbity', 'F': 'Fleventy'}
    pronounce = ''
    if len(hex_val_trunc) < 3:
        for i, char in enumerate(hex_val_trunc):
            char_str = str(char)
            if char == '0':
                continue
            if i < 1:
                pronounce += hex_dict[char_str] + '-'
            else:
                pronounce += hex_dict[char_str]
        return pronounce.strip()
    else:
        for i, char in enumerate(hex_val_trunc):
            char_str = str(char)
            if char == '0':
                continue
            if i < 1:
                pronounce += hex_dict[char_str] + '-bitey '
            else:
                pronounce += hex_dict[char_str] + ' '
        return pronounce.strip()


print(pronounce_hex('0xF5'))
print(pronounce_hex('0xB3'))
print(pronounce_hex('0xE4'))
print(pronounce_hex('0xBBBB'))
print(pronounce_hex('0xA0C9'))
