import pyttsx3
import pyautogui
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib
import speech_recognition as sr

path = r'C:\Users\91939\Desktop\project\project\ironman - Shortcut'
os.startfile(path)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voic = 0

engine.setProperty('voice',voices[voic].id)
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
webbrowser=webbrowser.get('chrome')
name = 'yuvraj'

def sendemail(to,content):
    file = open('yuv.txt','r')
    line=file.readline()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('dhgfhj58@gmail.com',line)
    server.sendmail('dhgfhj58@gmail.com',to,content)
    server.close()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 5 and hour < 12:
        speak('good morning '+name)
    elif hour >= 12 and hour < 18:
        speak('good afternoon '+name)
    elif hour >= 18 and hour < 21:
        speak('good evening '+name)
    else:
        speak('its so late night please go to the bed yuvraj')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
try:
    import pywhatkit
except Exception:
    print('internet is slow or not connected to internet ')
    speak('internet is slow or not connected to internet')
    
def takecommand():
    r = sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration = 1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        return query

    except Exception as e:
        e=str(e)
        if 'recognition connection failed: [Errno 11001] getaddrinfo failed' in e:
            print('connect to internet or wifi')
            speak('connect to internet or wifi')
        else:
            print('Say that again please...')
            return 'some error ocurred'

def complete_task(query):
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query, sentences=1)
        speak('according to wikipedia')
        print(results)
        speak(results)

    elif 'search' in query:
        text = query.replace('search','')
        text = text.replace('about','')
        pywhatkit.search(text)
        speak('searching'+text)
        
    elif 'youtube' in query:
        pywhatkit.playonyt('')
        speak('opening youtube please wait')
        
    elif 'google' in query:
        webbrowser.open('google.com')
        speak('opening google please wait')

    elif 'facebook' in query:
        webbrowser.open('facebook.com')
        speak('opening facebook please wait')
        
    elif 'chrome' in query:
        path = r'c:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        os.startfile(path)
        speak('opening chrome please wait')
        
    elif 'music' in query:
        music_dir = 'c:\\Users\\91939\\Desktop\\background music'
        songs = os.listdir(music_dir)
        a = random.randint(0,len(songs)-1)
        os.startfile(os.path.join(music_dir,songs[a]))
        speak('playing music hows that')
        
    elif 'time' in query:
        strtime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'sir, the time is {strtime}')
        
    elif 'date' in query:
        strdate = datetime.datetime.now().strftime("%Y %m %d")
        speak(f'sir, the date is {strdate}')
        
    elif 'some error' in query:
        print('listening error')
    
    elif 'visual' in query or 'studio' in query:
        codepath = 'c:\\Users\\91939\\Appdata\\Local\\Programs\\microsoft VS Code\\Code.exe'
        os.startfile(codepath)
        speak('opening studio please wait')
        
    elif 'email' in query and 'yuvraj' in query:
        try:
            speak('what should i say?')
            content = takecommand()
            to = 'ysinghkanwar@gmail.com'
            sendemail(to,content)
            speak('email has been sent')
        except Exception as e:
            print(e)
            speak('sorry yuvraj i am unable to send your email')
            
    elif 'change' in query and 'voice' in query:
        global voic
        if voic == 0:
            voic = 1
            engine.setProperty('voice',voices[voic].id)
        else:
            voic = 0
            engine.setProperty('voice',voices[voic].id)
            
    elif 'spam' in query and 'whatsapp' in query:
        path = r'C:\Users\91939\Desktop\project\project\newfile.py'
        os.startfile(path)
        speak('spaming whatsapp please wait.......... enter whatsapp no.')
          
    elif 'whatsapp' in query:
        strtime = datetime.datetime.now().strftime('%H%M%S')
        hour1=int(strtime[0:2])
        min1=int(strtime[2:4])+1
        sec1=int(strtime[4:6])
        if sec1>30:
            min1+=1
        speak('what do you want to send')
        text = takecommand()
        pywhatkit.sendwhatmsg('+919399077082',text,hour1,min1)
        speak('message has been sent')
          
    elif 'game' in query:
        path = r'C:\Users\91939\Desktop\project\project\new.py'
        os.startfile(path)
        pyautogui.hotkey('alt','ctrl','left')
        speak('opening your game please wait..')

    elif 'rewoke' in query or 'reebok' in query:
        path = r'C:\Users\91939\Desktop\project\project\jarvis1.py'
        os.startfile(path)
        speak('rewoking please wait..')
        exit()

    elif 'face' in query:
        path='face re.py'
        os.startfile(path)
        speak('starting face came please wait with your cute face.....')
        
    elif 'screen' in query:
        pyautogui.hotkey('alt','ctrl','up')
        speak('turning screen upward please wait')

    elif 'copy' in query:
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        speak('all text copied')

    elif 'paste' in query:
        pyautogui.hotkey('ctrl','v')
        speak('all text copied')
        
    elif 'handwriting' in query:
        speak('what do you want to write :-')
        text = takecommand()
        pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
        
    elif 'cancel shutdown' in query:
        pywhatkit.cancelShutdown()
        speak('canceling shutdown')
        
    elif 'shutdown' in query:
        pywhatkit.shutdown(time=20)
        speak('in 20 seconds your pc will be shutdown')

    elif 'task' in query or 'commands' in query:
        fl=open('jarvis1.py','r')
        all=fl.readlines()
        count_task=1
        for al in all:
            if 'if' in al and ' query'in al:
                if 'in al and' in al:
                    continue
                al = al.replace(' if','')
                al = al.replace(' elif','')
                al = al.replace('in query','')
                print(count_task,al,end='')
                count_task+=1
        speak('here is list of all task or commands')

    elif 'lectures' in query:
        path = r'C:\Users\91939\Desktop\project\videoplayback.mp4'
        os.startfile(path)
        speak('opening lectures please wait..')
        
    elif 'quit' in query or 'sleep' in query:
        speak('sleeping')
        exit()

    elif 'help' in query:
        print('press ctrl + c to exit from help:')
        speak('press ctrl + c to exit from help:')
        print(help())
        
    else:
        speak('your task is not in my list')

if __name__ == '__main__':
    wishme()
    while 1:
        speak('hello '+name+' how can i help you')
        while 1:
            try:
                query=takecommand().lower()
                complete_task(query)
            except Exception as e:
                print(e)
                break
    
