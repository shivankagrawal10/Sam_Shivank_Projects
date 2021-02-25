f = open("/Users/shivankagrawal/Personal/github/Sam_Shivank_Projects/GoogleHash_2021/example.txt", "r")
print(f.read())
f.close()

f = open("demo.txt", "a")
f.write("Now the file has more content!")
f.close()