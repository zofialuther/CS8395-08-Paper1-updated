```python
def foo():
    try:
        method1()
        method2()
        method3()
    except NumberFormatException:
        # handle NumberFormatException
    except FileNotFoundException:
        # handle FileNotFoundException
    except IOException as e:
        # re-throw IOException
        raise
    except UnsupportedDataTypeException:
        # handle UnsupportedDataTypeException
```