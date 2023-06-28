# SheetSyncer Test Suite

This repository contains a test suite for the SheetSyncer application. The test suite is implemented using the `unittest` module and covers various endpoints and functionalities of the SheetSyncer API.

## Prerequisites

Before running the tests, make sure you have the following:

- Python 3.7 or above installed
- SheetSyncer application running locally (or accessible endpoint URLs)

## Installation

1. Clone the repository:

```shell
git clone https://github.com/z-kahraman/7-GoogleSheets-API.git
```

2. Navigate to the project directory:

```shell
cd test
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

To run the test suite, execute the following command:

```shell
pytest test_main.py
```

The test suite will automatically discover the test cases and execute them. You will see the test results in the console, indicating whether each test passed or failed.

## Customizing Tests

The test suite includes the following test cases:

- `test_testdbconnection`: Tests the `/api/testdbconnection` endpoint to ensure a successful database connection.
- `test_listfiles`: Tests the `/api/testlistfiles` endpoint to ensure the response contains the expected structure.
- `test_getsheettable`: Tests the `/api/getSheetTable` endpoint to ensure the response contains the expected structure.
- `test_syncdata`: Tests the `/api/syncData` endpoint to ensure a successful data synchronization.

Feel free to modify or add additional test cases according to your requirements. You can create new test methods following the same pattern as the existing ones.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
