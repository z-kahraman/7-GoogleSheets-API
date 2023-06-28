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

## test_main.py

This file is a test file used to test the `main.py` file.

### Usage

1. Open the terminal and run the `test_main.py` file using the following command:

   ```shell
   pytest test_main.py
   ```

2. The `test_main.py` file will test the functions in `main.py` and verify the results.

### Notes

- The `test_main.py` file helps in testing the `main.py` file for its testability and correctness.
- It checks if the functions in `main.py` are working as expected and producing the desired outputs.

## Contributing

Contributions to this project are

 always welcome. If you find any issues or want to contribute improvements, please feel free to open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions or need any assistance, please feel free to contact me at [zaferkahraman123@gmail.com](mailto:zaferkahraman123@gmail.com).

---

# Docker Compose Configuration for MySQL and Adminer

This project is configured to start MySQL and Adminer using Docker Compose.

## Getting Started

You can run this project on your local machine by following the steps below.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your local machine.

- You can follow the resources [here](https://docs.docker.com/get-docker/) to install Docker.
- You can follow the resources [here](https://docs.docker.com/compose/install/) to install Docker Compose.

### Installation

1. Clone or download this project:

   ```shell
   git clone https://github.com/z-kahraman/7-GoogleSheets-API.git
   ```

2. Navigate to the project directory:

   ```shell
   cd <project_directory>
   ```

3. Start the MySQL and Adminer containers using Docker Compose:

   ```shell
   docker-compose up -d
   ```

4. To access the Adminer interface in your browser, visit [http://localhost:8080](http://localhost:8080).

   - Server: `db`
   - Username: `root`
   - Password: `test`
   - Database: `test_db` (you can change it as desired)

## Usage

- You can use the Adminer interface to access the MySQL database.
- Use `localhost:3306` for the database connection.

## Contributing

1. Fork this repository (`https://github.com/z-kahraman/7-GoogleSheets-API.git`).
2. Create a new branch (`git checkout -b feature/xyz`).
3. Make changes and commit them (`git commit -am 'Add some xyz'`).
4. Push the branch (`git push origin feature/xyz`).
5. Open a pull request.

## License

This project is licensed under the MIT License. For more information, please see the [LICENSE](LICENSE) file.
```

Please make sure to replace `<repository_link>` and `<project_directory>` with the appropriate values for your project.