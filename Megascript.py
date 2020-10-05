from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

print ("")
print ("-------------------------------------------------------")
print ("- [MEGA-SCRIPT] - By BlendyDev (github.com/blendydev) -")
print ("-------------------------------------------------------")
print ("")
print ("# FIRST SELECT A CONTACT/GROUP TO MESSAGE ON WHATSAPP WEB #")


def main ():
    print ("")
    mode = input ('Enter a mode (Fibonacci | Power | Consecutive | TextSpam | Send | FromTxt | Sticker) : ')
    if (mode.lower() != 'send' and mode.lower() != 'fromtxt'):
        count = int(input('Enter the amount of messages : '))

    input('Enter anything after on group after scanning QR code')



    msg_box = driver.find_element_by_xpath('//div[@data-tab="1"]')

    def send (msg):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()

    if (mode.lower() == "textspam"):
        msg = input ('Enter text : ')
        for i in range(count):
            send(msg)
    elif (mode.lower() == 'consecutive'):
        startingnum = int(input ('Starting on : '))
        num = startingnum
        for i in range(count):
            send (str (num))
            num += 1
    elif (mode.lower() == 'power'):
        power = int (input ('Power of : '))
        n = power
        for i in range(count):
            send (str (n))
            n = n*power
    elif (mode.lower() == 'fibonacci'):
        a = 1
        b = 1
        mode = 'a'
        for i in range(count):
            if (mode == 'a'):
                send (str(a))
                mode = 'b'
                a = a+b
            elif (mode == 'b'):
                send (str(b))
                mode = 'a'
                b = a+b
    elif (mode.lower() == 'send'):
        msg = input ('Type the message : ')
        send (msg)
    elif (mode.lower() == 'fromtxt'):
        file = open (input('Type the name of the file (Current dir, no ".txt") : ') + ".txt")
        msg = re.sub(' +', ' ', file.read()).replace ("\n", "")
        words = msg.split (" ")
        for i in range(len(words)):
            if (words[i].isspace()):
                send("-")
            else:
                send (words[i])
    elif (mode.lower() == 'sticker'):
        classname = input('Sticker url (blob:https://web.whatsapp...) : ')
        print (classname)
        
        sticker = driver.find_element_by_xpath('//img[@src="' + classname + '"]')
        for i in range(count):
            sticker.click()
        
    else:
        print ("That's not implemented yet...")

    main ()

    

main()

