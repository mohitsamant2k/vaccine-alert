import requests
import time
import datetime
from datetime import timedelta
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
already_done=[]




while(True):
   
    
    today=datetime.date.today()
    # dates=today.strftime('%d-%m-%Y')
    zz=1
    for i in range(15): 
        time.sleep(1)
        now_dates=today+timedelta(days=i)
        
        now_dates=now_dates.strftime('%d-%m-%Y')
        print(now_dates)
        now_dates=str(now_dates)
        
        try:
         
            request=requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=263139&date={now_dates}",headers=headers)
            
            p=request.status_code
            
            
                
            if(zz==1):
                pp= requests.get(f"https://api.telegram.org/bot1809999872:AAEFuNFngQMjqpUs3bbG_VR2alnmu8bk-9I/sendMessage?chat_id=-1001329516656&text={p}")
            zz=0
            if(p==200):
                sessions=request.json()["sessions"]
                
                for session in sessions:
                   if(session["session_id"] not in already_done):
                        # already_done.append(session["session_id"])
                        name=session["name"]
                        address=session["address"]
                        dose1=session.get("available_capacity_dose1",0)
                        dose2=session.get("available_capacity_dose2",0)
                        min_age_lim=session.get("min_age_limit",18)
                        vaccine=session.get("vaccine")
                        text=f"""
                            dates={now_dates}
name ={name}\n
address={address}\n
dose1={dose1}\n
dose2={dose2}\n
min_age_lim={min_age_lim}\n
vaccine={vaccine}\n
                        """
                        if(dose1+dose2 > 0 and min_age_lim==18):
                            pp= requests.get(f"https://api.telegram.org/bot1809999872:AAEFuNFngQMjqpUs3bbG_VR2alnmu8bk-9I/sendMessage?chat_id=-1001495012017&text={text}")


                
        except:
            print('fail')
    time.sleep(30)
 
        
