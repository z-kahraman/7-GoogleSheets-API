# SheetSyncer: Google Sheets and MySQL Data Synchronization

SheetSyncer is a Python application that synchronizes data between Google Sheets and a MySQL database. It allows you to fetch data from a specific Google Sheet and store it in a MySQL database, as well as test the database connection and list files from Google Drive.

## Features

- Test MySQL database connection with a simple API endpoint.
- List files from Google Drive using the Google Drive API.
- Fetch data from a Google Sheet and store it in a MySQL database.
- Synchronize data between Google Sheets and MySQL with a single API call.

## Prerequisites

Before running SheetSyncer, make sure you have the following:

- Python 3.7 or above installed
- MySQL database server
- Google Sheets API credentials (JSON file) with necessary permissions
- Google Drive API credentials (JSON file) with necessary permissions

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/sheetsyncer.git
```

2. Navigate to the project directory:

```shell
cd sheetsyncer
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

4. Set up the configuration:

   - Rename the `config.example.py` file to `config.py`.
   - Open `config.py` and provide the necessary configuration values, such as MySQL database credentials and Google API credentials file paths.

## Usage

1. Start the application:

```shell
python main.py
```

2. Access the API endpoints using a web browser or API testing tool:

   - Test database connection: [http://localhost:8000/api/testdbconnection](http://localhost:8000/api/testdbconnection)
   - List files from Google Drive: [http://localhost:8000/api/testlistfiles](http://localhost:8000/api/testlistfiles)
   - Fetch data from Google Sheet: [http://localhost:8000/api/getSheetTable](http://localhost:8000/api/getSheetTable)
   - Synchronize data between Google Sheets and MySQL: [http://localhost:8000/api/syncData](http://localhost:8000/api/syncData)

## Testing

SheetSyncer includes a test suite to ensure the functionality of the application. To run the tests, execute the following command:

```shell
python test.py
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Make sure to replace "your-username" with your actual GitHub username in the clone command. Feel free to modify the content to fit your specific project details and requirements.

Remember to include any additional sections or information that you think would be relevant to your users, such as installation instructions for the MySQL server or how to obtain the necessary Google API credentials.

I hope this helps! Let me know if you have any further questions.