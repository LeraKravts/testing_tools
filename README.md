issue-01
вводим в терминал
```python3 -m doctest -v -o ELLIPSIS trying_dict.py```

issue-02
вводим в терминал
```pytest test_issues_1_2_morse.py::test_morse_to_english```

issue-03
вводим в терминал
```python3 test_issue_3_test_fit_transform.py```

issue-04
вводим в терминал
```pytest test_issue_4_one_hot_encode.py```

issue-05
вводим в терминал
```coverage run test_what_is_year_now.py
   coverage report -m
   coverage html```

или 
```python3 -m pytest --cov . --cov-report html
```