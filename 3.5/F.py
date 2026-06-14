alphabet = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e',
    'Ж': 'Zh', 'ж': 'zh',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Й': 'I', 'й': 'i',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'Kh', 'х': 'kh',
    'Ц': 'Tc', 'ц': 'tc',
    'Ч': 'Ch', 'ч': 'ch',
    'Ш': 'Sh', 'ш': 'sh',
    'Щ': 'Shch', 'щ': 'shch',
    'Ы': 'Y', 'ы': 'y',
    'Э': 'E', 'э': 'e',
    'Ю': 'Iu', 'ю': 'iu',
    'Я': 'Ia', 'я': 'ia',
    'Ь': '', 'ь': '',
    'Ъ': '', 'ъ': '',
}

with open(r"D:\code\yandex-handbook-python\txts\3.5\E cyrillic.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()
translated = ''
for sentences in lines:
    for symbol in sentences:
        if symbol in alphabet:
            translated += alphabet[symbol]
        else:
            translated += symbol
with open(r"D:\code\yandex-handbook-python\txts\3.5\E transliteration.txt", "w", encoding="UTF-8") as file_out:
    # file_out.write(translated)
    print(translated, file=file_out)