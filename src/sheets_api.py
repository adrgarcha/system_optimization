import gspread

scopes = ["https://www.googleapis.com/auth/spreadsheets"]

sheet_id = "1yAs92iiEneSBRiSyXtK1d4oapqa_D4iwcmQGAWMuzvM"

gc = gspread.oauth(
    credentials_filename="../credentials.json",
    authorized_user_filename="../authorized_user.json"
)

sheet = gc.open_by_key(sheet_id)

def export_to_sheets(dataframe, worksheet_title):
    if worksheet_title not in [sheet.title for sheet in sheet.worksheets()]:
        worksheet = sheet.add_worksheet(title=worksheet_title, rows="100", cols="100")
    else:
        worksheet = sheet.worksheet(worksheet_title)
    worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())