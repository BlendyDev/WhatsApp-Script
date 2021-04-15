from selenium import webdriver
from math import pi
import time
import re
import datetime

print ("")
print ("-------------------------------------------------------")
print ("- [MEGA-SCRIPT] - By BlendyDev (github.com/blendydev) -")
print ("-------------------------------------------------------")
print ("")
print ("# FIRST SELECT A CONTACT/GROUP TO MESSAGE ON WHATSAPP WEB #")
print ("")


ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--no-sandbox') 
ChromeOptions.add_argument('--user-data-dir=./User_Data')
    
driver = webdriver.Chrome(options=ChromeOptions)
driver.get('https://web.whatsapp.com/')

input('Press return after on group after scanning QR code | ')
delay = 0.0
def main ():
    
    # Fibonacci | Power | Consecutive | TextSpam | Send | FromTxt | Sticker | Goto | Pi | Delay
    print ("")
    global delay
    mode = input ('Enter a mode (Type "help" for help) : ')
    if (mode.lower() == 'Fibonacci' or mode.lower() == 'consecutive' or mode.lower().split(' ')[0] == 'textspam' or mode.lower() == 'sticker' or mode.lower() == 'power' or mode.lower() == 'fibonacci'):
        isint = False
        while (isint == False):
            try:
                count = int(input('Enter the amount of messages : '))
                isint = True
            except:
                print ('Thats not a number...')
        

    if (mode.lower() != 'help' and mode.lower() != 'goto' and mode.lower() != 'exit'):
        msg_box = driver.find_element_by_xpath('//div[@data-tab="6"]')

    def send (msg, s):
        if (msg != ''):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_1E0Oz')
            button.click()
            if (s > 0):
                time.sleep(s)

    if (mode.lower().split (' ')[0] == "textspam"):
        phmode = False
        if (len(mode.lower().split(' ')) > 1):
            if (mode.lower().split(' ')[1] == '-p'):
                phmode = True
        msg = input ('Enter text : ')
        for i in range(count):
            if (phmode == True):
                date = datetime.datetime.now()
                message = msg.replace ("$SECOND", str(date.second)) .replace("$MINUTE", str(date.minute)).replace ("$HOUR", str(date.hour)).replace ("$DAY", str(date.day)).replace ("$MONTH", str(date.month)).replace ("$YEAR", str(date.year))
            else:
                message = msg
            send(message, delay)
    elif (mode.lower() == 'pi'):
        send (str(pi)[0:int(input('Number of digits : '))], delay)
    elif (mode.lower() == 'consecutive'):
        startingnum = int(input ('Starting on : '))
        num = startingnum
        for i in range(count):
            send (str (num), delay)
            num += 1
    elif (mode.lower() == 'power'):
        power = int (input ('Power of : '))
        n = power
        for i in range(count):
            send (str (n), delay)
            n = n*power
    elif (mode.lower() == 'fibonacci'):
        a = 1
        b = 1
        mode = 'a'
        for i in range(count):
            if (mode == 'a'):
                send (str(a), delay)
                mode = 'b'
                a = a+b
            elif (mode == 'b'):
                send (str(b), delay)
                mode = 'a'
                b = a+b
    elif (mode.lower() == 'send'):
        msg = input ('Type the message : ')
        send (msg, 0)
    elif (mode.lower().split(' ')[0] == 'fromtxt'):
        
        file = open (input('Type the name of the file (Current dir, no ".txt") : ') + ".txt")
        
        msg = re.sub(' +', ' ', file.read()).replace ("\n", "")
        
        words = msg.split (" ")
        for i in range(len(words)):
            if (words[i].isspace()):
                send("-", delay)
            else:
                send (words[i], delay)
    elif (mode.lower() == 'goto'):
        chat = input("Insert the name of the group/chat : ")
        try:
            driver.find_element_by_xpath('//span[@title = "{}"]'.format(chat)).click()
        except:
            print('Unable to find element "' + chat + '"')

    elif (mode.lower() == 'sticker'):
        classname = input('Sticker url (blob:https://web.whatsapp...) : ')
        print (classname)
        
        sticker = driver.find_element_by_xpath('//img[@src="' + classname + '"]')
        for i in range(count):
            sticker.click()
    elif (mode.lower () == 'delay'):
        try:
            n = float(input('Set delay (seconds) : '))
            if (n > 0):
                delay = n
            elif (n == 0):
                delay = 0
            else:
                print ('Enter a number higher than 0!')
        except:
            print ('That\'s not a number!')
    elif (mode.lower () == 'custom'):
        exec(open(input ('Type the name of the file (Current dir, no ".txt") : ') + '.txt', 'r').read())
    elif (mode.lower() == 'help'):
        print ('''First run the script

Connect to web.whatsapp.com and enter a chat (group/private)

Select an option (Fibonacci | Power | Consecutive | TextSpam | Send | FromTxt | Sticker | Goto | Pi | Delay | Custom)

Follow the steps

----------------------------------------------------------------------------------------------------------------

For Sticker option:

You need to press F12 or enter inspect mode and Inspect the sticker you want. There is gonna be a <img src="blob:https://web.whatsapp.com/RANDOMCHARS"> where you copy blob:https://web.whatsapp.com/RANDOMCHARS and paste it into the sticker url

----------------------------------------------------------------------------------------------------------------

For textspam -p option:

You can add placeholders to your message ($YEAR, $MONTH, $DAY, $HOUR, $MINUTE, $SECOND)

----------------------------------------------------------------------------------------------------------------

For custom option:

You need a .txt file containing python code. The method send(message, delay) can be used. Other declared variables will work as well

''')
        
    else:
        print ("That's not implemented yet...")

    main ()

    

main()

