import nbformat as nbf
from pathlib import Path
from glob import glob

def strip_code_lines(code:str) -> str:
    lines = code.split('\n')
    new_lines = []
    for idx in range(len(lines)):
        if lines[idx].startswith('#'):
            to_add = lines[idx]
            try:
                if not lines[idx+1].startswith('#'):
                    to_add += '\n'
            except IndexError:
                pass
            new_lines.append(to_add)
    return '\n'.join(new_lines)

def strip_notebook(path_to_notebook:str|Path) -> nbf.NotebookNode:
    ntbk = nbf.read(path_to_notebook, nbf.NO_CONVERT)
    cells_to_keep = []
    for cell in ntbk.cells:
        if cell.cell_type == "markdown" or cell.source.startswith('#*'):
            add_cell = cell
        else:
            new_content = strip_code_lines(cell.source)
            add_cell = nbf.v4.new_code_cell(source=new_content)
        cells_to_keep.append(add_cell)
    new_ntbk = ntbk
    new_ntbk.cells = cells_to_keep
    return new_ntbk

def save_notebook(notebook:nbf.NotebookNode, path:str|Path) -> None:
    nbf.write(notebook, path, version=nbf.NO_CONVERT)

if __name__ == '__main__':

    folders = [x for x in Path().iterdir() if x.is_dir() and x.name[0].isdigit()]
    save_dir = Path('built_workbooks')
    save_dir.mkdir(exist_ok=True)

    for folder in folders:
        folder_path = Path(folder)
        files = folder_path.glob('*.ipynb')
        for file in files:
            if not 'workbook' in file.name and not 'exercises' in file.name:
                new_notebook = strip_notebook(file)
                new_path = save_dir / Path(file.stem + '_workbook' + file.suffix)
                save_notebook(new_notebook, new_path)   