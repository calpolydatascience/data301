# encoding: utf-8
"""Vizualize NumPy arrays using ipythonblocks.

To enable the automatic vizualization of arrays::

    import vizarray
    vizarray.enable()

To disable this::

    vizarray.disable()

To set the colormap (to any valid matplotlib colormap name)::

    vizarray.set_cmap('jet')

To set the block_size in px (default is 30px)::

    vizarray.set_block_size(10)

To turn off autoscaling of arrays:

    vizarray.set_scale(False)
"""

import ipythonblocks as ipb
from ipythonblocks import BlockGrid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

_cmap = 'jet'
_scale = True
_vmin = None
_vmax = None
_block_size = 30

def set_cmap(cmap_name):
    """Set the global value of cmap."""
    global _cmap
    _cmap = cmap_name


def set_scale(s):
    """Set the global value of scale."""
    global _scale
    _scale = s


def set_vmin(vm):
    """Set the global value of vmin."""
    global _vmin
    _vmin = vm


def set_vmax(vm):
    """Set the global value of vmax."""
    global _vmax
    _vmax = vm


def set_block_size(bs):
    """Set the global value of block_size."""
    global _block_size
    _block_size = bs


def list_colormaps():
    """List all of the matplotlib colormap strings."""
    return sorted(m for m in plt.cm.datad if not m.endswith("_r"))


def _value_to_color(value, cmap):
    """Convert a value in the range [0,1] to an RGB tuple using a colormap."""
    cm = plt.get_cmap(cmap)
    rgba = cm(value)
    return [int(round(255*v)) for v in rgba[0:3]]


def vizarray(x, cmap=None, scale=None, vmin=None, vmax=None, block_size=None):
    """Visualize a NumPy array using ipythonblocks."""
    if not (x.ndim == 2 or x.ndim == 1):
        raise TypeError('This function only works with 1 or 2 dimensional arrays')
    global _cmap, _scale, _vmin, _vmax, _block_size
    cmap = cmap if cmap is not None else _cmap
    scale = scale if scale is not None else _scale
    vmin = vmin if vmin is not None else _vmin
    vmax = vmax if vmax is not None else _vmax
    block_size = block_size if block_size is not None else _block_size
    base = x.base if x.base is not None else None
    data = x.copy()
    if scale:
        n = colors.Normalize(vmin=vmin, vmax=vmax)
        if base is not None:
            n.autoscale(base)
        data = n(data)
    if data.ndim == 1:
        rows = 1
        cols = data.shape[0]
        bg = BlockGrid(cols, rows, block_size=block_size)
        for col in range(cols):
            bg[0,col] = _value_to_color(data[col], cmap)
    elif data.ndim == 2:
        rows = data.shape[0]
        cols = data.shape[1]
        bg = BlockGrid(cols, rows, block_size=block_size)
        for row in range(rows):
            for col in range(cols):
                bg[row, col] = _value_to_color(data[row, col], cmap)
    return bg


def _array_to_html(a):
    return vizarray(a)._repr_html_()


def enable():
    """Enable automatic visualization of NumPy arrays in the IPython Notebook."""
    try:
        from IPython.core.getipython import get_ipython
    except ImportError:
        raise ImportError('This feature requires IPython 1.0+')
    ip = get_ipython()
    f = ip.display_formatter.formatters['text/html']
    f.for_type(np.ndarray, _array_to_html)


def disable():
    """Disable automatic visualization of NumPy arrays in the IPython Notebook."""
    try:
        from IPython.core.getipython import get_ipython
    except ImportError:
        raise ImportError('This feature requires IPython 1.0+')
    ip = get_ipython()
    f = ip.display_formatter.formatters['text/html']
    f.type_printers.pop(np.ndarray, None)

