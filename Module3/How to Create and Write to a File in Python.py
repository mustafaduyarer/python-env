"""
In this section of the course, we're going to start working with the file system in Python.
 So we're going to start off with the basics.
 open() fonsiyonu once bakiyor dosya ismi varmi diye , varsaa aciyor icerisine ekleme yapiyo
 yoksa o dosyayi olusturuyor
"""
file_builder = open("logger.txt", "w+") #dosya ismi ve uzantisini veriyoruz birde w+ diyerek bu dosyaya yazmamizicin izin veriyoruz

for i in range(10):
    file_builder.write(f"I'm on line {i + 1}\n")

# file_builder.write("Hey, I'm in a file!")

file_builder.close()
