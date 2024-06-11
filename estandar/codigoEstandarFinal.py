#Importamos las librerías necesarias para la ejecución del código
import os
from pytdml.type import EOTrainingDataset, EOTrainingData, SceneLabel
from pytdml.io import write_to_json
from pydantic import BaseModel
from typing import List, Dict, Any, Tuple
import pytdml, json
#Inicializamos las clases que se necesitan para generar el JSON de forma correcta
#En cada clase se agragen las variables necesarias para que cumplan con el estandar.

class Geometry(BaseModel):
    type: str
    coordinates: List[Tuple[float, float]]

class ObjectType(BaseModel):
    type: str
    geometry: Geometry

class SceneLabel(BaseModel):
    type: str
    label_class: str   
    image_format: List[str]
    object:  ObjectType    
    dateTime: str
    bboxType: str
    isDiffDetectable: bool
    

class EOTrainingData(BaseModel):
    type: str
    id: str    
    dataSources: str
    dataURL: List[str]
    numberOfLabels: int
    trainingType: str
    labels: List[SceneLabel]
    

class EOTask(BaseModel):
    task_type: str
    id: str
    description: str
    taskType: str
    datasetId: str
    type: str

class EOTrainingDataset(BaseModel):
    type:str
    id:str
    name:str
    description:str
    license:str    
    version:str
    amountOfTrainingData:int
    createdTime:str
    providers:List[str]
    classes:List[str]
    numberOfClasses:int
    bands:List[str]
    tasks: List[EOTask]
    data: List[EOTrainingData]
    amountOfTrainingData: int = 0
    

# Definir el conjunto de datos EOTrainingDataset. Inicializamos data como una lista vacía, ya que con el bucle for que hay 
# a continuación, se ira completando según la infromación de las etiquetas.
dataset = EOTrainingDataset(
    type= "TrainingDataset",
    id='DeteccionRE',    
    name='DeteccionRE',
    description='datos de la detección de rotondas y enlaces en diferentes imágenes de diversas áreas de España ',
    license="CC BY-SA 4.0",    
    version="1.0",
    amountOfTrainingData=0,
    createdTime="2024-05-15",
    providers=["UPM"],
    classes=["enlaceBI2", "enlaceTci", "rotondaEn", "enlaceTsi", "enlaceTA", "cruce", "rotondaN"],
    numberOfClasses=7,
    bands=["red", "green", "blue"],
    tasks = [
            EOTask(
                type="AI_EOTask",
                task_type="AI_EOTask",
                id="DeteccionRE-task",
                description="Remote Sensing Object Detection",
                taskType="Object Detection",
                datasetId="PNOA"
            )
        ],
    
    keywords=["Redes Convolucioneles", "Deep Learning", "Identificación", "etiquetado"],
    data = []
)

# Procesar las imágenes y etiquetas
for datos in ["train", "test", "val"]:
    relativa= "G:/CASA/UNIVERSIDAD4CURSO/practicas_TFG/tfgInma/rotondas_enlace_amp_rep2/YOLODataset"

    imagenes = os.path.join("G:/CASA/UNIVERSIDAD4CURSO/practicas_TFG/tfgInma/rotondas_enlace_amp_rep2/YOLODataset", "images", datos)
    etiquetasImg = os.path.join("G:/CASA/UNIVERSIDAD4CURSO/practicas_TFG/tfgInma/rotondas_enlace_amp_rep2/YOLODataset", "labels", datos)
    #Se guarda el nombre del archivo y el path de donde esta, para luego indicar la ruta
    for img in os.listdir(imagenes):
        if img.endswith(".png"):
            ruta= os.path.relpath(imagenes, relativa)
            imgNombre = img.split(".")[0]            
            img_path = os.path.join(ruta,img)
            label_path = os.path.join(etiquetasImg, imgNombre + ".txt")            
            print(label_path)
            # Leer la etiqueta de la carpeta
            with open(label_path, "r") as file:
                #Se lee línea por línea las etiquetas, por cada una se identifica la clase y se recogen las coordenadas
                objeto = file.readlines()
                numeroEtiquetas=len(objeto)
                etiqueta = []
                for etiquetas in objeto:
                    parametros = etiquetas.split()
                    class_name = parametros[0]
                    
                    #Se identifican que clases son para poner cual es, en vez del número
                    if class_name== "0":
                        class_name="enlaceBI2"
                    elif class_name== "1":
                        class_name="enlaceTci"
                    elif class_name== "2":
                        class_name="rotondaEn"
                    elif class_name== "3":
                        class_name="enlaceTsi"
                    elif class_name== "4":
                        class_name="enlaceTA"
                    elif class_name== "5":
                        class_name="cruce"
                    elif class_name== "6":
                        class_name="rotondaN"
                    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, parametros[1:9])
                    #Control para saber si se recogen de forma correcta las coordenadas
                    #print(x1, y1, x2, y2, x3, y3, x4, y4)
                    #Se normalizan las coordenadas, ya que se tienen medidas en pixeles, los resultados iran del 0 al 1
                    p1=[x1/512,y1/512]
                    p2=[x2/512,y2/512]
                    p3=[x3/512,y3/512]
                    p4=[x4/512,y4/512]
                    p5=[x1/512,y1/512]
                    type = 'AI_SceneLabel'
                    bounding_box=[p1,p2,p3,p4,p5]
                    geometry_data=Geometry(type="Polygon", coordinates= bounding_box)
                    object_type_data = ObjectType( type="Feature",  geometry=geometry_data)

                    
                    #Una vez se han obtenido todos los datos necesarios, se procede a introducirlos en data
                    etiqueta.append(SceneLabel(
                                                type= "AI_ObjectLabel",
                                                label_class=class_name,                                                 
                                                image_format=["png"],
                                                object=object_type_data,                                        
                                                dateTime="2024-05-15T12:00:00",
                                                bboxType="Oriented BBox",
                                                isDiffDetectable=True
                                                
                                            ))

                # Agregar datos de entrenamiento al conjunto de datos
                training_data = EOTrainingData(
                                                type= "AI_EOTrainingData",
                                                id=imgNombre,                                                
                                                dataSources="PNOA",
                                                dataURL=[img_path],
                                                numberOfLabels=numeroEtiquetas,
                                                trainingType="training",
                                                labels=etiqueta  
                                            )
                #Aquí es donde se introduce los valores que se han obtenido
                dataset.data.append(training_data)
dataset.amountOfTrainingData = len(dataset.data)



# Escribir en formato json
write_to_json(dataset, "dataset.json")
#Imprimir un mensaje para saber si se ha realizado 
print("Ya se ha creado el JSON")


