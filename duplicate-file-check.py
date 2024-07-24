"""to check if the two file are identical and the content inside it matches with each other"""

def check_files(file_1,file_2):
    print(f"File 1 is : {file_1}")
    print(f"File 2 is : {file_2}")
    with open(file_1) as file1:
        file1_cont = file1.read()
    with open(file_2) as file2:
        file2_cont = file2.read()  
    print(f"file1 content is : {file1_cont}") 
    print(f"file2 content is : {file2_cont}") 
    if file1_cont == file2_cont:
        print(f"both files ({file_1, file_2}) are identical and content is matching")
    else:
        print(f"content is not matching")

file_1 = input("Enter File_1 name : ")
file_2 = input("Enter File_2 name : ")

    
check_files(file_1,file_2)