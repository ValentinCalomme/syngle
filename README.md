# Syngle


[![pypi](https://img.shields.io/pypi/v/syngle.svg)](https://pypi.python.org/pypi/syngle) [![license](https://img.shields.io/github/license/valentincalomme/syngle.svg)](https://github.com/valentincalomme/syngle/blob/master/LICENSE)

 <!-- [![downloads](https://img.shields.io/pypi/dm/syngle.svg)](https://pypistats.org/packages/syngle) -->
---

**Documentation**: <a href="https://valentincalomme.github.io/syngle/" target="_blank">https://valentincalomme.github.io/syngle/</a>

**Source Code**: <a href="https://github.com/ValentinCalomme/syngle/" target="_blank">https://github.com/ValentinCalomme/syngle/</a>

---

## Table of Contents

  - [About](#about)
  - [Installation](#installation)
  - [Usage](#usage)

## About

Simple package implementing the Singleton pattern as a mixin class.

## Installation

Simply pip install the package!

```
pip install syngle
```

The package only has Python as a dependency to remain. It was developed for Python 3.8+ and has not been tested for prior versions.

## Usage

Simply import the Singleton class and make your classess extend it.

```python
from syngle import Singleton

class MyClass(Singleton):

    pass

myclass1 = MyClass()
myclass2 = MyClass()

assert myclass1 is myclass2
```
