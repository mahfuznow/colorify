### Build Distribution
```python
python setup.py sdist bdist_wheel
```

### Upload
```python
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

#or
twine upload dist/*
#then give username and password
#DONE
```
### Update
```python
#first increment the version number in setup.py
#delete dist directory
#then build distribution
python setup.py sdist bdist_wheel
twine upload dist/*

```
> If error occurs while updating (File already exists):
> try: 
```python
twine upload --skip-existing dist/*
```