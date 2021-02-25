import os
import sys
f = open(os.path.join(sys.path[0], 'example.txt'), "r")
print(f.read())
f.close()
#/Users/shivankagrawal/Personal/github
f = open(os.path.join(sys.path[0],"demo.txt"), "w")
f.write("Now the file has more content!")
f.close()