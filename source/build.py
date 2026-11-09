# Inline source/images into a self-contained ../index.html: python3 source/build.py
import base64, os, re
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'index.html'), encoding='utf-8').read()
def rep(m):
    f = os.path.join(here, 'images', m.group(1))
    mime = 'image/png' if f.endswith('.png') else 'image/jpeg'
    return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(open(f, 'rb').read()).decode())
out = re.sub(r'src="images/([^"]+)"', rep, src)
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(out)
print('built', len(out) // 1024, 'KB')
