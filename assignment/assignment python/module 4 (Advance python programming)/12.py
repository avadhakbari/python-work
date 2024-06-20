#12. Write a Python program to copy the contents of a file to another file. 

 
with open('text.txt','r') as firstfile, open('text2.txt','a') as secondfile: 
      
    for line in firstfile: 
        secondfile.write(line)
