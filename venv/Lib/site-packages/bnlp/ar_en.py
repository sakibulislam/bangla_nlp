#-*- coding: utf-8 -*-
ar_en = {}

#tha, ha, ba, sin, ra, qaf, lam, nun
consonants_ar = [u'\u062b', u'\u062d', u'\u0628', u'\u0633',u'\u0631', u'\u0642', u'\u0644', u'\u0646']

#alif, wa, ya
vowels_ar = [u'\u0627',u'\u0648',u'\u064a']

#consonants_en = ['b','c','d','f','g','h','

#blank space
ar_en[u' '] = [u'',' ']

#alif
ar_en[u'\u0627'] = [u'a',u'o']

#alif hamza
ar_en[u'\u0623'] = [u'a']

#alif hamza with hamza at bottom
ar_en[u'\u0625'] = [u'i']

#ba
ar_en[u'\u0628'] = ['b']

# ta
ar_en[u'\u062a'] = [u't']

# tha
ar_en[u'\u062b'] = [u'th']

#ja/ga
ar_en[u'\u062c'] = ['j','g','ja','ga']

# ha'
ar_en[u'\u062d'] = [u'h',u'ha',u'he']

# dal
ar_en[u'\u062f'] = [u'd']

# ghayn
ar_en[u'\u063a'] = [u'gh']

#ra
ar_en[u'\u0631'] = [u'r',u'ra']

# za
ar_en[u'\u0632'] = [u'z',u'zz']

#sin
ar_en[u'\u0633'] = [u's','sa']

#shin connected
ar_en[u'\u0634'] = [u'sh',u'shu',u'sha']

#sad
ar_en[u'\u0635'] = [u's',u'sa']

#deep ta
ar_en[u'\u0637'] = [u't',u'ta']

# ayn
ar_en[u'\u0639'] = [u'3',u'a',u'']

# fa
ar_en[u'\u0641'] = [u'f',u'fa']

#qaf
ar_en[u'\u0642'] = [u'q',u'qu']

#kaf
ar_en[u'\u0643'] = [u'k',u'ka']

##lam
ar_en[u'\u0644'] = [u'l',u'l-',u'l ',u's',u's-',u's ',u'sh',u'sh-','sh ',u't',u't-',u't ',u'th',u'th-',u'th ','la',u'li']

#mim solo
ar_en[u'\u0645'] = ['m','ma','mu']

#nun
ar_en[u'\u0646'] = [u'n', u'na']

#tar ma-buta
ar_en[u'\u0629'] = [u'a',u'at']

#light ha/he
ar_en[u'\u0647'] = ['','h','ha','he']

#wa
ar_en[u'\u0648'] = [u'u',u'o','w','wa']

# ya, said ee
ar_en[u'\u064a'] = [u'y',u'i',u'iyy',u'yyi','ee']

#hamza solo
ar_en[u'\u0621'] = [u""]

#hamza on ya
ar_en[u'\u0626'] = ['i',"'i"]

#left-to-right mark
ar_en[u'\u200e'] = ['']
