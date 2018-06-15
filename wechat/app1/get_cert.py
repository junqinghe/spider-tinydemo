# scode='''<error>
#     <ret>0</ret>
#     <message></message>
#     <skey>@crypt_5975c0bd_db02723089792bab12d0b7669d8ce01c</skey>
#     <wxsid>xHnHrpBSJChRX8J9</wxsid>
#     <wxuin>2303829181</wxuin>
#     <pass_ticket>dFnZurJrAbD2KRVgwk8hPdXnvAF%2Bhb3sjLZSZrWoe4WpgQabRkgdqhoUrjsHPP8S</pass_ticket>
#     <isgrayscale>1</isgrayscale>
# </error>
# '''

def ticket(scode):
    '''验证信息格式化'''
    from bs4 import BeautifulSoup
    ret={}
    soup=BeautifulSoup(scode,'html.parser')
    for tag in soup.find(name='error').find_all():
        ret[tag.name]=tag.text
    return ret
