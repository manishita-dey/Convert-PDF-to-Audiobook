import requests
import voicerss_tts
import playsound

API_KEY = '084ab285efc54b498223f64d9d21f1b2'
# ENDPOINT = 'https://api.voicerss.org/'

# response = requests.get('http://api.voicerss.org/?key=084ab285efc54b498223f64d9d21f1b2&hl=en-us&src=Hello, world!')
response = requests.get('http://api.voicerss.org/?key=084ab285efc54b498223f64d9d21f1b2&hl=en-us&c=MP3&f=16khz_16bit_stereo&src=Hello, world!')
# print(response.text)
playsound.playsound(response, True)

# voice = voicerss_tts.speech({
#     'key': API_KEY,
#     'hl': 'en-us',
#     'v': 'Linda',
#     'src': 'Hello, world!',
#     'r': '0',
#     'c': 'mp3',
#     'f': '44khz_16bit_stereo',
#     'ssml': 'false',
#     'b64': 'true'
# })
#
# print('<audio src="' + voice['response'] + '" autoplay="autoplay"></audio>')
