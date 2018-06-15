from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

import requests,json,time,re
#获取二维码随机字符串
# https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}

# https://login.weixin.qq.com/qrcode/{0}  二维码地址

#等待时请求地址
# https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}==&tip=0&r=1923237225&_={1}
def check(req):
    if req.method=='GET':
        response={}
        uuid_time=int(time.time()*1000)
        uuid_url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(uuid_time)
        r1=requests.get(uuid_url)
        uuid=re.findall('uuid = "(.*)";',r1.text)
        # print(uuid[0])
        response['uuid']=uuid[0]
        req.session['uuid']=uuid[0]
        req.session['uuid_time'] = uuid_time
        return render(req,'login.html',response)

def check_login(req):

    response = {}
    ctime = int(time.time() * 1000)
    base_url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=1919962222&_={1}".format(req.session['uuid'],ctime)
    print(base_url)
    r2=requests.get(base_url)
    print(r2.text)
    if "window.code=400;" in r2.text:
        '''无人扫码时候'''
        response['code']=408
    elif "window.code=201;" in r2.text:
        '''扫码了，但未确认'''
        response['code']=201
        user_avat=re.findall("window.userAvatar = '(.*)';",r2.text)[0]
        response['data']=user_avat              #头像地址
    elif "window.code=200;" in r2.text:
        '''扫码确认了，返回地址'''\
        '''但返回的地址是不全'''
        """window.redirect_uri="https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=A9DN2Fq0BjErYC9f_khB9Rxw@qrticket_0&uuid=YePytZqWog==&lang=zh_CN&scan=1527215409";"""
        '''比较全的地址，后面还有fun=new&version=v2
           https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=A0ZqOUpHNLqWWLSlIR20uYwp@qrticket_0&uuid=Ybv2yi2xrA==&lang=zh_CN&scan=1527217355&fun=new&version=v2
        '''
        req.session['LOGIN_COOKIE']=r2.cookies.get_dict()
        base_redirect_url=re.findall('redirect_uri="(.*)"',r2.text)[0]
        redirect_url=base_redirect_url+"&fun=new&version=v2"

        '''通过该地址获取凭证'''
        r2=requests.get(redirect_url)
        print(r2.text)
        from app1.get_cert import ticket
        ticket_dict=ticket(r2.text)
        req.session['TICKED_DICT']=ticket_dict
        req.session['TICKED_COOKIES']=r2.cookies.get_dict()

        #初始化，获取最近联系人信息,初始化信息放在session中
        '''https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=1787147737'''
        init_url='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=1786479806&lang=zh_CN&pass_ticket={0}'.format(ticket_dict['pass_ticket'])
        post_data={
            'BaseRequest':{
                'DeviceID': "e810013791592179",
                'Sid': req.session['TICKED_DICT']['wxsid'],
                'Uin': req.session['TICKED_DICT']['wxuin'],
                'Skey': req.session['TICKED_DICT']['skey'],
            }
        }

        r3=requests.post(url=init_url,
                         json=post_data)
        r3.encoding='utf-8'
        init_dict=json.loads(r3.text)
        print(init_dict)
        for k,i in init_dict.items():
            print(k,i)
        req.session['INIT_DICT']=init_dict
        response['code']=200
    return HttpResponse(json.dumps(response))

def avatar(req):
    '''返回头像'''
    user_img_url=req.GET.get('prev')  #/cgi-bin/mmwebwx-bin/webwxgeticon?seq=971863233
    # img_url = "https：//wx2.qq.com" + user_img_url     #被截断了，所以用以下分段截取
    username=req.GET.get('username')#@21dda1bb204ca7cc9de102f9f5773745b84713cab4d72cbcc266cfd8ea131a68
    skey= req.GET.get('skey')        #@crypt_5975c0bd_ccd523236938e2cbafead50f960c2558
    img_url = "https://wx2.qq.com{0}&username={1}&skey={2}".format(user_img_url,username,skey)

    cookies={}
    cookies.update(req.session['LOGIN_COOKIE'])
    cookies.update(req.session['TICKED_COOKIES'])

    rel = requests.get(url=img_url,cookies=cookies,
                       )                 #竟然不用携带cookies和refer和Content-Type   headers={'Content-Type:': 'image/jpeg'} 'Referer:':'https://wx2.qq.com/?&lang=zh_CN',
    # print(rel.content)
    return HttpResponse(rel.content)
    pass
def index(req):
    '''获取最近联系人'''

    return render(req,'index.html')

def contact_list(req):
    '''所有联系人'''
