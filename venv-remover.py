import os
import subprocess
import shutil

VENV_NAMES = ['venv', '.venv', 'env', '.env']

def find_virtualenvs(root_dir):
    for dirpath, dirnames, _ in os.walk(root_dir):
        for venv_name in VENV_NAMES:
            if venv_name in dirnames:
                yield os.path.join(dirpath, venv_name)

def export_requirements(venv_path):
    pip_path = os.path.join(venv_path, 'Scripts', 'pip.exe') if os.name == 'nt' else os.path.join(venv_path, 'bin', 'pip')
    if not os.path.exists(pip_path):
        print(f'pip não encontrado em {venv_path}')
        return
    req_path = os.path.join(os.path.dirname(venv_path), 'requirements.txt')
    try:
        subprocess.run([pip_path, 'freeze'], check=True, stdout=open(req_path, 'w'), stderr=subprocess.PIPE)
        print(f'Requirements exportado para {req_path}')
    except Exception as e:
        print(f'Erro ao exportar requirements de {venv_path}: {e}')

def remove_virtualenv(venv_path):
    try:
        shutil.rmtree(venv_path)
        print(f'Ambiente virtual removido: {venv_path}')
    except Exception as e:
        print(f'Erro ao remover {venv_path}: {e}')

if __name__ == '__main__':
    root = os.getcwd()
    for venv in find_virtualenvs(root):
        export_requirements(venv)
        remove_virtualenv(venv)