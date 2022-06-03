
import requests,random,re,ctypes,os,time,colorama,autopy
from termcolor import colored

dir_path = os.path.dirname(os.path.realpath(__file__))
colorama.init()

timestamp = str(int(time.time()))

chars = "qwertyuiopasdfghjklzxcvbnm"

Numbers = "1234567890"

def RandomString(strings,Lenth=10) -> random: return ''.join(random.choice(strings) for i in range(Lenth))
def uuid() -> requests.Response: return requests.get("https://httpbin.org/uuid").text
   



class Design:
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    s1 = '\x1b[36m1\x1b[31m'
    s2 = '\x1b[36m2\x1b[31m'
    one = f"\x1b[31m[{s1}]\x1b[31m"
    tow = f"\x1b[31m[{s2}]\x1b[31m"
    eq = '\x1b[36m≈\x1b[31m'
    eq1 = f"\x1b[31m[{eq}]\x1b[31m"
    equl = '\x1b[36m=\x1b[31m'
    equl1 = f"\x1b[31m[{equl}]\x1b[31m"
    du = '\x1b[36m≠\x1b[31m'
    du1 = f"\x1b[31m[{du}]\x1b[31m"
    plus = '\x1b[36m+\x1b[31m'
    plus2 = '\x1b[32m+\x1b[36m'
    mains = '\x1b[36m-\x1b[31m'
    SL = '\x1b[36m/\x1b[31m'
    INPUT = f"\x1b[31m[ {plus} ]\x1b[31m"
    INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
    INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"
    INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
    marka = '\x1b[32m✓\x1b[36m'
    INPUT3 = f"\x1b[36m[{marka}]\x1b[36m"
    blueq = '\x1b[36m\x1b[40m'
    reda = '\x1b[31m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    purble = '\x1b[35m\x1b[39m'
    SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
    Run = '\x1b[36m Started Running...\x1b[31m'
    under = '\x1b[35m_\x1b[39m'
    skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
    clearConsle = lambda: os.system('cls')
    
    clearTermnal = lambda: os.system('clear')
        

    qube = '['
    qube2 = ']'

    grey = 'gray'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    white = 'white'
    
    right = "Made By Psycho Rayan"
    Banner = """

    
    
        |  \  |   _    |    ____|  | _)        
        |   \ | / _ \  __|  |      |  | \ \  / 
        | |\  |   __/  |    __|    |  |  `  <  
        |_| \_| \___| \__| _|     _| _|  _/\_\ 
            By Rayan IG : @1k3k

"""


def Print(Frist_NewLine,ReadLine,mark,color,text,Last_Line):
    if Frist_NewLine:
        Frist_NewLine = "\n"
    else:
        Frist_NewLine = ""
    if ReadLine:
        ReadLine = "\r"
    else:
        ReadLine = ""
    if Last_Line:
        Last_Line = "\n"
    else:
        Last_Line = ""
    print(f"{Frist_NewLine}{ReadLine}{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)} {Last_Line}",end='')






def LoadFile(name,path):
    try:
        with open(path,"r") as myfile:
            file = myfile.read().splitlines()
    except FileNotFoundError:
        Print(False,False,"/",Design.yellow,f"{name} Path : ",False);pa = input()
        try:
            path2 = re.search(r"'(.*?)'",pa).group(1)
        except:path2 = re.search(r"(.*?)",pa).group(1)
        with open(path2,"r") as myfile:
            file = myfile.read().splitlines()
        #file = [i.strip() for i in open(path2,"r") if i]

    if len(file) <=0:
        Print(False,False,"!",Design.red,f"{name} Empty File",True)
        input()
        exit(0)
    else:
        Print(False,False,f"{len(file)}",Design.green,f"{name} Loaded Successfully ",True)
        return file
    
    
def CrateFile(name,path,text):
    try:
        with open(path,"a") as myfile:
            myfile.write(text)
    except:
        Print(False,False,"!",Design.yellow,f"{name} Error Crate File",False);
    
    if len(text) <=0:
        Print(False,False,"!",Design.red,f"{name} Empty File",True)
        input()
        exit(0)
    else:
        Print(False,False,f"+",Design.green,f"{name} Crated Successfully ",True)
        return myfile   


def MsgBox(Title,text):
    try:
        autopy.alert.alert(f"{text}", f"{Title}")
    except:
        ctypes.windll.user32.MessageBoxW(0, f"{text}", f"{Title}", 0x1000)

