import os

"""
cmd = "ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s"%(
    "name.m4a",
    "audio.pcm"
)
"""

# 音频转码
def anthing2pcm(old_code, new_code = 'audio'):
    root_path = r'./static/audio_file/'
    old_code = root_path+old_code
    new_code = root_path+new_code+'.pcm'
    shell_str = 'ffmpeg -y  -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s'%(old_code, new_code)
    os.system(shell_str)
    return  new_code