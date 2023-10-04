from oauth2client.service_account import ServiceAccountCredentials
# pip install oauth2client
import gspread


def googleSheetOpen():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "/Users/rayrajnish/PycharmProjects/Scrapping/src/helper/secretkeysjson/websitedatascrapping-398805"
        "-b82ee56d2512.json", scope)
    client = gspread.authorize(creds)
    current_sheet = client.open('DataScrappingFromWeb').sheet1
    return current_sheet
