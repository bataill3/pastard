from sys import argv
import options
import requests
pastard, *args = argv

prompt = '-> '
api_dev_key = '' # You can get your key from pastebin.com
FILE, TITLE = options.check(args)

if FILE != 'NONE':
    SOURCE = open(FILE)
    API_PASTE_CODE = SOURCE.read()
    SOURCE.close()
else:
    print('Paste your paste!')
    API_PASTE_CODE = input(prompt)

parameters = {'api_dev_key': api_dev_key, 'api_option': 'paste', 'api_paste_code': API_PASTE_CODE}
if TITLE != 'NONE':
    parameters['api_paste_name'] = TITLE

POST = requests.post('http://pastebin.com/api/api_post.php', data = parameters)

print("Here's your paste: %s" % POST.text)
