import os
os.chdir('c"/user/admin...')
i=1
for file in os.listdir():
    src=file
    dst="jumanji"+str(i)+'png'
    os.rename(src,dst)
    i+=1 
