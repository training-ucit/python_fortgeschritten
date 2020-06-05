import os

def find_files(dir):
    result = []
    for root, dirs, files in os.walk(dir):
        for file in files:
        #if file.endswith(".txt"):
            #print (type(os.path.join(root, file)))
            result.append(os.path.join(root, file))
        return result

if __name__ == "__main__":
  
    #find_files("/home/coder/")
    print(find_files("/home/coder/"))

            



