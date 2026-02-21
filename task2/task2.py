# Завдання 2

from pathlib import Path

def get_cats_info(path):
    path = Path(path)

    #check if file exist before proceed 
    if not path.exists():
       raise FileNotFoundError("File does not exist.")
    
    #prepate empty 'cats' dictionary
    cats = []
    
    with path.open("r", encoding="utf-8") as file:
        for line in file:
             id,name,age = line.strip().split(",")
             cat_dict = {
                "id": id,
                "name": name,
                "age": age
            }
             #add details to cats dictionary using append
             cats.append(cat_dict)
        return cats
    
#using try except to handle the error  
try:
    cats_info = get_cats_info("goit-pycore-hw-04/task2/cats.txt")
    print(cats_info)
except FileNotFoundError as e:
    print(e)


