# Pracctica de tupla
miTupla = ("Programacion","English","Metodologias","Base Datos", "Sistemas")
# Conjunto
prog = {"Java","JavaScript", "Python","Nodejs","Angular"}
en = {"verbo","adjetivo","sustantivo"}
metod = {"Scrum", "DevOps", "Kanan","XP"}
db = {"PostgreSQL","OracleDB","MySQL","MongoDB"}
system = {"Debian","CentOS", "Arch","Fedora","Windows"}

# Diccionario y Listas
tareas = {"java":{"Spring":["mvc","boot","data","Security","cloud"],"jsf":["ejb","web"],"struts":["mvc"],"jfx":["componente"]},"js":"DOM"}

print(tareas)

print("Selecciona un tema ")
for tema in miTupla:
    print("- "+ tema)
elemento = input(" Introduce un elemento ")

if elemento in miTupla:
    print(" Elemento contenido")
else:
    print(" No existe elemento")
