# Proyecto listo para Google Colab

Esta es una copia del repositorio preparada para ejecutarse en Google Colab sin cambiar la lógica del pipeline ni los imports del proyecto.

## Estructura
git clone https://github.com/<usuario>/<repo>.git
cd <repo>

## Opción 1: clonar directamente desde GitHub

```bash
!git clone https://github.com/<usuario>/<repo>.git
%cd <repo>
!pip install -r requirements.txt
!python scripts/colab_setup.py
```

## Opción 2: subir la carpeta del repositorio a Google Drive

1. Sube esta carpeta a tu Google Drive.
2. Abre Colab y monta tu Drive:

```python
from google.colab import drive

drive.mount('/content/drive')
```

3. Luego abre la carpeta y ejecuta:

```python
%cd /content/drive/MyDrive/<ruta>/Analisis-Nacional-Papa-Colab
!pip install -r requirements.txt
!python scripts/colab_setup.py
```

## Verificación rápida

```python
import sys
sys.path.insert(0, '.')

from src.infrastructure.config import PROJECT_ROOT
print(PROJECT_ROOT)
```

Si imprime la ruta del proyecto, todo está listo.

## Ejecución del pipeline

Después del bootstrap, puedes correr notebooks o scripts desde la raíz del repositorio.

```python
%cd /content/<repo>
```

Ejemplos:

```python
from src.application.ingestion_service import IngestionService
from src.application.cleaning_service import CleaningService
```

O ejecutar notebooks secuenciales del flujo CRISP-DM:

- `notebooks/01_ingestion_dataset_unico.ipynb`
- `notebooks/02_analisis_exploratorio_eda.ipynb`
- `notebooks/03_validacion_reglas_negocio.ipynb`
- `notebooks/04_limpieza_y_gobernanza.ipynb`
- `notebooks/05_ingenieria_de_features.ipynb`
- `notebooks/06_modelado_e_inferencia_dual.ipynb`
- `notebooks/07_visualizacion_y_tableros.ipynb`

## Nota importante

Los datos pesados no se incluyen en el repositorio por defecto. En Colab se recomienda montar Google Drive o cargar la carpeta `data/` antes de ejecutar el pipeline completo.
