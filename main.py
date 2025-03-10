def Encrypt(filename, key):
  file = open(filename, "rb") #rb for encoding issues
  data = file.read()
  print(data)
  file.close()

  data = bytearray(data)
  for index, value in enumerate(data):
    #print(f"index: {index} value: {value}")
    #whatever value at exclusive or for key passed in
    data[index] = value ^ key

  #make copy of file
  file = open("D-" + filename, "wb")
  file.write(data)
  file.close()

key = int(input("Ask for a key between 1 and 255: "))
filename = input("Enter a file name: ")
Encrypt(filename, key)

