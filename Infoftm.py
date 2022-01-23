import scan_config as g
import requests
import time

def ftm(A):
    response = requests.get("https://api.ftmscan.com/api?module=account&action=balance&address="+A+"&tag=latest&apikey="+g.API_ftm)
    R=response.json()
    v=int(R['result'])*(10**(-18))
    return v
def latest_erc20_ftm(A):
    ts = time.time()
    w=requests.get("https://api.ftmscan.com/api?module=block&action=getblocknobytime&timestamp="+str(int(ts))+"&closest=before&apikey="+g.API_ftm)
    Bg=w.json()
    block_start=int(Bg['result'])
    block_end=100000000000000000000000000
    while True :
            z=requests.get("https://api.ftmscan.com/api?module=account&action=tokentx&address="+A+"&startblock="+str(block_start)+"&endblock="+str(block_end)+"&sort=asc&apikey="+g.API_ftm)
            O=z.json()
            time.sleep(5)
            if O['result']!=[]:
            	for i in range (len(O['result'])-1):
            		D=O['result'][i]
            		if D['to']==A:
            			v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            			t=D['tokenName']
            			j=D['timeStamp']
            			msg2= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"U bought: "+ str(v) +"  "+str(t)+"Balance ftm:"+str(ftm(A)))
            			block_start=(int(D['blockNumber'])+1)
            			time.sleep(1)
            		elif D['from']==A:
            			v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            			t=D['tokenName']
            			j=D['timeStamp']
            			msg3= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"U sold: "+ str(v) +"  "+ str(t)+"Balance ftm:"+str(ftm(A)))
            			block_start=(int(D['blockNumber'])+1)
            			time.sleep(1)
    return 
latest_erc20_ftm(g.SCAN)

