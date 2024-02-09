import os

class PathHandler:

    def __enter__(self):
        current_dirs = [x for x in os.listdir()]
        print(current_dirs)
        try:
            new_dir = input("select a new directory to go: ")
            os.chdir(new_dir)
        except:
            raise ValueError("No such a directory")
        return self
    
    def __exit__(self, type, eso, lootro):
        pass
    

with PathHandler() as p:
    print("Te encuentras en el directorio:", os.getcwd())


print("Directorio fuera del context manager",os.getcwd())

