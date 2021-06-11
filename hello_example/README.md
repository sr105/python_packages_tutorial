# Introduction

Let's see how three methods of python packaging work by example. In this directory, there are three types of hello applications: a single hello.py module, a hello_dir package, and a hello_zip_dir package bundled into a zip file.

# Simple Module

A single `hello.py` module consisting of the following:

```
#!/usr/bin/env python3

def say_hello():
    print('Hello from a module')
    
say_hello()
```

The first line is a hint to our terminal shell of which program needs to be run in order to process this file.

Run it with python normally:

```
$ python3 hello.py
Hello from a module
$
```

To run it by itself, we have to tell the shell that the file is executable:

```
$ chmod a+x hello.py
$ ./hello.py
Hello from a module
$
```

# Package directory

Any directory can be a Python package. Note: older versions of Python require an `__init__.py` file to exist (even if empty). Any directory given to python as the source of a program will look for a `__main__.py` file to run within the directory. Let's look at the simple module above converted to a directory.

```
$ ls hello_dir
hello.py __main__.py
```

Since `__main__.py` is the file that will be run, our hello.py only needs the `say_hello()` method.

```
def say_hello():
    print('Hello from a directory')
```

The `__main__.py` file needs to import `hello.py` and run the `say_hello()` method.

```
import hello

hello.say_hello()
```

```
$ python3 hello_dir
Hello from a directory
```

Since you can't run a directory itself from a shell, this is as far as we can go with directories.

# Zip file package

A package directory can be zipped and Python will happily run it just as if it were a directory. Let's create an almost identical version of `hello_dir`.


```
$ ls hello_zip_dir
hello.py __main__.py
```

Just like before, since `__main__.py` is the file that will be run, our hello.py only needs the `say_hello()` method.

```
def say_hello():
    print('Hello from a directory inside a zip file')
```

The `__main__.py` file needs to import `hello.py` and run the `say_hello()` method.

```
import hello

hello.say_hello()
```

`hello_zip_dir` is still a valid package, and we can run it just like above.

```
$ python3 hello_zip_dir
Hello from a directory inside a zip file
```

Our message isn't correct yet. Let's fix it by creating and running a zip file.

```
$ cd hello_zip_dir
hello_zip_dir$ zip ../hello.zip hello.py __main__.py
  adding: hello.py (deflated 3%)
  adding: __main__.py (deflated 15%)
hello_zip_dir$ cd ..
$ python3 hello.zip
Hello from a directory inside a zip file
```

Much better, but can we run the zip file itself? Sure, we only need to tell the shell which program run and pass the zip file to as input. Remember the `#!/usr/bin/env python3` line from above? That told the shell to run python3 and pass all of the contents of that file to the running python3. Let's see how we can do the same with a zip file.

```
$ echo '#!/usr/bin/env python3' | cat - hello.zip > hello
$ chmod a+x hello
$ ./hello
Hello from a directory inside a zip file
```

The cat command concatenates all of its inputs and then we redirect all of the output into a new file we're naming `hello`. The `-` argument to cat means to use what ever is passed to it. In this case, the echo command passes the line that shell needs. The end result is a file named `hello` that is a single line of instruction text for shell followed immediately by a binary zip file.
