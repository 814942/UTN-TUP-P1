# Resultados de Tiempos de Ejecución de Algoritmos de Ordenamiento

## Tiempos Promedio (en segundos)

| Algoritmo | 1000 productos | 9,685 productos | 53,300 productos |
|-----------|----------------|------------------|------------------|
| Bubble Sort | 0.2124 | ~21.79 | 1009.36 |
| Bubble Sort V2 | 0.0238 | ~2.76 | - |
| Merge Sort | 0.0038 | 0.052 | ~0.34 |

## Análisis de Resultados

1. **Bubble Sort (Estándar)**:
   - Muestra un incremento significativo en el tiempo de ejecución a medida que crece el tamaño de los datos.
   - Para 53,300 productos, el tiempo de ejecución supera los 16 minutos.

2. **Bubble Sort V2 (Optimizado)**:
   - Mejora considerablemente después de la primera iteración gracias a su optimización.
   - Los tiempos posteriores a la primera iteración son significativamente más bajos.
   - No hay datos disponibles para 53,300 productos.

3. **Merge Sort**:
   - Demuestra ser el más eficiente de los tres algoritmos probados.
   - Muestra un comportamiento casi lineal en el crecimiento del tiempo respecto al tamaño de los datos.
   - Para 53,300 productos, el tiempo de ejecución es de aproximadamente 0.34 segundos.

## Conclusión

El Merge Sort es claramente el algoritmo más eficiente para grandes conjuntos de datos, mostrando tiempos de ejecución significativamente más bajos que las versiones de Bubble Sort. Mientras que Bubble Sort V2 mejora notablemente sobre la versión estándar gracias a sus optimizaciones, sigue siendo mucho más lento que Merge Sort para conjuntos de datos grandes.
