import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator  # Используем deep-translator для перевода

# Функция для получения случайного английского слова и его определения
def get_english_words():
    url = "https://randomword.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем успешность запроса
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {"english_word": english_word, "word_definition": word_definition}
    except Exception as e:
        print(f"Произошла ошибка при получении данных: {e}")
        return None

# Функция для перевода слова и его определения
def translate_to_russian(word, definition):
    try:
        translator = GoogleTranslator(source="en", target="ru")
        translated_word = translator.translate(word)
        translated_definition = translator.translate(definition)
        return translated_word, translated_definition
    except Exception as e:
        print(f"Произошла ошибка при переводе: {e}")
        return word, definition  # В случае ошибки возвращаем оригинальные данные

# Основная функция игры
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Ошибка при получении слова, попробуйте позже.")
            break

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский язык
        russian_word, russian_definition = translate_to_russian(english_word, word_definition)

        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ").strip()
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Возможность завершить игру
        play_again = input("Хотите сыграть еще раз? y/n: ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()
