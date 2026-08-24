# CURRENCY CONVERTER

#### Video Demo: 

#### Description:

This was a project for my CS50 Python Course which was a **Currency Converter**

What motivated me to do this project was the love to use APIs and interact with them and I wanted to do it as a fully fledged project

##### Running the program:

To run the program you need to make sure that all the libraries in the `requirements.txt` file are installed.
It takes command-line arguments and follows the following format: 
`python currency_converter.py -a/--amount {amount_to_be_converted} -f/--fro {valid_currency_code} -t/--to {valid_currency_code}`


##### Main FILE:

The project uses command line arguments to take input rather than just asking the user for input
I took this approach over the native way of using the input function because I wanted to practice using the ***argparse*** library which seemed interesting to take input from the command-line and a better alternative to the ***sys*** library.
If a user inputs the wrong flags, they get a description of why their input is wrong rather than raising errors. This is enabled by the argparse module method called `add_argument()` which has a `help` parameter that gives a description of what a certain flag does.

I implemented an empty class `LimitError` that is raised if the API request returns back an error with the error code simply being a limit-reached on the monthly requests which didn't require any instances.

The `main` function handles the input and breaks the command line arguments to give the `base_currency`, `quote_currency` and `amount_to_be_converted` which are essential variables in order for the conversion to occur as intended. The three variables are passed to `get_exchange_rate` function.

The `get_exchange_rate` function performs two actions which are: **Retrieving data from the cache file** and **Creating the cache file** if it doesn't exist. Caching helps reduce the burden of requesting everytime and to perform offline requests.

The `update_cache_file` function from the name updates the cache file if the pair being looked for doesn't exist in the cache_file. When testing this function if the pair is already in the cache file it doesn't need to be added there again.

##### Test FILE:

This test file tests whether the main file returns the required values and where necessary it raises the required errors.
It uses ***pytest*** to perform the test on the three functions to check whether they perform and return the required values and raise the required errors.

The `test_update_cache_file` test function checks if the **update_cache_file** function returns the required dictionary and also if an error is raised for the wrong currency code if it exists.

The `test_calculate_amount` test function checks if the **calculate_amount** function returns the required calculation and gives it in the right format.

The `test_get_exchange_rate` test function checks if the **get_exchange_rate** function raises the right error if an error code is given for wrong currency code.

##### API and Caching:
I chose the **ExchangeRateAPI** because it had more requests for a free plan and it was not complex to use and it gave the format in JSON so it was easier to convert to a python `dict`.

For the caching it uses a JSON file which the pair are an array of JSON objects for simple retrieval. The program caches when the pair is not in the JSON file. 

##### Future Features:
To improve the caching in order for it to update everyday in order to get new exchange rates and updated ones.
Allow the user to check for historical dates and exchange rates for comparison purposes.