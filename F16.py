print ("MAFIA SCRIPT")
import requests,uuid,secrets
from time import sleep
print ('join my group')
sleep(2)
print ('https://t.me/MAFIA_TEAM4')
uid = uuid.uuid4()
r = requests.Session()
cookie = secrets.token_hex(8)*2
print ("IG / report")
print ("tele » @Ft_r5")
username = input('username (fake)===»:')
password = input('password ===»:')
target = input('victim===»:')
sle = int(input('sleep (ex:20,15,10)===»:'))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('login True')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':1,'frx_context':''} #fire
            report = r.post(url_report,data=datas)
            print('fireeee {}'.format(done))
            sleep(sle)
            done += 1
    else:
        print('login false')
        exit()

login()

