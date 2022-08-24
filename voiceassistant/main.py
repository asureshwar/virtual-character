import random
import sys
import pyttsx3 as tts
import speech_recognition
from neuralintents import GenericAssistant
from textblob import TextBlob
from shakespear import generate_text
import pandas_datareader as web
import requests
from bs4 import BeautifulSoup

stock_tickers = ['AAPL', 'FB']
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
voices = speaker.getProperty('voices')

speaker.setProperty('rate', 130)

todo_list = ['go shopping', 'clean room', 'record video']
seneca = [
    "“It’s not because things are difficult that we dare not venture. It’s because we dare not venture that they are difficult.”",
    "“We suffer more often in imagination than in reality.”", "“He who is brave is free.”",
    "“The whole future lies in uncertainty: live immediately.” ",
    "“If a man knows not to which port he sails, no wind is favorable.”"]
marcus = ["If it is not right do not do it; if it is not true do not say it.",
          "“People are not disturbed by things, but by the views they take of them.”",
          "“Don’t go on discussing what a good person should be. Just be one.”",
          "“When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love…” "]
dobad = [
    "you are just one individual among a species of primate with billions of relatives living on a tiny rock in the middle of nowhere, so why do you worry all the time",
    "one often meets  his destiny on the road he takes to avoid it",
    "if you believed in santa for more than 5 years then you can believe in yourself for at least 10 seconds"]
dogood = ["life is barely long enough to get good at one thing , so be careful what u get good at ",
          "the world will ask who u are , and if you do not know , the world will tell you "]
quotes = ["the planet is fine , but the people are fucked",
          "words are like keys , if u choose them right ,they can open any heart and shut any mouth",
          "secret to happiness is low expectation"]
speaker.setProperty('voice', 'english_rp+f3')


def add_todo():
    global recognizer
    speaker.say("what do you want to add")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.02)
                audio = recognizer.listen(mic)

                todo = recognizer.recognize_google(audio)
                todo = todo.lower()

                todo_list.append(todo)
                done = True

                speaker.say(f"I successfully added {todo} in to do list")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("i did not understand what u said. please try again")
            speaker.runAndWait()


def show_todos():
    speaker.say("the items on your to do list are ")
    for todo in todo_list:
        speaker.say(todo)
    speaker.runAndWait()


def hello():
    speaker.say("hello,master, what can i do for you today?")
    speaker.runAndWait()


def praise():
    global recognizer
    speaker.say("praise whom")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.02)
                audio = recognizer.listen(mic)

                person = recognizer.recognize_google(audio)
                person = person.lower()
                speaker.say(f"well , {person}, have some balls ,ooh i forgot u have no balls")
                speaker.runAndWait()
                done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("i did not understand what u said. please try again")
            speaker.runAndWait()


def shakespeare():
    text = generate_text(300, 0.2)
    print(text)
    speaker.say(f"I quote shakespeare now {text}")
    speaker.runAndWait()


def favorite_quote():
    speaker.say(
        "i quote Thomas Babington Macaulay. and his poem lays of ancient rome , Then out spake brave Horatius,The Captain of the gate To every man upon this earth,Death cometh soon or late,And how can man die better,Than facing fearful odds, For the ashes of his fathers, And the temples of his Gods.")
    speaker.runAndWait()


def sentiment():
    global recognizer
    speaker.say("tell me how was your day")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.02)
                rec = recognizer.listen(mic)
                audio = recognizer.recognize_google(rec)
                audio = audio.lower()
                blob = TextBlob(audio)
                senti = blob.sentiment.polarity
                if senti > 0:
                    speaker.say(
                        " glad to hear your day is good,  now , know that, its not living forever ,shrihari, its living with yourself ")
                    speaker.runAndWait()
                else:
                    speaker.say(
                        " sad to hear your day isnt good, but you know that , anything can change your bad day in to good day , now , know that, its not living forever ,shrihari, its living with yourself ")
                    speaker.runAndWait()

                speaker.say(f"your day was on scale of -1 to 1 is  {senti}")
                speaker.runAndWait()
                done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("i did not understand what u said. please try again")
            speaker.runAndWait()


def introduce():
    global recognizer
    speaker.say("introduce   whom")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.02)
                audio = recognizer.listen(mic)

                person = recognizer.recognize_google(audio)
                person = person.lower()
                speaker.say(
                    f"well ,, {person}, i am janeaway of the starship u s s voyager, i am not really here , i am an artificial intellegence character made by master shrihari with help of, nlp and tensorflow ")
                speaker.runAndWait()
                done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("i did not understand what u said. please try again")
            speaker.runAndWait()


def stocks():
    for ticker in stock_tickers:
        data = web.DataReader(ticker, 'yahoo')
        float = data['Close'].iloc[-1]
        format_float = "{:.2f}".format(float)
        print(f"the last price of {ticker} was {format_float}")
        speaker.say(f"the last price of {ticker} was {format_float}")
        speaker.runAndWait()


def marcusaurelius():
    rnd = random.choice(marcus)
    print(f"{rnd}")
    speaker.say(f"{rnd}")
    speaker.runAndWait()


def senecas():
    rnd = random.choice(seneca)
    print(f"{rnd}")
    speaker.say(f"{rnd}")
    speaker.runAndWait()


def quotesses():
    rnd = random.choice(quotes)
    print(f"{rnd}")
    speaker.say(f"{rnd}")
    speaker.runAndWait()


url = 'https://www.bbc.com/news/world/asia/india'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')


def news():
    for x in headlines:
        beautyfulnews = x.text.strip()
        print(beautyfulnews)
        speaker.say(f"today's news is {BeautifulSoup} ")
        speaker.runAndWait()


def exit():
    speaker.say("I will terminate myself ,master,have a good day")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "add_todo": add_todo,
    "show_todos": show_todos,
    "praise": praise,
    "shakespeare": shakespeare,
    "exit": exit,
    "favorite_quote": favorite_quote,
    "sentiment": sentiment,
    "introduce": introduce,
    "stocks": stocks,
    "marcus": marcusaurelius,
    "seneca": senecas,
    "quotes": quotesses,
    "news": news}

assistant = GenericAssistant('intents.json', mappings)
assistant.train_model()
assistant.load_model('main.model')

while True:
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.02)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
