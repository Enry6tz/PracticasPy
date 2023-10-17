En este proyecto, hemos aplicado exitosamente una red neuronal convolucional (CNN) para la clasificación de dígitos manuscritos utilizando el conjunto de datos SVHN (Street View House Numbers). A lo largo de este proyecto, hemos realizado las siguientes tareas clave:

1. **Preprocesamiento de Datos:** Descargamos y preprocesamos los datos de entrenamiento y prueba desde el conjunto de datos SVHN. Realizamos transformaciones como cambiar el tamaño de las imágenes y normalizar los valores de píxeles para preparar los datos para el entrenamiento del modelo.

2. **Diseño de la Red Neuronal:** Diseñamos y entrenamos una CNN personalizada que consta de múltiples capas de convolución, activación 'swish', MaxPooling, y capas totalmente conectadas. También aplicamos técnicas como la regularización mediante la capa de Dropout.

3. **Entrenamiento del Modelo:** Utilizamos Google Colab para aprovechar la potencia de procesamiento GPU y entrenamos el modelo en el conjunto de datos de entrenamiento. Implementamos un proceso de entrenamiento que incluye paradas tempranas, reducción de la tasa de aprendizaje y almacenamiento de los pesos del modelo en los puntos óptimos.

4. **Evaluación y Validación:** Evaluamos el modelo en el conjunto de datos de prueba y validación, y supervisamos las métricas de precisión y pérdida a lo largo de las épocas del entrenamiento. Observamos un rendimiento sólido en términos de precisión y capacidad de generalización del modelo.

5. **Predicción en Nuevas Imágenes:** Mostramos cómo utilizar el modelo entrenado para hacer predicciones en nuevas imágenes. Realizamos un preprocesamiento en una imagen de ejemplo y demostramos cómo obtener la etiqueta de clase predicha a partir de las probabilidades de salida del modelo.

En general, este proyecto ha demostrado cómo implementar y entrenar una red neuronal convolucional personalizada en un conjunto de datos del mundo real. Además, hemos explorado técnicas de preprocesamiento, diseño de arquitectura, entrenamiento y evaluación del modelo. Los resultados sólidos obtenidos en la clasificación de dígitos manuscritos confirman la eficacia de la arquitectura de la CNN y subrayan la importancia de las estrategias de regularización y optimización. Este proyecto proporciona una sólida base para futuras investigaciones y aplicaciones de aprendizaje profundo en la clasificación de imágenes.
