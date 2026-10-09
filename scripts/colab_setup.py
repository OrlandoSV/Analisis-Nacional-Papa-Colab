"""Bootstrap para ejecutar este repositorio en Google Colab.

Este script asegura que:
- la raíz del proyecto quede en PYTHONPATH,
- el entorno se encuentre en el directorio correcto,
- se instalen las dependencias necesarias si se ejecuta desde Colab.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def find_repo_root() -> Path:
    """Devuelve la raíz del repo en ejecución."""
    candidates = [
        Path.cwd(),
        Path('/content'),
        Path('/workspace'),
        Path.home(),
    ]

    for candidate in candidates:
        if (candidate / 'src').exists() and (candidate / 'requirements.txt').exists():
            return candidate.resolve()

    # Si se ejecuta desde una subcarpeta del repo, busca hacia arriba.
    current = Path.cwd().resolve()
    for parent in [current, *current.parents]:
        if (parent / 'src').exists() and (parent / 'requirements.txt').exists():
            return parent

    raise FileNotFoundError(
        'No se encontró la raíz del repositorio. Ejecuta este script desde la carpeta del proyecto.'
    )


def configure_pythonpath(repo_root: Path) -> None:
    repo_str = str(repo_root)
    if repo_str not in sys.path:
        sys.path.insert(0, repo_str)
    os.environ['PYTHONPATH'] = repo_str + os.pathsep + os.environ.get('PYTHONPATH', '')
    os.chdir(repo_root)
    print(f'[colab_setup] Proyecto configurado en: {repo_root}')


def install_requirements_if_needed(repo_root: Path) -> None:
    """Instala dependencias solo en Colab y cuando existe requirements.txt."""
    is_colab = 'google.colab' in sys.modules
    if not is_colab:
        print('[colab_setup] No se detecta Google Colab; se omite la instalación automática.')
        return

    requirements = repo_root / 'requirements.txt'
    if not requirements.exists():
        print('[colab_setup] No existe requirements.txt en la raíz del proyecto.')
        return

    print('[colab_setup] Instalando dependencias del proyecto...')
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', str(requirements)], check=True)


def main() -> None:
    repo_root = find_repo_root()
    configure_pythonpath(repo_root)
    install_requirements_if_needed(repo_root)

    print('[colab_setup] Listo. El repositorio puede importarse desde Python y Colab.')
    print('[colab_setup] Ejemplo: from src.infrastructure.config import PROJECT_ROOT')


if __name__ == '__main__':
    main()
