Title: Python import mechanics considered annoying
Tags: python, programming
Date: 2015-06-19T22:18

This may be old knowledge for most python programmers, but I discovered what I consider to be a design flaw in python's import mechanics, which leads to tight coupling and strange side effects.

I have 5 python files:

**~/main.py**:

    import a, b

**~/a.py**:

    import lib.c

**~/b.py**:

    import lib.d
    print "b.py called lib.c.test(): {}".format(lib.c.test())
    print "b.py called lib.d.test(): {}".format(lib.d.test())

**~/lib/c.py**:

    def test():
        return "c reply"

**~/lib/d.py**:

    def test():
        return "d reply"

I also have a blank **__init__.py** in the `/` and `/lib` folders, and each `.py` file starts with `#!/usr/bin/env python`.

Running gives me this:

    ~$ PYTHONPATH=~/ python main.py
    b.py called lib.c.test(): c reply
    b.py called lib.d.test(): d reply

Great! My file (**~/b.py**) is coded correctly. Deploy it, job done, walk away.

Later someone edits **~/a.py** and no longer imports `lib.c`, since whatever it did isn't needed anymore. Now my code in **~/b.py** (which admittedly had a bug in it) no longer works:

    ~$ PYTHONPATH=~/ python main.py
    Traceback (most recent call last):
      File "main.py", line 2, in <module>
        import a,b
      File "/home/steve/b.py", line 3, in <module>
        print "b.py called lib.c.test(): {}".format(lib.c.test())
    AttributeError: 'module' object has no attribute 'c'

So python was silently letting my broken code run because of a side effect. It worked because **~/a.py** was importing a module I needed. This sets up code to run in a context that is incredible coupled with *all other code* in the same process.

## Python's two step import

According to [StackOverflow][import-mechanics], python's import statement does two things in sequence:

1. Loads the modules into the classloader
2. Maps the classloader entities into the local namespace

This means that when **~/a.py** runs `import lib.c` it does the following:

1. Tell the classloader to load the `lib` module
2. Tell the classloader to load the `c` module within `lib`
3. Map the `lib` module to the string '''lib''' in the namespace

Later, when **~/b.py** runs `import lib.d`, it runs:

1. Classloader doesn't need to load the `lib` module, since it already has
2. Tell the classloader to load the `d` module within `lib`
3. Map the `lib` module to the string '''lib''' in the namespace

So then, within **~/b.py**, we can use `lib` to get ahold of the classloader's loaded module, then traverse down to `lib.c` (which is already loaded because of **~/a.py**), and use that submodule.

## Solutions?

Ideally, this kind of side-effect would be blocked by the classloader so code that compiles, compiles because it has written the correct imports, **not because it was run in a context that had things imported already**. Because this is not true, I guess setting up a Jenkins instance with a linter is probably the next best solution. I'll be working on that next.

[import-mechanics]: http://stackoverflow.com/questions/1917958/python-import-mechanics
