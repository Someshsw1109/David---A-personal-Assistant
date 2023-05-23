from email import encoders, message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyttsx3   
import speech_recognition as sr
import datetime
import os
import cv2
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import instaloader
from bs4 import BeautifulSoup
import psutil
from pywikihow import search_wikihow
import speedtest
#import MyAlarm
import urllib
import numpy as np
#import wolframalpha
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import webbrowser






engine = pyttsx3.init('sapi5') #engine:- defines the basic settings to make the device or VI operations such as IP address, networks, routes, networks, DNS servers....
voices = engine.getProperty('voices') #Provides an interface to instance attributes
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
synthesizer = pyttsx3.init()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))





def speak(audio):
    print("  ")
    print(f": {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait() #runandwait:- It will make the speech audible in the system....

def takeCommand():
    r = sr.Recognizer() # sr.recognizer():- to recognize the speech
    with sr.Microphone() as source: # for running the microphone you need to install PYaudio in the library, if not installed then the code runs but microphone will not work
        print("Listening...")
        r.pause_threshold = 1 # the number of seconds for which the system will recoginze the voice of the user...
        r.adjust_for_ambient_noise(source, duration=1) # used to callibrate the recognizer for changing noise conditions each and evry time when the code runs...
        audio = r.listen(source,timeout=5,phrase_time_limit=5) #time limit for speech_recognition.....

        #try:
        #    query = r.recognize_google(audio, language="en-in")
        #    print(f"user said: {query}")
        #    return query 
        #except Exception as e:
        #    return "Some error occured. sorry sir from my side"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #you can add many languages like, en-uk, hindi......
        print(f"you just said: {query}\n") #print the recognizing voice by the user....

    except Exception as e:
        speak("sir if you don't mind can you say that again please....")
        query = "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    tt = time.strftime("%I:%M %p") #converting the dates and time to string....

    if hour>=0 and hour<=12:
        speak(f"Good Morning, its {tt} sir")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon, its {tt} sir")
    else:
        speak(f"Good Evening, its {tt} sir")
    speak("Hey sir i am DAVID, Please tell me how may i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Enter your login mail id', 'Enter your password')
    server.sendmail('Enter sendinng mail id', to, content)
    server.close()

#def news():
   # main_url = 'https://newsapi.org/v2/everything?q=apple&from=2023-01-21&to=2023-01-21&sortBy=popularity&apiKey=fd5e077110974cb0a7a04db434328dfc'

    #main_page = requests.get(main_url).json()
    #articles = main_page("articles")
    #head = []
    #day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    #for ar in articles:
    #    head.append(ar["titles"])
    #    for i in range(len(day)):
    #    #print(f"today's {day[i]} news is:", head[i])
    #    speak(f"today's {day[i]} news is: {head[i]}")




    


    


    




def Taskexecuting():

    #def Music():
    #    speak("Tell me the name of the song!..")
    #    musicName = takeCommand()

    #    if "All falls down" in musicName:
    #        os.startfile('C:\\Phone\Music\\All Falls Down - Digital Farm Animals, Alan Walker, Noah Cyrus.m4a')

    #    elif "Bhool bhulaiya" in musicName:
    #        os.startfile('C:\\Phone\Music\\Bhool Bhulaiyaa 2 Title Track - Pritam, Tanishk Bagchi, Neeraj Shridhar, Mellow D, Bob.m4a')

    #    else:
    #        kit.playonyt(musicName)

    #    speak("your song has been started!... Enjoy it sir....")
# if _name_ == "main":
    #takeCommand()
    #speak("Write your code here")

    def Whatsapp_msg():
        speak("sir please can you Tell me the name of the person you want to send message on whatsapp")
        name=takeCommand()

        if "Anand" in name:
            speak("Tell me the message sir....")
            message = takeCommand()
            #speak("sir please specify the time for sending this message....")
            #speak("Time in hours.....")
            #hour = int(takeCommand())
            #speak("Time in minutes....")
            #min = int(takeCommand())
            kit.sendwhatmsg("+919155126922", message)    
            speak(f"ok, sir , sending whatsapp message to {name}.....")

        elif "Abhishek" in query:
            speak("Tell me the message sir....")
            message = takeCommand()
            #speak("sir please specify the time for sending this message....")
            #speak("Time in hours.....")
            #hour = int(takeCommand())
            #speak("Time in minutes....")
            #min = int(takeCommand())
            kit.sendwhatmsg("+919955698924", message)    
            speak(f"ok, sir , sending whatsapp message to {query}.....")

        else:
            speak("Tell me the phone number sir....")
            phone = int(takeCommand())
            ph = '+91' + phone
            speak("Tell me the message sir....")
            message = takeCommand()
            #speak("sir please specify the time for sending this message....")
            #speak("Time in hours.....")
            #hour = int(takeCommand())
            #speak("Time in minutes....")
            #min = int(takeCommand())
            kit.sendwhatmsg(ph, message)     
            speak(f"ok, sir , sending whatsapp message to {name}.....")


    wishMe()
    while True:
    #if 1:

        query = takeCommand().lower()
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            speak("ok sir please wait")
            os.startfile(npath)
            while True:
                notepadQuery = takeCommand()
                if "paste" in notepadQuery:
                    pyautogui.hotkey('ctrl', 'v')
                    speak("done sir!")

                elif "save this current file" in notepadQuery:
                    pyautogui.hotkey('ctrl', 's')
                    speak("sir, please specify a name for this current file")
                    notepadeSavingQuery = takeCommand()
                    pyautogui.write(notepadeSavingQuery)
                    pyautogui.press('enter')
                    speak("Sir your file is ready to view")

                elif 'type' in notepadQuery:
                    speak("sir please tell me what should i write here")
                    while True:
                        writeInNotepad = takeCommand()
                        if writeInNotepad == 'exit typing':
                            speak("Done sir")
                            break
                        else:
                            pyautogui.write(writeInNotepad)

                elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                    speak('As per your order sir, i am closing notepad.....')
                    pyautogui.hotkey('ctrl', 'w')
                    break
           
            
                    


        #elif "set alarm" in query:
        #    speak("ok sir please wait i'll set alarm for you")
        #    nn = int(datetime.datetime.now().hour)
        #    if nn == 22:
        #        music_dir = 'C:\\Users\\Somesh Raj\\Favorites'
        #        songs = os.listdir(music_dir)
        #        os.startfile(os.path.join(music_dir, songs[0]))


        #elif "close notepad" in query:
         #   speak("Thanks for using notepad, i'm closing it sir")
          #  os.system("taskkill /f /im notepad.exe")
            

        elif "open code" in query:
            codePath = "C:\\Users\\Somesh Raj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("ok sir please wait")
            os.startfile(codePath)
            while True:
                codeQuery = takeCommand()
                if "paste" in codeQuery:
                    pyautogui.hotkey('ctrl', 'v')
                    speak("done sir!")

                elif "create a new file" in codeQuery:
                    pyautogui.hotkey('ctrl', 'alt', 'windows', 'N')
                    speak("Sir your file is ready for work")
                    speak("sir, please specify a name for this current file")
                    FileName = takeCommand()
                    pyautogui.write(FileName)
                    pyautogui.press('enter')
                    speak("Sir your file is ready to view")

                elif "save this current file" in codeQuery:
                    pyautogui.hotkey('ctrl', 's')
                    speak("sir, please specify a name for this current file")
                    codeSavingQuery = takeCommand()
                    pyautogui.write(codeSavingQuery)
                    pyautogui.press('enter')
                    speak("Sir your file is ready to view")

                elif 'type' in codeQuery:
                    speak("sir please tell me what should i write here")
                    while True:
                        writeIncode = takeCommand()
                        if writeIncode == 'exit typing':
                            speak("Done sir")
                            break
                        else:
                            pyautogui.write(writeIncode)

                elif "exit notepad" in codeQuery or 'close notepad' in codeQuery:
                    speak('As per your order sir, i am closing the vs code.....')
                    pyautogui.hotkey('ctrl', 'w')
                    break


       # elif "close code" in query:
        #    speak("Thanks for using code, i'm closing it sir")
        #    os.system("taskkill /f /im code.exe")

        elif "open command prompt" in query:
            speak("ok sir please wait")
            os.system("start cmd")

        elif "close command prompt" in query:
            speak("Thanks for using command prompt, i'm closing it sir")
            os.system("taskkill /f /im cmd.exe")

        
        elif "open camera" in query:
            speak("ok sir please wait")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()



        elif "play music" in query:
            speak("ok sir please wait")
            music_dir = "C:\\Users\\Somesh Raj\\Favorites"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak("ok sir please wait")
            speak(f"your IP address is {ip}")

        #elif "Open video" in query:
         #   speak("Ok sir please wait")
          #  video_dir = "C:\Users\Somesh Raj\Videos"
           # videos = os.listdir(video_dir)
           # for video in videos:
           #     if video.endswith('.mp4'):
           #         os.startfile(os.path.join(video_dir, video))

        elif "wikipedia" in query:
            speak("ok sir please wait")
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("sir according to wikipedia...")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("ok sir please wait")
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            speak("ok sir please wait")
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            speak("ok sir please wait")
            webbrowser.open("www.facebook.com")

        elif "open stack over flow" in query:
            speak("ok sir please wait")
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("ok sir please wait")
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            speak("ok sir please wait")
            webbrowser.open(f"{cm}")

        elif 'play' in query:
            query = query.replace('song_name', '')
            speak(' ok sir as per your order i am playing ' + query)
            kit.playonyt(query)

        elif 'send a message in whatsapp' in query:

            Whatsapp_msg()

        #elif "send message" in query:
        #    speak("ok sir please wait for some seconds i'll send that message")
        #    kit.sendwhatmsg("+919155126922", "Main code likh rha tha isilie main phone ni utha paya tha uss time kal morning me call karte hain aaram se",3,44)


        elif "email to somesh" in query:
            try:
                speak("ok sir please wait")
                speak("what should i say?")
                content = takeCommand().lower()
                to = "someshraj78669@gmail.com"
                sendEmail(to, content)
                speak("sir email has been sent successfully to somesh")

            except Exception as e:
                print(e)
                speak("sorry sir there is an error occured during sending this email to somesh, i'm not able to send this email...")

            
        elif "tell me a joke" in query:
            speak("ok sir please wait, i've a joke for you")
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            speak("ok sir your pc will be shutting down in 5 seconds")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("ok sir your pc will be restarting in 5 seconds")
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powprof.dll, setSuspendState 0,1,0")

       


        elif 'switch the window' in query:
            speak("ok sir please wait, i'm switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "send email to somesh" in query:
            speak("ok sir please wait, i'll send it a second")
            query = takeCommand().lower()
            
            if "send a file" in query:
                email = 'somesh388.hitee22020@gmail.com'
                password = 'Swati#110901'
                send_to_email = 'someshraj78669@gmail.com'
                speak("ok sir, what is the subject of that email")
                query = takeCommand().lower()
                subject = query
                speak("and sir please tell me, what is the message for this email")
                speak("sir please kindly enter the correct path of the file into the shell")
                file_location = input("please enter the path here:-")

                speak("sir please wait a second, i'll sending email now")

                msg = MIMEMultipart()
                msg['from'] = email
                msg['to'] = send_to_email
                msg['subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-Disposition', "attachment; filename= %s" %filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent successfully to somesh")
            else:
                email = 'somesh388.hitee22020@gmail.com'
                password = 'Swati#110901'
                send_to_email = 'someshraj78669@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent successfully to somesh")




            

        #elif "tell me the news" in query:
        #    speak("ok sir please wait, i'm fetching the latest news")
        #    news()

        elif "where i am" in query or "where we are" in query or "can you find me, where i am" in query or "can you find my location quickly" in query:
            speak("wait a sec sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i think we are in {city} city of {state} state of {country} country, but sir i'm not sure my sensor gets information about this location")
            except Exception as e:
                speak("sorry sir my sensor does not able to find where we are..")
                pass


        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly..")
            name = input("Enter your user name correctly:-")
            speak("sir please wait a second, i'll gathering the information of that account")
            webbrowser.open(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this instagram account..")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                pass


        elif "take a screenshot" in query:
            speak("sir, please tell me the name for this scrrenshot file")
            name = takeCommand().lower()
            speak("please sir can you hold the screen for few seconds, i am taking the screenshot")
            time.sleep(4)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screnshot is saved in our main folder. Now i am ready for the next command...")

        elif "hello" in query or "hii" in query:
            speak("Hello sir")

        elif "how are you" in query:
            speak("I'm fine sir what about you")

        elif "also good" in query or "also fine" in query or "fine" in query:
            speak("ok sir, what do you want to do right now")

        elif "thanks" in query or "thank you" in query:
            speak("it's my pleasure sir")

        elif "temperature" in query:


            search = "temperature in Muzaffarpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"sir the current {search} is {temp}")        
                
        #elif "activate how to do mode" in query:
         #   speak("how to do mode is activated sir please tell me what you want to know")
          #  how = takeCommand()
           # speak("ok sir i'm fetching the results that you're looking for")
            #max_results = 1
            #how_to = search_wikihow(how, max_results)
            #assert len(how_to) == 1
            #how_to[0].print()
            #speak(how_to[0].summary)

        elif "activate how to do mode" in query:
            speak("sir your how to do mode is activated now")
            while True:
                speak("sir please tell me you're looking for")
                how = takeCommand()
                speak("ok sir i'm fetching the results that you're looking for")
                try:
                    if "exit" in how or "close" in how:
                        speak("as per your order sir your how to mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i'm not able to find this")

        
        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("sir we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("sir i think we should connect our system to charging point because your battery is less than 75%")
            elif percentage<=15 and percentage<=30:
                speak("sir we don't have enough power to run this system, please connect to charging")
            elif percentage<=15:
                speak("sir we have very low power, please connect to charging or the system will shutdown very soon")
        

        elif "internet speed" in query or "speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")     
    

        #elif 'type' in query:
            #speak("sir, please tell me what should i write here")
            #while True:
             #   typeQuery = takeCommand()
              #  if typeQuery == "exit typing":
               #     speak("Done sir!")
                #    break
                #else:
                 #   pyautogui.write(typeQuery)
        #try:
            #os.system('cmd /k "speedtest"')
        #except:
            #speak("sir there is no internet connection")

        elif 'volume up' in query:
            speak(" ok sir please wait")
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            speak(" ok sir please wait")
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            speak(" ok sir please wait")
            pyautogui.press("volumemute")

        #elif 'set alarm' in query:
        #    speak("sir please tell me the time to set alarm. for example, set alarm to 5:30 am")
        #    tt = takeCommand()
        #    tt = tt.replace("set alarm to", "")
        #    tt = tt.replace(".", "")
        #    MyAlarm.alarm(tt)

        elif "open mobile camera" in query:
            URL = "U_R_L"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows()

        elif "open my folder" in query:
            speak("ok sir please wait i'm opening your folder")
            cpath = "C:\\Users\\somes\\S.W.A.T.I"
            os.startfile(cpath)

        elif "what can you do for me" in query:
            speak('nice question sir')
            speak('As per my program, I am an AI which is created by you in python programming language which can execute tasks through your voice commands')

        elif "minimize" in query or 'minimise' in query:
            speak('sir as per your order i am minimizing the current window')
            pyautogui.moveTo(1251,8)
            pyautogui.leftClick()

        elif "maximize" in query or 'maximise' in query:
            speak('sir as per your order i am maximizing the current window')
            #pyautogui.moveTo(1120,14)
            pyautogui.moveTo(1296,12)
            pyautogui.leftClick()

        elif "close the current window" in query or 'close the current application' in query:
            speak('sir as per your order, i am closing the current window')
            pyautogui.moveTo(1339,0)
            pyautogui.leftClick()

        elif 'info about' in query:
            infoQuery = query.replace('info about', '')
            speak("ok sir please wait i'm fetching some info about this one")
            try:
                resInfo = kit.info(infoQuery, lines=2)
                print(resInfo)
                speak(resInfo)
            except:
                speak("sir my system doen't find any info regarding this one..., i think i couldn't find this")

        elif 'where is' in query:
            from g_map import GMAP
            place = query.replace("where is ", "")
            place = place.replace("DAVID", "")

            GMAP(place)


        
        elif "sleep now" in query:
            speak("ok sir i'm going to sleeping you can call me anytime i'm always available for you")
            break
            

        

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "good morning" in permission or "good afternoon" in permission or "good evening" in permission:
            Taskexecuting()
        
        elif "goodbye" in permission or "good night" in permission:
            speak("ok sir i'm leaving now, BYE... Take care of yourself")
            sys.exit()
