def Encrypt(filename, key):
  file = open(filename, "rb") #rb for encoding issues so files other than text can be used
  data = file.read()
  file.close()

  #converts file to bytearray
  data = bytearray(data)
  for index, value in enumerate(data):
    #whatever value at exclusive or (XOR) for key passed in
    data[index] = value ^ key

  #make copy of file that will be encrypted version
  file = open("E-" + filename, "wb")
  file.write(data)
  file.close()

#decrypts encrypted file with same key, creating new unencrypted version of file
def Decrypt(filename, key):
  file = open(filename, "rb")
  data = file.read()
  file.close()

  data = bytearray(data)
  for index, value in enumerate(data):
    data[index] = value ^ key

  file = open(filename, "wb")
  file.write(data)
  file.close()

choice = ""
while choice != "3":
  print("Select input your option (1-3): ")
  print("1. Encrypt File")
  print("2. Decrypt File")
  print("3. Exit")
  choice = input()
  if choice == "1" or choice == "2":
    key = int(input("Enter a key (1-255): \n"))
    filename = input("Enter filename (ex: example.py): \n")
    if choice == "1":
      Encrypt(filename, key)
    if choice == "2":
      Encrypt(filename, key)
  else:
    if choice != "3":
      print("Invalid choice. Please input a valid choice (1-3).\n")
    else:
      break



