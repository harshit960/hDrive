import requests
import os
def binaryToFile(cache):
    filename = cache[0]
    binary_string = cache[1]
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = int(binary_string[i:i+8], 2)
        byte_array.append(byte)
    LATTE = byte_array
    #print(byte_array)
    with open(filename,'wb') as file:
        file.write(byte_array)

def fileToBinary(filename):
    ext = filename.split(".")[-1]
    with open(str(filename),'rb') as f:
        contents = f.read()
        binary = ''.join(format(byte,'08b') for byte in contents)
        #binaryToFile("final_output.pdf",binary)   
        
    return [binary,ext]


def fileSave(file_url,title):
    ext=file_url.split('/')[-1]
    name, ext = os.path.splitext(file_url)
    r = requests.get(file_url, stream = True)
    path="temp/"+str(title)+str(ext)
    with open(path,"wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
       
		# writing one chunk at a time to pdf file
            if chunk:
                f.write(chunk)
                print
    return [path,ext]    
	
