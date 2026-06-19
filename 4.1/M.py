strngs = set()


def modern_print(text):
    if text not in strngs:
        strngs.add(text)
        print(text)
modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")