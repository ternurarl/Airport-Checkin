import requests
import json
import os

requests.packages.urllib3.disable_warnings()
SCKEY = os.environ.get('SCKEY')
TG_BOT_TOKEN = os.environ.get('TGBOT')
TG_USER_ID = os.environ.get('TGUSERID')


def checkin(email=os.environ.get('EMAIL'), password=os.environ.get('PASSWORD'),
            base_url=os.environ.get('BASE_URL'), ):
    if not all([email, password, base_url]):
        missing = []
        if not email: missing.append("EMAIL")
        if not password: missing.append("PASSWORD")
        if not base_url: missing.append("BASE_URL")
        raise ValueError(f"缺少环境变量: {', '.join(missing)}")

    # 验证邮箱格式
    if "@" not in email:
        raise ValueError(f"邮箱格式错误: {email} (缺少@符号)")

   
    email_part = email.split('@')
    email_encoded = email_part[0] + '%40' + email_part[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/user-login.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email_encoded + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Referer': base_url + '/user-login.htm'
    }
    response = session.post(base_url + '/sg_sign.htm', headers=headers,
                            verify=False)
    response = json.loads(response.text)
    print(response['msg'])
    return response['msg']


result = checkin()
if SCKEY != '':
    sendurl = 'https://sctapi.ftqq.com/' + SCKEY + '.send?title=机场签到&desp=' + result
    r = requests.get(url=sendurl)
if TG_USER_ID != '':
    sendurl = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={TG_USER_ID}&text={result}&disable_web_page_preview=True'
    r = requests.get(url=sendurl)
