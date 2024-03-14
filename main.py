import os
import requests


# 获取早报信息
def get_news():
    alapi_token = os.getenv('alapi_token')
    url = 'https://v2.alapi.cn/api/zaobao'
    params = {'token': alapi_token}
    response = requests.get(url, params=params)
    data = response.json()
    if data.get('code') == 200:
        return data.get('data')
    else:
        print(data.get("msg"))
        return None


# 推送消息
def push_message(title, content):
    wpush_apikey = os.getenv('wpush_apikey')
    url = 'https://api.wpush.cn/api/v1/send'
    channel = os.getenv("channel", "wechat")
    if channel not in ["wechat", "sms", "mail", "feishu", "dingtalk", "webhook", "wechat_work"]:
        channel = "wechat"

    params = {'apikey': wpush_apikey, 'title': title, 'content': content, 'channel': channel}
    response = requests.post(url, data=params)
    data = response.json()
    if data.get("code") == 0:
        return True
    else:
        print(data.get("message"))
        return False


# 主函数
def main():
    if not os.getenv('alapi_token') or not os.getenv('wpush_apikey'):
        print('请设置alapi_token和wpush_apikey环境变量！')
        return
    send_type = os.getenv("type", "image")

    if send_type not in ["image", "text"]:
        send_type = "image"

    news_data = get_news()
    if news_data:
        date = news_data.get('date')
        news_list = news_data.get('news')
        image_url = news_data.get('image')

        title = '每日60秒早报'
        content = f'### 日期：{date}\n\n'

        if send_type == "image":
            content += f'![image]({image_url})'
        else:
            content += '#### 新闻：\n'
            for news in news_list:
                content += f'- {news}\n'

        if push_message(title, content):
            print('消息推送成功！')
        else:
            print('消息推送失败！')
    else:
        print('获取早报信息失败！')


if __name__ == '__main__':
    main()
