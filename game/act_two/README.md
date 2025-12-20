# `act_two` 文件夹内容

## 子文件夹

- **[py](./py)**: Contains the Python code for the code used in Act Two of DDLC.
- **\_\_pycache\_\_**: Contains the compiled Python files for the code used in Act Two - Four of DDLC. This should normally not appear in your mod nor in packaged mod templates, but if it exists, ignore it.

## 文件
- **README.md**: This file, which provides an overview of the contents of the `act_two` folder.
- **\_\_init\_\_.py**: 一个测试用途的空白文件。
- **[poems_special.rpy](./poems_special.rpy)**: Defines the special poems that the player can see during Act Two. Only three poems are ever shown to the player which are selected at random by *[splash.rpy](../splash.rpy)*.

## 已被移走的文件
- **glitchtext.rpy**: This file was moved from the `game/act_two/py` folder as *[glitchtext_ren.py](./py/glitchtext_ren.py)* as this is purely a Ren'Py file with a Python function.