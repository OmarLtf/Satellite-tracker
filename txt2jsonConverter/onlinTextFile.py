import urllib.request

url = "https://celestrak.com/NORAD/elements/starlink.txt"
file = urllib.request.urlopen(url)

f = open("tle.txt","a")

for line in file : 
    decoded_line = line.decode("utf-8")
    f.write(decoded_line.strip()+"\n")

f.close()
	