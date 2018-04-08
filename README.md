# Unit testing with Travis CI

[![Build Status](https://travis-ci.org/aaronherman/python-unit-test.svg?branch=master)](https://travis-ci.org/aaronherman/python-unit-test)
## How Travis CI Works
Once you have created a project on GitHub, you will need to add a `.travis.yml` file which sets the configurations for Travis. For instance, what languages will you be using? Do you need a specific operating system? If something fails, should it email a certain address? 

You also need to set the script that you'd like to run. This way, Travis will run the test files you specify and report any non-zero exit codes.

View Travis: https://travis-ci.org/aaronherman/python-unit-test/builds

## Running the unit tests
You can run the unit tests with the following command
```
python3 unit_tests.py
```

## Add more unit tests
You should add more test cases to the `unit_tests.py` file. You should test for subtraction, division and multiplication. 