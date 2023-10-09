import os 
# Francisco Marin, Diego Mares, Juan Yael

# # directorio
# print(os.getcwd())

# # Lista del directorio
# print(os.listdir())

# # Crea directorio
# if not os.path.exists("modules"):
#     os.mkdir("modules")

# # Stats
# path_file=os.path.join("modules", "README.txt")
# f=os.open(path_file, os.O_RDWR|os.O_CREAT)

# file_properties=os.stat(path_file)
# print(file_properties.st_mode)
# print(file_properties.st_size)
# print(file_properties.st_mtime)

# # copy
# for file in os.listdir(os.path.join("c1")):
#     new_file=os.open(os.path.join("modules", f"{file}"), os.O_RDWR|os.O_CREAT)
#     og_file=os.open(os.path.join("c1", file), os.O_RDWR|os.O_CREAT)
#     os.write(new_file, os.read(og_file, os.stat(os.path.join("c1", file)).st_size))
#     os.close(os.path.join("modules", f"{file}"))
#     os.close(os.path.join("c1", file))
    
# for file in os.listdir(os.path.join("c2")):
#     new_file=os.open(os.path.join("modules", f"{file}"), os.O_RDWR|os.O_CREAT)
#     og_file=os.open(os.path.join("c2", file), os.O_RDWR|os.O_CREAT)
#     os.write(new_file, os.read(og_file, os.stat(os.path.join("c2", file)).st_size))
#     os.close(os.path.join("modules", f"{file}"))
#     os.close(os.path.join("c2", file))


# Eliminar archivos
for file in os.listdir(os.path.join("c1")):
    os.remove(os.path.join("c1", file))

for file in os.listdir(os.path.join("c2")):
    os.remove(os.path.join("c2", file))