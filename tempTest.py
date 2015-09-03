__author__ = 'Administrator'

import re

databuf = "command: select * from table EndHash34343"

matchobj = re.match(r'(^.*?): (.*) EndHash(.*)',databuf,re.I)

print r'hello\n'
print matchobj.group(1)
print matchobj.group(2)
print matchobj.group(3)

if "command" in databuf:
    print "yes"