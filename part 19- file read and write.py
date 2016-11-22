fw= open('ratul1.txt', 'w')

fw.write("i am ratul\n") #file write

fw.write("i am a good boy\n")# file write
fw.close()
fw1=open('man1.txt','w')

fw1.write("we are human\n we can do mistake")

fw1.close()

fr=open("ratul1.txt", 'r')

text=fr.read()

print(text)
fr.close()

fr1=open('man1.txt',"r")
text1=fr1.read()
print(text1)
fr1.close()