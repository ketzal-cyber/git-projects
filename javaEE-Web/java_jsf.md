Java Beneans es una clase en java que contiene:
	* un constructor vacio
	* atributos privadas 
	* por cada atributo se tienen un metodo get y set

Managed Beans es una clase java que cumplen con java beans
	* No estan obligados a extender de ninguna otra clase

Backing Beans
	* Beans de modelo: repressentan el modelo MVC
	* Beans de control: representan el controlador en el patron MVC
	* Beasn de soporte o Helpers: Contienen codigo E/p Convertidores
	* beans de Utileria: tareas genericas como obtener el objeto request

Uso de managed Beans declaraciones
	* anotacion antes del nombre de la clase -> @ManagedBean
	* definirla con un CDI (Contexts and Dependency Inyeccion) ants del nombre de la clase  -> @Named
	* al utiliar este concepto debemos agregar un archivo llamado beans.xml en web/WEB-INF
	* declarar un bean desde el archivo faces-config.xml
		- utiliar los tags en el archivo de configuracion <managed-bean> ... </managed-bean>

Alcance de los Managed Beans  anotacion jsf javax.faces.bean
	* application: persiste durante toda la aplicacion
	* session: persiste durante tiempo de session del usuario
	* view: persiste si es la misma vista (util si usamos ajax)
	* request: persiste durante la peticion del usuario
	* map: personalizado enlace de llave y sus valores
 
Alcance de CDI y Beans  anotaciones de CDI javax.enterprice.context
	* application: persiste durante toda la aplicacion
	* session: persiste durante tiempo de session del usuario
	* conversation: persiste asta concuir alguna tarea
	* request: persiste durante la peticion del usuario
	* map: personalizado enlace de llave y sus valores 

Navegacion en JSF
	* permmite moversnos entre paginas de la misma tecnología
	* Tipos de navegación
		> Navegación Estática: el valor de la siguiente vista esta dada por  una cadena fija
		> Navegcion Dinámica: el valor de la siguiente vista a seleccionar va a depender de la accion que ejecute el usuario

	* Formas de configurar la naveacion
		> Navegación implícita -> busca la cadena en el direcotio 
		> Navegación explícita -> se define en el archivo faces-confi.xml de detalla las acciones
