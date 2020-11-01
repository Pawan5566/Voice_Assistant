import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import random
import psutil


class PersonalAssistant:
    def __init__(self, name):
        self.name = name
        self.from_ = "gyaniscode@gmail.com"
        self.password = "India@1234567890"
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Function to convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()


    def time(self):
        """Tells info about current time"""
        time = datetime.datetime.now().strftime("%I:%M:%S")
        self.speak("the current time is")
        self.speak(time)


    def date(self):
        """Tells info about today date"""
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.speak("the current date is")
        self.speak(date)
        self.speak(month_list[month - 1])
        self.speak(year)


    def wishme(self):
        """Wish according time"""
        self.speak("welcome back sir!")

        self.time()
        self.date()

        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            self.speak("Good morning sir!")
        elif 12 <= hour < 17:
            self.speak("Good afternoon sir!")
        elif 17 <= hour < 19:
            self.speak("Good evening sir!")
        else:
            self.speak("Good night sir!")
        self.speak(self.name + " at your service. Please tell me how can I help you?")


    def take_command(self):
        """Takes command using microphone"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print("Recognizing.....")
            print("Query=", query)
        except Exception as e :
            print(e)
            self.speak("Say that again please....")
            return "None"
        return query

    def Path(self,p):
        m = ''
        for r, d, f in os.walk("C:\\"):
            for files in f:
                if files == p:
                    c = str("\\" + p)
                    a = str(os.path.join(r)) + c
                    break
        for i in range(len(a)):
            d = a[i]
            if d == '\\':
                d = '/'
            m += d
        return m

    def send_email(self, to, content):
        """Used to send email"""
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(self.from_, self.password)
        server.sendmail(self.from_, to, content)
        speak("Email has been sent Succesfully!")
        return "None"

    def browse(self):
        a = open('Browser.txt', 'r+')
        chromepath = a.read()
        if chromepath == "":
            a = open('Browser.txt', 'r+')
            chromepath =  self.Path("chrome.exe")
            a.write(chromepath)
            a.close()
        chromepath = chromepath + " %s"
        #print(chromepath) #(optional)
        Jarvis.speak("what should i search?")
        search = self.take_command().lower()
        wb.get(str(chromepath)).open_new_tab(search+'.com')

    def WikiPedia(self, query):
        self.speak("Searching....")
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            self.speak(result)
        except Exception as e:
            print("wikipedia exception =", e)
            self.speak("could not found page on wikipedia")

    def Remember_That(self):
        self.speak("What should i Remember?")
        data = self.take_command()
        self.speak("you said me to remember that " + data)
        remember = open('data.txt', 'a+')
        remember.write(data)
        remember.close()

    def tell_me(self):
        remember = open('data.txt', 'r')
        self.speak("You said me to remember that " + remember.read())

    def screen_shot(self):
        img = pyautogui.screenshot()
        a = str("D:/" + str(random.randint(1, 1000)) + ".png")
        img.save(a)
        self.speak("Done, Screenshot saved inside D Drive")

    def CPU(self):
        usage = str(psutil.cpu_percent())
        self.speak("CPU is at " + usage)
        battery = psutil.sensors_battery()
        self.speak("Battery is at ")
        self.speak(battery.percent)

    def codeblocks(self):
        a = open('Codeblocks.txt', 'r+')
        codeblockspath = a.read()
        if codeblockspath == "":
            codeblockspath = self.Path("codeblocks.exe")
            a.write(codeblockspath)
            a.close()
        for i in range(len(codeblockspath) - 1, 0, -1):
            if codeblockspath[i] == "/":
                codeblockspath = codeblockspath[0:i]
                break
        Var = os.listdir(codeblockspath)
        INDEX = Var.index("codeblocks.exe")
        os.startfile(os.path.join(codeblockspath, Var[INDEX]))

    def WinPowershell(self):
        a = open('Powershell.txt', 'r+')
        powershellpath = a.read()
        if powershellpath == "":
            powershellpath = self.Path("powershell.exe")
            a.write(powershellpath)
            a.close()
        for i in range(len(powershellpath) - 1, 0, -1):
            if powershellpath[i] == "/":
                powershellpath = powershellpath[0:i]
                break
        Var = os.listdir(powershellpath)
        INDEX = Var.index("powershell.exe")
        os.startfile(os.path.join(powershellpath, Var[INDEX]))


Jarvis = PersonalAssistant("JARVIS")
if __name__ == "__main__":
    #Jarvis.wishme()
    while True:
        query = Jarvis.take_command().lower()
        if "time" in query:
            Jarvis.time()
        elif "date" in query:
            Jarvis.date()
        elif "wikipedia" in query:
            Jarvis.WikiPedia(query)
        elif 'remember that' in query:
            Jarvis.Remember_That()
        elif 'do you know anything' in query:
            Jarvis.tell_me()
        elif 'screenshot' in query:
            Jarvis.screen_shot()
        elif 'search in chrome' in query or 'google' in query:
            Jarvis.browse()
        elif 'cpu' in query:
            Jarvis.CPU()
        elif "mail" in query or "send mail" in query  or "send email" in query:
            to = "thedarksoulgd@gmail.com"
            Jarvis.speak("What should i say?")
            content = Jarvis.take_command()
            Jarvis.send_email(to, content)
        elif 'code blocks' in query or 'codeblocks' in query:
            Jarvis.codeblocks()
        elif 'powershell' in query or 'powershell' in query:
            Jarvis.WinPowershell()
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'thank you' in query:
            Jarvis.speak("Its my pleasure Sir!")
        elif "stop" in query or "exit" in query or "offline" in query or "quiet" in query or 'quite' in query:
            quit()
        elif "meet" in query:
            Jarvis.speak("Hello Mister!..Nice to meet you!")
        else:
            pass
