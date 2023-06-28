# SheetSyncer: Google Sheets and MySQL Data Synchronization

This project is created as a reference and for gaining experience for a job on Upwork.

## Project Description

This project is a FastAPI application that synchronizes data between Google Sheets and MySQL database using the Google Sheets API and MySQL Connector. It retrieves data from Google Sheets and writes it to the MySQL database. It also provides API endpoints for testing the database connection and listing files in Google Drive.

## Requirements

To run the project, you need the following requirements:

- Python 3.x
- Virtual Environment (venv)
- Libraries listed in the `requirements.txt` file

It is recommended to create a virtual environment using venv. With venv, you can create an isolated Python environment and manage project dependencies within that environment.

1. Open the terminal in the project's root directory.
2. Create a venv using the following command:

   ```shell
   python3 -m venv myenv
   ```

3. Activate the created venv:

   ```shell
   source myenv/bin/activate
   ```

4. Now, you can install the required libraries listed in the `requirements.txt` file:

   ```shell
   pip install -r requirements.txt
   ```

   This command will automatically download and install the necessary libraries.

   Note: If you prefer to install the project's libraries directly, you can use the following commands:

   ```shell
   pip install google-api-python-client mysql-connector-python fastapi uvicorn
   ```

## Installation

1. Open the terminal in the project's root directory.
2. Create the `token.json` file and add an authorization file containing your Google API authentication credentials.
3. Create your MySQL database and update the connection settings in the `config` variable.
4. Update the `range_` variable to specify the target range in Google Sheets.
5. Start the application by running the following command in the terminal:

   ```shell
   python main.py
   ```

   The application will run by default at `127.0.0.1:8000`.

## API Endpoints

The project provides the following API endpoints:

- `/api/testdbconnection`: Sends a GET request to test the database connection.
- `/api/testlistfiles`: Sends a GET request to list files in Google Drive.
- `/api/getSheetTable`: Sends a GET request to retrieve data from Google Sheets.
- `/api/syncData`: Sends a GET request to synchronize data from Google Sheets to the MySQL database.

Example requests to test the API endpoints:

- `GET /api/testdbconnection`: To test the database connection.
- `GET /api/testlistfiles`: To list files in Google Drive.
- `GET /api/getSheetTable`: To retrieve data from Google Sheets.
- `GET /api/syncData`: To synchronize data from Google Sheets to the MySQL database.

## License

This project is licensed under the MIT License. For more information, please see the [LICENSE](LICENSE) file.

---