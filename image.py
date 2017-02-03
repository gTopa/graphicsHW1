image=open("image.ppm","w")
string="P3 500 500 255 "
for x in range(500):
    for y in range(500):
        string+=str(x%256)+" "+str(y%256)+" "+str((x+y)%256)+"\n"
image.write(string)
