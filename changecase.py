import re, sys
from xml.sax.saxutils import escape
# from xml.sax.saxutils import quoteattr

skip_words = ['a', 'and', 'an', 'the', 'or']

def title_case(text):
  first = [True]
  def some_titles(m):
    text = m.group()
    if first[0]:
      first[0] = False
      return text.capitalize()
    elif text in skip_words:
      return text
    else:
      return text.capitalize()
  return re.sub(r'\w+', some_titles, text)

if len(sys.argv) > 1 and len(sys.argv[1].strip()):
	text = sys.argv[1]
else:
	text = sys.stdin.read()

variations = {
  'lower': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ),
  'upper': escape(text.upper(), {'"': '&quot;', '\n': '&#10;'} ),
  'title': escape(title_case(text), {'"': '&quot;', '\n': '&#10;'} )
}

print """<?xml version="1.0"?>
<items>
  <item uid="changecase-lower" arg="%(lower)s" type="file">
    <title>%(lower)s</title>
    <subtitle>Lowercase</subtitle>
  </item>
  <item uid="changecase-upper" arg="%(upper)s" type="file">
    <title>%(upper)s</title>
    <subtitle>Uppercase</subtitle>
  </item>
  <item uid="changecase-title" arg="%(title)s" type="file">
    <title>%(title)s</title>
    <subtitle>Title Case</subtitle>
  </item>
</items>""" % variations
