def imagefilecopy():
    try:
        with open("D:\\Photos\\Spects.jpg","rb") as rp:
            with open("D:\\Python\\Operations-On-File\\file.png","wb") as wp:
                srcfiledata = rp.read()
                wp.write(srcfiledata)
                print("Image copied successfully")
    except FileNotFoundError:
        print("Source file does not exist")
#Main Program
imagefilecopy()