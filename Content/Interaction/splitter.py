from IPython.nbformat import current
from copy import deepcopy as copy

with open('Widgets.ipynb') as f:
    nb = current.reads(f.read())

splits = [[]]
cells = nb['worksheets'][0].cells
for i, cell in enumerate(cells):
    if 'source' in cell and cell['source'].strip().lower() == 'split here':
        splits.append([])
    else:
        splits[-1].append(cell)

for i, split in enumerate(splits):
    new_nb = copy(nb)
    new_nb['worksheets'][0]['cells'] = split
    with open('Widgets%d.ipynb' % (i+1), 'w') as f:
        f.write(current.writes(new_nb))
