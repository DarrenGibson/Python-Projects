#----------------------------------------------------------------#
#						The Traveling Suitcase
#----------------------------------------------------------------#

# this code works beautifully, but if running from command line need to use 
# python, instead of python3

import urllib
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()






































































