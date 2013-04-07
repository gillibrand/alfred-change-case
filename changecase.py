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


always_uppercase = r'''\bXML|HTML|CSS|JSON|FYI|AOL|ATM|BBC|CD|FAQ|GAIM|GNU|GTK|HIRD|HIV
  |HURD|IEEE|IOU|IRA|IUPAC|JPEG|LCD|NAACP|NAC|NATO|NCAA|NOAD|OEM|PHP|ROM|SAT|SFMOMA|SQL|USA|VHDL|VHSIC|W3C
  |LOL|WTF\b'''
always_uppercase_re = re.compile(always_uppercase, re.I | re.X)

def titlecase_plus(text):
  """The titlecase module assumes words in all UPPERCASE should be ignored.
  This works for words like HTML, FYI, ID, etc., but not generally. Just work
  around for now by going to .lower first. Then, replace any well known
  "always" uppercase"""
  text = titlecase(text.lower())
  def upcase(m):
    return m.group().upper()
  return always_uppercase_re.sub(upcase, text)

variations = {
  'lower': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ),
  'upper': escape(text.upper(), {'"': '&quot;', '\n': '&#10;'} ),
  'title': escape(titlecase_plus(text), {'"': '&quot;', '\n': '&#10;'} )
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
