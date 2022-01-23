import scan_config as g
import requests
import time



def bnb(A):
    response = requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+ A +"&tag=latest&apikey="+ g.API_bsc)
    R=response.json()
    v=int(R['result'])*(10**(-18))
    return v
def latest_erc20_bsc(A):
    ts = time.time()
    w=requests.get("https://api.bscscan.com/api?module=block&action=getblocknobytime&timestamp="+str(int(ts))+"&closest=before&apikey="+g.API_bsc)
    Bg=w.json()
    block_start=int(Bg['result'])
    block_end=10000000000000000
    while True :
            z=requests.get("https://api.bscscan.com/api?module=account&action=tokentx&address="+A+"&startblock="+str(block_start)+"&endblock="+str(block_end)+"&sort=asc&apikey="+g.API_bsc)
            O=z.json()
            time.sleep(5)
            if O['result']!=[]:
            	for i in range (len(O['result'])-1):
            		D=O['result'][i]
            			if D['to']==A:
            				v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            				t=D['tokenName']
            				j=D['timeStamp']
            				msg2= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"bsc: U bought: "+ str(v) +"  "+str(t)+"Balance bnb:"+str(bnb(A)))
            				block_start=(int(D['blockNumber'])+1)
            				time.sleep(1)
            			elif D['from']==A:
            				v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            				t=D['tokenName']
            				j=D['timeStamp']
            				msg3= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"bsc: U sold: "+ str(v) +"  "+ str(t)+"Balance bnb:"+str(bnb(A)))
            				block_start=(int(D['blockNumber'])+1)
            				time.sleep(1)      
    return
latest_erc20_bsc(g.SCAN)
