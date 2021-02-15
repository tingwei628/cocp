## Tests

```
pytest lexer_test.py
```

```
pytest lexer_test.py -k '[function_name]'
```


### Reference:
https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery

```
In those directories, search for test_*.py or *_test.py files, imported by their test package name.

From those files, collect test items:

    test prefixed test functions or methods outside of class

    test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)


```
