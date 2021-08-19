for filePath in ./tareas/*                                          #bucle que entra en la carpeta tareas
do
    if [ ! -d $filePath ]                                           #si no es una carpeta, entra en las siguientes lineas
    then
        fileBasename=$(basename ${filePath})                        #filaName devuelve la ruta con todos los datos de los archivos, de forma que con fileBasename, se aisla solamente el nombre del archivo.
        mv $filePath ./tareas/renombrado-${fileBasename}            #renombra los archivos con el pronombre: renombrado-
    fi
done