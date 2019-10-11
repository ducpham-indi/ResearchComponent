import sys, os, importlib, importlib.machinery, pdb, traceback, subprocess, os.path


def load_scripts(rel_path: str, module_name: str, file: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path += rel_path
    sys.path.append(dir_path)
    loader = importlib.machinery.SourceFileLoader(
        module_name, os.path.join(dir_path, file)
    )
    module = loader.load_module()
    return module
