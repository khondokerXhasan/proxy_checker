import requests,json,sys,os,random,time
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime


class proxy_checker():

    def __init__(self):
        self.ses=requests.Session()
        self.loop=0
        self.ok=0
        self.ua=random.choice(['Mozilla/5.0 (Linux; Android 11; A600DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; ZC520KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 YaBrowser/20.4.1.144.00 SA/1 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36','Mozilla/5.0 (X11; CrOS i686 6310.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.94 Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Ilium M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; A10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; XT1635-01 Build/ODNS27.76-12-30-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'])
        self.now=datetime.now().strftime("%d-%B-%Y")
        self.select()
                
    def logo(self):
        os.system('clear')
        print('\t\x1b[38;5;129m ____   ____    ___  __  ____   __')
        print('\t\x1b[38;5;129m|  _ \ |  _ \  / _ \ \ \/ /\ \ / /')
        print('\t\x1b[38;5;129m| |_) || |_) || | | | \  /  \ V /')
        print('\t\x1b[38;5;129m|  __/ |  _ < | |_| | /  \   | |')
        print('\t\x1b[38;5;129m|_|    |_| \_\ \___/ /_/\_\  |_|')
        print()
        print('\t\x1b[38;5;161m    Made by \x1b[38;5;118mkhondoker \x1b[1;92mX \x1b[38;5;118mhasan')
        print('\t\x1b[1;94m    --------------------------')
        print()
        print()    
    
    def select(self):
        self.logo()
        print('\t\x1b[1;93m[\x1b[1;92m1\x1b[1;93m] \x1b[1;93mCheck Socks4')
        print('\t\x1b[1;93m[\x1b[1;92m2\x1b[1;93m] \x1b[1;93mCheck Sock5')
        print('\t\x1b[1;93m[\x1b[1;92m3\x1b[1;93m] \x1b[1;93mDump Proxy')
        print('\t\x1b[1;93m[\x1b[1;92m0\x1b[1;93m] \x1b[1;91mExit')
        option = input('\t\x1b[1;93m[\x1b[1;92m*\x1b[1;93m] Select : \x1b[1;92m')
        if option =='1': self.socks4()
        elif option =='2': self.socks5()
        elif option =='3': self.dump_proxy()
        elif option=='0':exit('')
        else:print('\x1b[1;90m\t Invalid option ');time.sleep(1)       
    
    def socks4(self):
        try:yy=input('\n\t\x1b[1;93m[\x1b[1;92m+\x1b[1;93m] Socks4 File : \x1b[1;92m');non=open(yy,'r').read().splitlines();self.socks4_checker(non)
        except FileNotFoundError:print('\n\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m] \x1b[1;91mFile Not Found !' );time.sleep(1);os.system('clear');self.logo();self.socks4()
    
    def socks4_checker(self,non):
        os.system('clear')
        print('\t\x1b[38;5;29m[      IP       -   Country   ]')
        print('\t\x1b[1;94m--------------------------------')
        with tred(max_workers=50) as khondoker_x_hasan:
	        for isi in non:
	            khondoker_x_hasan.submit(self.run,str(isi))
    
    def run(self,isi):
        sys.stdout.write('\r\r\t\033[1;37m [SOCKS-4] %s|\033[1;33mActive: - \x1b[1;92m %s\r\r'%(self.loop,self.ok));sys.stdout.flush()
        self.loop+=1
        try:
	        socks4 = {"https": f"socks4://{isi}","http": f"socks4://{isi}"}
	        data = self.ses.get("https://ipinfo.io/json",proxies=socks4,timeout=5,headers={'User-Agent':f'{self.ua}'}).json()
	        country=data["country"]
	        ip=data["ip"]
	        print('\t\033[1;92m  '+str(ip)+'   -   \033[1;93m'+str(country)+'\033            ')
	        ses.close()
	        os.system(f'touch proxy/{self.now}_active_socks4.txt')
	        y=open(f'proxy/{self.now}_active_socks4.txt','r').read()
	        if str(isi) not in str(y):open(f'proxy/{self.now}_active_socks4.txt','a').write(str(isi)+'\n')
	        else:pass
	        self.ok+=1
        except Exception as e:pass
    
    def socks5(self):
        try:yy=input('\n\t\x1b[1;93m[\x1b[1;92m+\x1b[1;93m] Socks5 File : \x1b[1;92m');non=open(yy,'r').read().splitlines();self.socks5_checker(non)
        except FileNotFoundError:print('\n\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m] \x1b[1;91mFile Not Found !' );time.sleep(1);os.system('clear');self.logo();self.socks5()
        
    def socks5_checker(self,non):
        os.system('clear')
        print('\t\x1b[38;5;29m[      IP       -   Country   ]')
        print('\t\x1b[1;94--------------------------------')
        with tred(max_workers=50) as khondoker_x_hasan:
	        for isi in non:
	            khondoker_x_hasan.submit(self.run1,str(isi))
    def run1(self,isi):
        sys.stdout.write('\r\r\t\033[1;37m [SOCKS-5] %s|\033[1;33mActive: - \x1b[1;92m %s\r\r'%(self.loop,self.ok));sys.stdout.flush()
        self.loop+=1
        try:
	        socks5 = {"https": f"socks5://{isi}","http": f"socks5://{isi}"}
	        ses=requests.Session()
	        data = self.ses.get("https://ipinfo.io/json",proxies=socks5,timeout=5,headers={'User-Agent':f'{self.ua}'}).json()
	        country=data["country"]
	        ip=data["ip"]
	        print('\t\033[1;92m  '+str(ip)+'   -   \033[1;93m'+str(country)+'\033            ')
	        ses.close()
	        os.system(f'touch proxy/{self.now}_active_socks5.txt')
	        y=open(f'proxy/{self.now}_active_socks5.txt','r').read()
	        if str(isi) not in str(y):open(f'proxy/{self.now}_active_socks5.txt','a').write(str(isi)+'\n')
	        else:pass
	        self.ok+=1
        except Exception as e:pass
    
    def dump_proxy(self):
        link_prox=[
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
            "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxyscan.io/download?type=socks4",
            "https://api.openproxylist.xyz/socks4.txt",
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all',
            'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt'
        ]
        link_proxz=[
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.proxyscan.io/download?type=socks5",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
            'https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
        ]
        print('\n\t\x1b[1;93m[\x1b[1;92m DUMPING SOCKS-4 \x1b[1;93m]')
        open("dump/socks4.txt","w").flush()
        for link in link_prox:
            all_prox = self.ses.get(link).text
            open("dump/socks4.txt","a").write(str(all_prox)+'\n')
        
        print('\n\t\x1b[1;93m[\x1b[1;92m DUMPING SOCKS-5 \x1b[1;93m]')
        open("dump/socks5.txt","w").flush()
        for linkz in link_proxz:
            all_proxz = self.ses.get(linkz).text
            open("dump/socks5.txt","a").write(str(all_proxz)+'\n')
        print('Socks4 saved in : dump/socks4.txt')
        print('Socks5 saved in : dump/socks5.txt')
	
proxy_checker()