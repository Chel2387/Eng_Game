import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 5  # секунды записи
sample_rate = 44100

words_by_level = {
    "easy": ["Книга", "Шар", "Машина", "Файл"],
    "medium": ["Мышь", "Глаз", "Карандаш", "Больница"],
    "hard": ["Огурец", "Круг", "Компьютер", "Окно"]
}

print("Привет! Давай проверим твоё произношение и знание английского языка! (-U-)")
print("Выбери сложность: легко, нормально, сложно")
level = input()

            ### СЛОЖНОСТЬ ЛЕГКО ###

if level == "легко":
    for i in range (len(words_by_level["easy"])):
        word = random.choice(words_by_level["easy"])
        points = 0
        print(word + ", произнеси это слово на английском")

        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("Запись завершена, теперь подожди...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("Ты сказал:", text)
            translator = Translator()
            translated = translator.translate(word, dest='en')
            correct = translated.text.lower()
            print("Правильный перевод: ", correct)

            if text.lower() == correct:
                print("Всё верно!")
                points += 1
                words_by_level["easy"].remove(word)
            else:
                print("Ты проиграл :(")
                print("Ты правильно ответил:", points)
                break


        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь. Ты проиграл")
            break
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")
            break
    print("Молодец! У тебя очень хорошая дикция")

            ### СЛОЖНОСТЬ НОРМАЛЬНО ###

elif level == "нормально":
    for i in range (len(words_by_level["medium"])):
        word = random.choice(words_by_level["medium"])
        points = 0
        print(word + ", произнеси это слово на английском")

        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("Запись завершена, теперь подожди...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("Ты сказал:", text)
            translator = Translator()
            translated = translator.translate(word, dest='en')
            correct = translated.text.lower()
            print("Правильный перевод: ", correct)

            if text.lower() == correct:
                print("Всё верно! Идём дальше")
                points += 1
                words_by_level["medium"].remove(word)
            else:
                print("Ты проиграл :(")
                print("Ты правильно ответил:", points)
                break


        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь. Ты проиграл")
            break
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")
            break
    print("Молодец! У тебя очень хорошая дикция")

            ### СЛОЖНОСТЬ СЛОЖНО ###

elif level == "сложно":
    for i in range (len(words_by_level["hard"])):
        word = random.choice(words_by_level["hard"])
        points = 0
        print(word + ", произнеси это слово на английском")

        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("Запись завершена, теперь подожди...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("Ты сказал:", text)
            translator = Translator()
            translated = translator.translate(word, dest='en')
            correct = translated.text.lower()
            print("Правильный перевод: ", correct)

            if text.lower() == correct:
                print("Всё верно! Идём дальше")
                points += 1
                words_by_level["hard"].remove(word)
            else:
                print("Ты проиграл :(")
                print("Ты правильно ответил:", points)
                break


        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь. Ты проиграл")
            break
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")
            break
    print("Молодец! У тебя очень хорошая дикция")