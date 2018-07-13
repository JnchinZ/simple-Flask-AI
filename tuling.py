import requests
import json
# import win32com.client
#
# def speak(words):
#     spk = win32com.client.Dispatch("SAPI.SpVoice")
#     spk.Speak(words)

# 使用图灵机器人接口回答
def to_tuling(questions):
    tuling_str = {'key':'f45eae2b62664b12bfc72efb6a57cdd0',
                 'info':questions
                 }

    res = requests.post('http://www.tuling123.com/openapi/api',data=tuling_str)
    res_dict = json.loads(res.content)
    answer = res_dict['text']
    print('robot:',answer)
    return answer