file_path="output.txt"
with open(file_path,"w")as file:
    file.write("Hello,world!\n")
    file.write("This is a sample text.")
print("Content written to",file_path)
