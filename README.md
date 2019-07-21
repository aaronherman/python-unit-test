# Unit Testing with Python

## Running the unit tests
You can run the unit tests with the following command
```
python3 unit_tests.py
```

`unit_tests.py` imports the calculator that we created and the `unittest` module needed to set up and run the tests.

## Add more unit tests
You should add more test cases to the `unit_tests.py` file. The general structure is to have a class that takes in the unittest module: `class TestCalculator(unittest.TestCase)`. Then, add functions that test a specific part of the code written in calculator.py

### Testing the class
In order to test a class in Python, you'll simply import it and then have a setup function which will create the object. In our case, we set self.a and self.b to two different numbers.

You should test for subtraction, division and multiplication.

### Testing a function
There is also an addition function in `calculator.py`. This function takes in an list of items (currently, it does not check to see if they're numbers) and then returns the sum.

## How Travis CI Works
[![Build Status](https://travis-ci.org/aaronherman/python-unit-test.svg?branch=master)](https://travis-ci.org/aaronherman/python-unit-test)


Once you have created a project on GitHub, you will need to add a `.travis.yml` file which sets the configurations for Travis. For instance, what languages will you be using? Do you need a specific operating system? If something fails, should it email a certain address? 

You also need to set the script that you'd like to run. This way, Travis will run the test files you specify and report any non-zero exit codes. Similar to how we run unit tests locally, you add `python unit_tests.py` to the scripts section of the `.yaml` file.

View Travis: https://travis-ci.org/aaronherman/python-unit-test/builds

## More information
[.travis.yml](https://docs.travis-ci.com/user/languages/python/)
[Overview](https://github.com/softwaresaved/build_and_test_examples/blob/master/travis/HelloWorld.md)