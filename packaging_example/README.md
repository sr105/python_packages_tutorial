# Introduction

This directory shows how a simple laboratory library named `lab.py` can grow overtime and then be broken up to keep it manageable all without breaking the code that uses it. In each of the three examples given, the exact same `work.py` is run with the same results.

# A single module

This example represents just getting started where all of the lab code is in one file named `lab.py`. Look over `work.py` to see how it uses the methods inside the lab module.

```python3
import lab

# We'll use the same work file here for all three package/module patterns to
# show that this code need not change.

def compute_circle_areas(radiuses):
    radiuses_squared = lab.square_a_list(radiuses)
    areas = lab.multiply_a_list_by(radiuses_squared, lab.PI)
    return areas


def get_areas_string(areas):
    return 'The areas are: ' + ', '.join(str(area) for area in areas)


circle_radiuses = [1, 2, 8, 10]
circle_areas = compute_circle_areas(circle_radiuses)
result_string = get_areas_string(circle_areas)
print(result_string)
print(lab.backwards(result_string))
```

And then running it gives this output:

```shell
$ python3 work.py 
The areas are: 3.14159, 12.56636, 201.06176, 314.159
951.413 ,67160.102 ,63665.21 ,95141.3 :era saera ehT
```

# Converting to a package directory

Our lab library has grown, and it's time to break it up into two pieces: computations and string manipulation. To do this, we'll split `lab.py` into two files. Then, the new lab directory will use an `__init__.py` to load the contents of those files into a single namespace so our users won't be able to tell that anything changed. Let's look at the new layout:

```shell
1_and_then_things_started_getting_out_of_hand$ tree
.
├── lab
│   ├── computations.py
│   ├── __init__.py
│   └── string_manipulations.py
└── work.py

1 directory, 4 files
```

And let's examine how `__init__.py` makes `import lab` inside `work.py` look exactly the same as before:

```python3
from .computations import *
from .string_manipulations import *
```

It grabs all of the contents of each submodule and puts all of their contents into the lab package's namespace directly.

# Ever-growing, further nesting of packages is required

Our lab has really become quite a phenomenon, and our `computations.py` submodule has started to get too big to comfortably manage. Let's convert that submodule into its own package just like we did with `lab.py`. We'll break it up into list processing methods and constants. Let's take a look at the new layout:

```shell
2_and_now_we_are_really_growing$ tree
.
├── lab
│   ├── computations
│   │   ├── constants.py
│   │   ├── __init__.py
│   │   └── list_methods.py
│   ├── __init__.py
│   └── string_manipulations.py
└── work.py

2 directories, 6 files
```

In order to continue to maintain our facade that `import lab` looks like `lab.py`, we'll need another `__init__.py` inside our new subpackage. It will work just like the other one, though. Let's see how the new `__init__.py` looks.

```python3
from .list_methods import *
from .constants import *
```

So now, the computations package imports all of its submodules contents into its own namespace such that when the lab package `__init__.py` runs, it will then grab the contents on computations into its own namespace. Really, we're just taking a nested namespace and flattening it so it appears that we have no heirarchy and everything can be pretended to exist in a `lab.py` module.

