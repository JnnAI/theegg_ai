if [ ! -d ./tareas ]; then                                              #Si no existe una carpeta que se llama tareas, la crea. -d significa: existe una carpeta que se llama tareas??
    echo "Creando carpeta"
    mkdir tareas                                                        #comando que crea la carpeta.
    echo "Carpeta 'tareas' creada correctamente"                        #echo funciona como print en python
fi

for fileName in ./*                                                     #la variable fileName coge las rutas de todos los archivos de la carpeta donde se encuentra este script (eso lo hace con ./*)
do
    if [[ $fileName == *"tarea"* ]] && [ ! -d $fileName ]; then         #Si entre los archivos que encuentra se encuentra la palabra "tarea" dentro, mueve el archivo dentro de la carpeta "tareas"
        mv $fileName "tareas/${fileName}"                               #Comando para mover los archivos dentro de la carpeta
        echo "Movida ${fileName} a la carpeta tareas"                   
    fi  
done