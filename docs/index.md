# Syngle

[![pypi](https://img.shields.io/pypi/v/syngle.svg)](https://pypi.python.org/pypi/syngle)
[![license](https://img.shields.io/github/license/valentincalomme/syngle.svg)](https://github.com/valentincalomme/syngle/blob/master/LICENSE)
[![downloads](https://img.shields.io/pypi/dm/syngle.svg)](https://pypistats.org/packages/syngle)
[![docstr-coverage](https://raw.githubusercontent.com/ValentinCalomme/syngle/master/docs/assets/docstr-coverage.svg)](https://github.com/ValentinCalomme/syngle/blob/master/docs/assets/docstr-coverage.svg)
[![coverage](https://raw.githubusercontent.com/ValentinCalomme/syngle/master/docs/assets/coverage.svg)](https://github.com/ValentinCalomme/syngle/blob/master/docs/assets/coverage.svg)

---

**Documentation**: <a href="https://valentincalomme.github.io/syngle/" target="_blank">https://valentincalomme.github.io/syngle/</a>

**Source Code**: <a href="https://github.com/ValentinCalomme/syngle/" target="_blank">https://github.com/ValentinCalomme/syngle/</a>

---

## Table of Contents

  - [About](#about)
  - [Installation](#installation)
  - [Usage](#usage)

## About

Simple package implementing the Singleton pattern as a metaclass.

## Installation

Simply pip install the package!

```
pip install syngle
```

Or if you are using poetry:

```
poetry add syngle
```

The package only has Python as a dependency to remain. It was developed for Python 3.7+ and has not been tested for prior versions.

## Usage

In order to make a class implement the singleton pattern, you can either use a metaclass or a decorator. Functionally, both will work the same way.

### As a metaclass

Simply import the Singleton class and make your classess extend it.

```python
from syngle import Singleton

class MyClass(metaclass=Singleton):

    pass

myclass1 = MyClass()
myclass2 = MyClass()

assert myclass1 is myclass2
```

### As a decorator

```python
from syngle import singleton

@singleton
class MyClass:

    pass

myclass1 = MyClass()
myclass2 = MyClass()

assert myclass1 is myclass2
```
