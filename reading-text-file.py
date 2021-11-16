fs = open(r"text-file.txt",'r')
# read 10 characters only
con = fs.read(10)
print(con)
# read the entire file
con = fs.read()
print(con)
fs.close()