#     https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=q7fGGuNrs0M4%252BBzMnr7J%252BUo7ns8zz%252FGayBIoQHTgznYiDmAHu%252FVdi3G76uRFdca7&r=1527231326758&seq=0&skey=@crypt_5975c0bd_aa89e1f5abd57d93ba43afc76e12e181
    ctime=str(time.time()*1000)
    pass_ticket=req.session['TICKED_DICT']['pass_ticket']
    skey = req.session['TICKED_DICT']['skey']
    base_url='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r={0}&skey={1}'.format(ctime,skey)
    print(base_url)
    cookies = {}
    cookies.update(req.session['LOGIN_COOKIE'])
    cookies.update(req.session['TICKED_COOKIES'])
    r2=requests.get(base_url,cookies=cookies)
    r2.encoding='utf-8'
    user_list=json.loads(r2.text)
    print(r2.text
          ,user_list)

    return render(req,'contact_list.html',{'userlist':user_list})

def send_msg(req):
    '''发送消息'''
    print('开始')
    ctime = str(time.time() * 1000)
    current_user=req.session['INIT_DICT']['User']['UserName']
    to=req.POST.get('to')
    msg= req.POST.get('msg')
    base_url="https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}".format(req.session['TICKED_DICT']['pass_ticket'])
    post_data = {
        'BaseRequest': {
            'DeviceID': "e810013791592179",
            'Sid':req.session['TICKED_DICT']['wxsid'],
            'Uin': req.session['TICKED_DICT']['wxuin'],
            'Skey': req.session['TICKED_DICT']['skey'],
        },
        'Msg':{
            'ClientMsgId':ctime,
            'Content':msg,
            'FromUserName':current_user,
            'LocalID':ctime,
            'ToUserName':to,
            'Type':1
        }
    }
    # requests.post(url=base_url,json=post_data,ensure_ascii=False)
    ################################################################因为发送数据有中文，所以ensure_ascii=False,变成中文的json字符串，然后再encode('utf-8')发送，小心编码问题
    r3=requests.post(url=base_url,data=json.dumps(post_data,ensure_ascii=False).encode('utf-8'),headers={'Content-Type':'application/json'})               #
    print('ok',r3.text)

    return HttpResponse('...')

def get_msg(req):
    '''长轮询接收消息'''

    ####先检查是否有消息到来
    cookies = {}
    cookies.update(req.session['LOGIN_COOKIE'])
    cookies.update(req.session['TICKED_COOKIES'])
    ctime = str(time.time() * 1000)
    # 'https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin/synccheck?r=1527238836798&skey=%40crypt_5975c0bd_a8290d67fcfd5edff3f54017de7a1056&sid=XRNl7jf1fttdldas&uin=2303829181&deviceid=e432910854227698&synckey=1_674468668%7C2_674468741%7C3_674468728%7C11_674468699%7C1000_1527234962%7C1001_1527235034&_=1527238795670'
    base_url='https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin/synccheck'
    synckey_dict=req.session['TICKED_DICT']['SyncKey']   #
    sy_list=[]
    for item in synckey_dict['List']:
        sy_list.append(item['Key']+'_'+item['Val'])
    sy_key="|".join(sy_list)
    r2=requests.get(base_url,params={
                 'r':ctime,
                 'deviceid': "e810013791592179",
                 'skey': req.session['TICKED_DICT']['skey'],
                 'sid': req.session['TICKED_DICT']['wxsid'],
                 'uin': req.session['TICKED_DICT']['wxuin'],
                 '_':ctime,
                 'synckey':sy_key
                 },cookies=cookies )

    if 'retcode:"0",selector:"0"' in r2.text:
        '''无消息'''
        return HttpResponse('...')
    else:
        '''收到消息'''
        ############再发送请求获取消息内容
        get_msg_url='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid={0}&skey={1}&lang=zh_CN&pass_ticket={2}'.format(req.session['TICKED_DICT']['wxsid'],req.session['TICKED_DICT']['skey'], req.session['TICKED_DICT']['pass_ticket'])
        post_data = {
            'BaseRequest': {
                'DeviceID': "e810013791592179",
                'Sid': req.session['TICKED_DICT']['wxsid'],
                'Uin': req.session['TICKED_DICT']['wxuin'],
                'Skey': req.session['TICKED_DICT']['skey'],
            },'SyncKey':synckey_dict,
        }

        r2=requests.post(url=get_msg_url,
                      json=post_data,
                       cookies=cookies
                         )
        msg_dict=json.loads(r2.text)   #发送过来的消息，里面也包括有新的SyncKey，拿到后要更新SyncKey
        for msg in msg_dict['AddMsgList']:   #所有消息
            print('您有新消息到来',msg['Content'])
        ###### 更新SyncKey
        #先拿到内存里
        init_dict=req.session['INIT_DICT']
        #对内存里的进行赋值
        init_dict['SyncKey']=msg_dict['SyncKey']
        #然后再放在数据库里
        req.session['INIT_DICT']=init_dict      #更新SyncKey

