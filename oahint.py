import requests
import json
 
def bot(robot_webhook,text):
    # 构建消息内容
    message_data = {
        "msgtype": "text",
        "text": {
            "content": text,
            "mentioned_list": ["@all"]
        }
    }
    # 发送请求
    response = requests.post(robot_webhook, headers={"Content-Type": "application/json"}, data=json.dumps(message_data))
 
    # 检查响应状态码
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print(f"消息发送失败，状态码：{response.status_code}")
if __name__ == '__main__':
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ce352bce-d4ac-40c8-bd84-25c45f96e44b'
    text = "定时提醒：个人日报填报"
    bot(url, text)