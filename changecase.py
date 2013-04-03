#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
import re, sys
from xml.sax.saxutils import escape
from titlecase import titlecase

if len(sys.argv) > 1 and len(sys.argv[1].strip()):
	text = sys.argv[1]
else:
	text = sys.stdin.read()

def hacky_titlecase(text):
  """The titlecase module assumes words in all UPPERCASE should be ignored.
  This works for words like HTML, FYI, ID, etc., but not generally.
  Just work around for now by going to .lower first. We need a whitelist of
  good words I guess."""
  return titlecase(text.lower())

variations = {
  'lower': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ),
  'upper': escape(text.upper(), {'"': '&quot;', '\n': '&#10;'} ),
  'title': escape(hacky_titlecase(text), {'"': '&quot;', '\n': '&#10;'} )
}

print """<?xml version="1.0"?>
<items>
  <item uid="changecase-lower" arg="%(lower)s">
    <title>%(lower)s</title>
    <subtitle>Lowercase</subtitle>
    <icon>lowercase.png</icon>
  </item>
  <item uid="changecase-upper" arg="%(upper)s">
    <title>%(upper)s</title>
    <subtitle>Uppercase</subtitle>
    <icon>uppercase.png</icon>
  </item>
  <item uid="changecase-title" arg="%(title)s">
    <title>%(title)s</title>
    <subtitle>Title Case</subtitle>
    <icon>titlecase.png</icon>
  </item>
</items>""" % variations
