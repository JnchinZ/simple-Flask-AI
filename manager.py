from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import baidu_ai
import change_type
import tuling

app = Flask(__name__)  # type:Flask


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload_audio",methods=["GET","POST"])  # 上传音频文件(非PCM格式)
def upload():
    file_info = request.values.to_dict()
    # print(file_info)
    file_name = file_info["name"]  # 前端获取文件名
    user_id = file_info["user_id"]  # 前端获取User_id

    audio_file = request.files["file"] # 历史录音文件
    # print(audio_file)
    audio_file.save("static/audio_file/%s" % (file_name))

    #进行人工智能的处理
    # 转成pcm音频文件
    new_file_name = change_type.anthing2pcm(file_name)
    # 音频转文字
    questions = baidu_ai.audio2text(new_file_name)
    # 文字逻辑处理
    if questions[-4:] == '.mp3':
        result_voice_file_name = questions
    else:
        result_voice_file_name = baidu_ai.nlp_simnet(questions)
        if result_voice_file_name == None:
            answer = tuling.to_tuling(questions)
            # 文字转音频
            result_voice_file_name = baidu_ai.text2audio(answer)


    # 返回信息
    ret_str = {
        "play_type": "talk",
        "res_name": result_voice_file_name,  # 被播放的文件名
    }

    # jsonify()是将字典数据类型转换成标准的json字符串格式
    return jsonify(ret_str)


app.run('localhost', 5000, debug=True)
