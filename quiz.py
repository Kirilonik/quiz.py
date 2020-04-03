#! python3
# quiz.py - Маленький помошник в составлении простеньких тестов.
import random

# Укажите количество билетов
Bilets = 10
# Укажите количество вопросов
Vopros = 10

capitals = {"Россия": "Москва", "США": "Вашингтон", "Канада": "Оттава",
            "Германия": "Берлин", "Украина": "Киев",
            "Польша": "Варшава", "Лондон": "Великобритания",
            "Сингапур": "Сингапур", "Финляндия": "Хельсинки",
            "Япония": "Токио", "Дания": "Копенгаген",
            "Португалия": "Лисабон", "Армения": "Ереван"}

for quizNum in range(1, Bilets+1):
    # создание файлов билетов и ключей ответов.
    quizFile = open('Билет_%s.txt' % quizNum, 'w')
    answerKeyFile = open('Ответ_%s.txt' % quizNum, 'w')

    # Запись заголовка Билета
    quizFile.write('Имя:\nДата:\nКурс:\n')
    quizFile.write(("\t" * 2) + "Проверка на знание столиц стран Билет %s" % quizNum)
    quizFile.write("\n\n")

    #  получаем список всех стран
    countrys = list(capitals.keys())
    random.shuffle(countrys)  # перемешивает список

    for questionNum in range(10):
        # Берем из словаря правильный ответ
        correctAnswer = capitals[countrys[questionNum]]
        wrongAnswers = list(capitals.values())
        # Убераем из списка неправильных ответов - правильный
        # и рандомно берем 3 элемента
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        #  обьеденяем 3 неправильных ответа с правильным
        #  и снова перемешиваем
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # Заполнение 4х вариантов ответа на 1 вопрос
        quizFile.write("\n%s. Выберите столицу %s.\n" % (questionNum+1, countrys[questionNum]))
        quizFile.write("\n")
        for i in range(4):
            quizFile.write(" %s. %s\n" % ('ABCD'[i], answerOptions[i]))
        # Заполним файл с ответами на вопросы
        answerKeyFile.write("%s. %s\n" % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    # Обязательно закрыть файлы после испльзования.
    quizFile.close()
    answerKeyFile.close()