# to test this script tun it with
#python youtube.py 'http://www.youtube.com/watch?v=hIPoRdfbsYs' test.flv
#import lxml.html
import re
import sys
import urllib
import urllib2

_RE_G204 = re.compile('"(http:.+.youtube.com.*\/generate_204[^"]+")', re.M)
_RE_URLS = re.compile('"fmt_url_map": "(\d*[^"]+)",.*', re.M)

def _fetch_url(url, ref=None, path=None):
    opener = urllib2.build_opener()
    headers = {}
    if ref:
        headers['Referer'] = ref
    request = urllib2.Request(url, headers=headers)
    handle = urllib2.urlopen(request)
    if not path:
        return handle.read()
    sys.stdout.write('saving: ')
    # write result to file
    with open(path, 'wb') as out:
        while True:
            part = handle.read(65536)
            if not part:
                break
            out.write(part)
            sys.stdout.write('.')
            sys.stdout.flush()
        sys.stdout.write('\nFinished.\n')

def _extract(html):
    try:
       import lxml.html
    except :
       print "install lxml "
    tree = lxml.html.fromstring(html)
    res = {'204': _RE_G204.findall(html)[0].replace('\\', '')}
    for script in tree.findall('.//script'):
        text = script.text_content()
        if 'fmt_url_map' not in text:
            continue
        # found it, extract the urls we need
        for tmp in _RE_URLS.findall(text)[0].split(','):
            url_id, url = tmp.split('|')
            res[url_id] = url.replace('\\', '')
        break
    return res

def main():
    target = sys.argv[1]
    dest = sys.argv[2]
    html = _fetch_url(target)
    res = dict(_extract(html))
    # hit the 'generate_204' url first and remove it
    _fetch_url(res['204'], ref=target)
    del res['204']
    # download the video. now i grab the first 'download' url and use it.
    first = res.values()[0]
    _fetch_url(first, ref=target, path=dest)

if __name__ == '__main__':
    main()
