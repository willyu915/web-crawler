import gspread
from oauth2client.service_account import ServiceAccountCredentials

# config setting 
auth_json_path = 'web-crawler-220526-d9f351eec2ce.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

# link
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
spreadsheet_key = '1qYRc7rW7apLNZHLVhxZKtpeo3YnOD4iSa-Zqpi0ujOw'
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

# get values
records = sheet.get_all_values()
print(records)

# update 
sheet.update('A1:B2', [[1, 2], [3, 4]])
