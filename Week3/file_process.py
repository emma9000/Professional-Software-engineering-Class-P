import os

def file_read(file_path):
    with open(file_path,'r',encoding="utf-8") as f:
        infile=f.read()
        return infile
    
def file_write(file_path,outfile):
    with open(file_path,'w',encoding="utf-8") as f:
        f.write(outfile)

if __name__=="__main__":
    # check path exist
    file_path="demo.txt"
    new_path="demo_copy.txt"
    if(os.path.exists(file_path)):
        
        context= file_read(file_path) 
        file_write(new_path,context)

        print("The context is writen into demo_copy,please check!")

    else:
        print("Your file is not exist!")