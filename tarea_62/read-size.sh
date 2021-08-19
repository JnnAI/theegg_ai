maximumFileSize=0
greatesFileName=""

for fileName in ./tareas/*                                          #bucle que entra en la carpeta "tareas"
do
    if [ ! -d $fileName ]                                           #si no es una carpeta, entra en el if y calcula el tamaño del archivo
    then
        fileSize=$(wc -c ${fileName} | awk '{print $1}')            #linea donde se calcula el tamaño del archivo
        if [[ $fileSize -gt $maximumFileSize ]]                     #condicion que regula si el tamaño del archivo que esta leyendo es el mas grande de la carpeta, sino actualiza el de mayor tamaño
        then
            maximumFileSize=$fileSize                       
            greatesFileName=$fileName
        fi
    fi
done

echo "El archivo mas grande es ${greatesFileName} con un tamaño de ${maximumFileSize}"