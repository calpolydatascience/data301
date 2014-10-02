# Installation note

## Anaconda

* Don't use the Anaconda Launcher for IPython as it runs in `\Documents\IPython` Notebooks on Windows.

## Running from IPython master

It is pretty simple to have students run from IPython master.

First, you need to build a wheel. Install `git` and `pip install wheel` to get the dependencies for
building the wheel. Then run:

```bash
$ pip wheel --no-deps git+https://github.com/ipython/ipython.git#egg=ipython[all]
$ ls
ipython-3.0.0_dev-py2-none-any.whl
```

You can either directly distribute the wheel file and install by running:

```
$ pip install --upgrade ipython-3.0.0_dev-py2-none-any.whl
```

Or you can post the wheel online somewhere. I have posted it as an official release binary in a GitHub
repo. Then install using:

```
$ pip install --upgrade https://github.com/ellisonbg/ds4e/releases/download/0.1/ipython-3.0.0_dev-py2-none-any.whl
```

If the user already has this version installed, they may have to do `pip uninstall ipython` first. I 
have tested this and it works on top of a default Anaconda.

