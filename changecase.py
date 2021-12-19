#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import re, sys
from xml.sax.saxutils import escape
from titlecase import titlecase
import random

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

# Props to Noah Krim <nkrim62@gmail.com> for this
# This is copied from https://github.com/nkrim/spongemock/blob/master/src/spongemock.py
def spongemock(text, diversity_bias=0.5, random_seed=None):
    # Error handling
    if diversity_bias < 0 or diversity_bias > 1:
        raise ValueError('diversity_bias must be between the inclusive range [0,1]')
    # Seed the random number generator
    random.seed(random_seed)
    # Mock the text
    out = ''
    last_was_upper = True
    swap_chance = 0.5
    for c in text:
        if c.isalpha():
            if random.random() < swap_chance:
                last_was_upper = not last_was_upper
                swap_chance = 0.5
            c = c.upper() if last_was_upper else c.lower()
            swap_chance += (1-swap_chance)*diversity_bias
        out += c
    return out

variations = {
  'lower': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ),
  'upper': escape(text.upper(), {'"': '&quot;', '\n': '&#10;'} ),
  'title': escape(titlecase_plus(text), {'"': '&quot;', '\n': '&#10;'} ),
  'camel': escape(titlecase_plus(text), {'"': '&quot;', '\n': '&#10;'} ).replace(' ', ''),
  'kebab': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ).replace(' ', '-').replace('_', '-'),
  'snake': escape(text.lower(), {'"': '&quot;', '\n': '&#10;'} ).replace(' ', '_').replace('-', '_'),
  'trout': escape(spongemock(text), {'"': '&quot;', '\n': '&#10;'} ),
}

print """<?xml version="1.0"?>
<items>
  <item arg="%(lower)s">
    <title>%(lower)s</title>
    <subtitle>lowercase</subtitle>
    <icon>lowercase.png</icon>
  </item>
  <item arg="%(upper)s">
    <title>%(upper)s</title>
    <subtitle>UPPERCASE</subtitle>
    <icon>uppercase.png</icon>
  </item>
  <item arg="%(title)s">
    <title>%(title)s</title>
    <subtitle>Title Case</subtitle>
    <icon>titlecase.png</icon>
  </item>
  <item arg="%(camel)s">
    <title>%(camel)s</title>
    <subtitle>CamelCase</subtitle>
    <icon>camelcase.png</icon>
  </item>
  <item arg="%(kebab)s">
    <title>%(kebab)s</title>
    <subtitle>kebab-case</subtitle>
    <icon>kebabcase.png</icon>
  </item>
  <item arg="%(snake)s">
    <title>%(snake)s</title>
    <subtitle>snake_case</subtitle>
    <icon>snakecase.png</icon>
  </item>
  <item arg="%(trout)s">
    <title>"%(trout)s"</title>
    <subtitle>TroUTcAsE</subtitle>
    <icon>troutcase.png</icon>
  </item>

</items>""" % variations
