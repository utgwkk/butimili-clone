# coding: utf-8
import os
import re
from urllib.parse import quote
from bottle import Bottle, run, redirect

app = Bottle()

TEMPLATE_TXT = '{} うおおおおおおあああああああああああああああああああ！！！！！！！！！！！ (ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ！！！！！！！)'
TEMPLATE_URL = 'https://twitter.com/intent/tweet?text={}'

def list_filter(config):
    delimiter = config or r'[/\+]'
    regexp = r'@?[0-9a-zA-Z_]+({}@?[0-9a-zA-Z_]+)*/*'.format(delimiter)

    def to_py(match):
        return [x.replace('@', '') for x in re.split(delimiter, match)
                                   if len(x) > 0]
    def to_url(strs):
        return delimiter.join(strs)

    return regexp, to_py, to_url

app.router.add_filter('list', list_filter)

@app.route('/<targets:list>')
def butimili(targets):
    replies = '@' + ' @'.join(targets)
    return redirect(TEMPLATE_URL.format(quote(TEMPLATE_TXT.format(replies))))


if __name__ == '__main__':
    run(app,
        host=os.environ.get('BUTIMILI_HOST', 'localhost'),
        port=os.environ.get('BUTIMILI_PORT', 8080),)
