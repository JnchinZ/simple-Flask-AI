from aip import AipNlp
from aip import AipSpeech
import time

""" 你的 APPID AK SK """
APP_ID = '11520798'
API_KEY = '2QVVOd6SLL8yGud0VG7MBnHg'
SECRET_KEY = 'giIgPaYZcAhsZns8arP6qK5dTf6FGiZy'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

client1 = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def text2audio(words):
    my_voice = {
        'per': 1,
        'spd': 4,
        'plt': 8,
        'vol': 10
    }
    res = client.synthesis(words, 'zh', 1, my_voice)
    result_voice = str(time.time())+'.mp3'
    with open(r'./static/audio_file/'+result_voice, 'wb') as f:
        f.write(res)
    return result_voice

def audio2text(file_name):
    with open(file_name, 'rb') as f:
        voice = f.read()

    # 识别本地文件
    res = client.asr(voice, 'pcm', 16000, {
        'dev_pid': 1536,  # 语言类型
    })
    try:
        words = res['result'][0]
    except:
        words = input('please input your question by hands:')
        # words = (words, 'what.mp3')
    else:
        print('your question:',words)
    return words

def nlp_simnet(b = '来首歌'):
    a = '你能唱首歌吗'
    res = client1.simnet(a, b)
    if res['score'] > 0.7:
        return 'ayok.mp3'
    else:
        return None
    pass