## Jinandjup

This is a python package for generating jupyter notebooks from templates. It works as a preprocessor for nbconvert. Just put a 'jinja' tag in the cell metadata of any cell you want to run the jinja substitution on (see the nbconvert example in the examples folder). Then create a config.py file (again see the example for details)
and run the following command:

`jupyter nbconvert --config config.py`

To test out templated code before running nbconvert, there is also a magic command `%%jinandjup` which, when
followed by a dictionary of values to substitute, will treat the cell as a jinja template. 
The values will be substituted and the cell will be run. For debugging purposes the magic also prints out
the templated code so you can see exactly what it looks like after the substitution. See the magic example
in the examples folder for more information.

I mostly wrote this to get a better understanding of writing basic extensions of jupyter, but I hope it will
also be useful to someone.