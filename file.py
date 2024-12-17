paths = r'Z:\Python for ICT\sample.txt'
num =0
with open(paths, 'r') as file:
    files = file.read()
    print("Initial Content:\n", files)

with open(paths, 'a+') as file:
    num+=1
    file.write(f"\nhello {num}")
    file.seek(0)
    written_file = file.read()
    print("\nContent after appending 'hello':\n", written_file)
