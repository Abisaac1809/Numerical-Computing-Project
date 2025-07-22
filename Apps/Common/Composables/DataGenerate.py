import os
import random

class archiveGenerator():
    __router = ""
    __nameArchive = ""

    def __init__(self, nameArchive = "generalArchive.bin", router = os.getcwd()):#constructor polimorfico
        """
        Crear o modificar archivos. 
        
        ->@param: string [archive.extension]
        ->@param: string router = C:\\folder1\\folder2\\folder or "C:\folder\folder\folder" or C:/folder/folder/folder
        ->@return: Void
        """
        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        
        if (len(nameArchive) == 0 or not nameArchive):
            raise Exception("Manage-Error: La ruta es vacia.")
        
        self.__nameArchive = nameArchive
        self.__utilDirectory(router)

    def setRouter(self, router):
        """
        Cambio de ruta existente

        ->@param: string router = C:\\folder1\\folder2\\folder or "C:\folder\folder\folder" or C:/folder/folder/folder
        ->@return: Void
        """
        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        self.utilDirectory(router)

    def setName(self, nameArchive):
        """
        Cambio de ruta existente

        ->@param: string [archive.extension]
        ->@return: Void
        """
        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        
        self.__nameArchive

    def __setOrCreateFiles(self, nameArchive, content = "", bool = False):#metodo polimorfico
        
        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        try: #usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            if (not content or len(content) == 0):
                archive = open(self.__router+"\\"+nameArchive+".txt", "x")
                return
            
            archive = open(self.__router+"\\"+nameArchive, "a")#requiere que el nombre venga con su extencion. 
            
            if (bool == True):
                archive.write(content+"\n")
            else:
                archive.write(content)

        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)

    def archiveDataGenerator(self, row = 3, colum = 3):
        """
        Genera archivo con datos aleatorios.

        ->@param: Float/Float [data default = 3]
        ->@return: Void
        """
        arrayBi = []

        if(row > 0 and colum > 0):
            arrayBi = [[random.randint(-30, 30) for j in range(colum)] for i in range(row)]

            for i in range(len(arrayBi)):
                for j in range(len(arrayBi[0])):
                    if(j == (len(arrayBi[0]) - 1)):
                        self.__setOrCreateFiles(self.__nameArchive, str(arrayBi[i][j]), i < (len(arrayBi) - 1))
                    else:
                        self.__setOrCreateFiles(self.__nameArchive, str(arrayBi[i][j])+"/")

    def __utilDirectory(self, router):
        
        if (os.path.exists(router) and not os.path.isdir(router)):
            raise NotADirectoryError(f"Manage-Error: La ruta '{router}' no es un directorio.")
        elif (not os.path.exists(router)):
            raise FileNotFoundError(f"Manage-Error: El directorio '{router}' no existe.")
        
        self.__router = router
