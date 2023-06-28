import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import mysql.connector
from fastapi import FastAPI, HTTPException, Response
import os

app = FastAPI()

# Load the authentication key
current_dir = os.path.dirname(os.path.abspath("token.json"))
credentials = Credentials.from_authorized_user_file(current_dir + '/token.json')
# Create a service on the Google Sheets API
service = build('sheets', 'v4', credentials=credentials)
# Use the Google Drive API to list all files
drive_service = build('drive', 'v3', credentials=credentials)

# MySQL connection settings
config = {
    'user': 'root',
    'password': 'test',
    'host': 'localhost',
    'database': 'test_db',
    'raise_on_warnings': True
}

# Spreadsheet API settings

# The A1 notation of the values to retrieve.
range_ = 'upwork-test!A:D'  # TODO: Update placeholder value.
# The default render option is ValueRenderOption.FORMATTED_VALUE.
value_render_option = 'FORMATTED_VALUE'  # TODO: Update placeholder value.
# The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
date_time_render_option = 'FORMATTED_STRING'  # TODO: Update placeholder value.

def test_db_connection():
    try:
        # Create a MySQL connection
        cnx = mysql.connector.connect(**config)
        cnx.close()
        return True
    except mysql.connector.Error as err:
        return {"message": "DB connection failed", "error": str(err)}

# Test DB Connection API
@app.get("/api/testdbconnection")
async def test_db_connection_api():
    if test_db_connection():
        return {"message": "DB connection successful"}
    else:
        raise HTTPException(status_code=500, detail="DB connection failed")

# Test Google Drive API
@app.get("/api/testlistfiles")
async def list_files():
    files = drive_service.files().list().execute().get('files', [])

    result = [{"name":  file['name'], "web_view_link": f"https://drive.google.com/file/d/{file['id']}/view?usp=sharing"} for file in files]

    return {"result": result}

@app.get("/api/getSheetTable")
async def get_table():
    files = drive_service.files().list().execute().get('files', [])
    for file in files:
        if file['mimeType'] == 'application/vnd.google-apps.spreadsheet':
            if(file['name'] == "test_db"):
                # The ID of the spreadsheet to retrieve data from.
                spreadsheet_id = file['id']
                break

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
    response = request.execute()

    result = response['values']

    return {"result": result}

@app.get("/api/syncData")
def sync_data():
    # Retrieve data using the Google Sheets API
    files = drive_service.files().list().execute().get('files', [])
    for file in files:
        if file['mimeType'] == 'application/vnd.google-apps.spreadsheet':
            if(file['name'] == "test_db"):
                # The ID of the spreadsheet to retrieve data from.
                spreadsheet_id = file['id']
                break

    sheet_range = range_  # Specify the desired sheet and cell range
    sheet_data = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
    values = sheet_data.get('values', [])

    # Create a MySQL connection
    cnx = mysql.connector.connect(**config)

    # Write the retrieved data to the MySQL database
    cursor = cnx.cursor()
    for row in values[2:]:
        # For example, let's write the data to the 'students' table
        query = "INSERT INTO {} (name, surname, school) VALUES (%s, %s, %s)".format("students")
        cursor.execute(query, (row[1], row[2], row[3]))
    cnx.commit()
    cursor.close()
    cnx.close()

    return {"message": "Data synchronized successfully"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
