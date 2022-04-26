import urllib.request






url = "https://celestrak.com/NORAD/elements/starlink.txt"
file = urllib.request.urlopen(url)

f = open("tle.txt","a")

for line in file : 
    decoded_line = line.decode("utf-8")
    f.write(decoded_line.strip()+"\n")

f.close()
	


f = open("tle.txt", "r")
data = f.readlines()

for i in range(0, len(data)-1, 3) :
    data[i] = '  { \n    "name" : "'+data[i].strip() +'",'+"\n"
    data[i+1] = '    "tle_line_1" : "'+data[i+1].strip() +'",'+"\n"
    data[i+2] = '    "tle_line_2" : "'+data[i+2].strip() +'" \n  },'+"\n"

data.insert(0,"[\n")
data[len(data)-1]=data[len(data)-1].replace(",","")
data.append("]")

name = input("Generated File's name : ")
f = open(name +".json", "a")
for i in data : 
    f.write(i)
f.close()



print(data)

