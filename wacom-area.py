#!/usr/bin/python

from subprocess import run, PIPE
import re
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else ''

#use command "xsetwacom set 12 maptooutput 1920x1200+1925+0" for control gimp tools with tablet
#use command "xsetwacom set 12 maptooutput 1920x1200+2214+0" if you do not need tools

id = run(["xsetwacom", "--list"], stdout=PIPE, text=True).stdout
id1, id2 = id.split("\n")[:-1]
id = re.findall(r'\d{1,3}', id1)[0]

if mode == 'lg':
	run(["xsetwacom", "set", id, "maptooutput", "1920x1080+0+0"]) # на монитор (монитор сверху)
else:
	run(["xsetwacom", "set", id, "maptooutput", "1920x1080+0+1080"]) # на ноутбук (монитор сверху)
