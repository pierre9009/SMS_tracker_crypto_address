import scan_config as g
import requests
import time


def avax(A):
    response = requests.get("https://api.snowtrace.io/api?module=account&action=balance&address="+ A +"&tag=latest&apikey="+ g.API_avax)
    R=response.json()
    v=int(R['result'])*(10**(-18))
    return v
def latest_erc20_avax(A):
    ts = time.time()
    w=requests.get("https://api.snowtrace.io/api?module=block&action=getblocknobytime&timestamp="+str(int(ts))+"&closest=before&apikey="+g.API_avax)
    Bg=w.json()
    block_start=int(Bg['result'])
    block_end=10000000000000000
    while True :
            z=requests.get("https://api.snowtrace.io/api?module=account&action=tokentx&address="+A+"&startblock="+str(block_start)+"&endblock="+str(block_end)+"&sort=asc&apikey="+g.API_avax)
            O=z.json()
            ts = time.time()
            time.sleep(25)
            if O['result']!=[]:
            	for i in range (len(O['result'])-1):
            		D=O['result'][i]
            		if D['to']==A:
            			v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            			t=D['tokenName']
            			j=D['timeStamp']
            			msg2= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"Avalanche: U bought:"+ str(v) +"  "+str(t)+" Balance avax: "+str(avax(A)))
            			block_start=(int(D['blockNumber'])+1)
            			time.sleep(1)
            		elif D['from']==A:
            			v=int(D['value'])*(10**(-int(D['tokenDecimal'])))
            			t=D['tokenName']
            			j=D['timeStamp']
            			msg3= requests.get("https://smsapi.free-mobile.fr/sendmsg?user="+g.User_free+"&pass="+g.API_free+"&msg="+"Avalanche: U sold: "+ str(v) +"  "+ str(t)+" Balance avax:"+str(avax(A)))
            			block_start=(int(D['blockNumber'])+1)
            			time.sleep(1)
    return 
latest_erc20_avax(g.SCAN)
