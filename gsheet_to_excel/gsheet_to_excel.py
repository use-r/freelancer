import gspread
import xlsxwriter
import pandas as pd
import os
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def get_credentials():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    CLIENT_SECRET_FILE = r"client_secret.json"
    APPLICATION_NAME = 'your app name'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
        credential_dir, 'sheets.googleapis.com-python-quickstart.json'
    )

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    dt = input('Date : ')  # example : '25-09-2017'
    tm = input('Time : ')  # example : '17:30'
    credentials = get_credentials()
    sheet_id = "your sheet id"
    gc = gspread.authorize(credentials)
    sht = gc.open_by_key(sheet_id)

    ad_list = sht.get_worksheet(1)
    ad_rank = sht.get_worksheet(0)
    ad_list_rows = ad_list.get_all_values()
    ad_rank_rows = ad_rank.get_all_values()
    ad_list_rows[0].extend(['Ad Ranking', 'Page Ranking'])

    for ad_rank_row in ad_rank_rows:
        if dt in ad_rank_row[0] and tm in ad_rank_row[1]:
            trg_row = ad_rank_row
            break
    else:
        print('No data matched')

    for ad_list_row, ad_rank_val in zip(ad_list_rows[1:], trg_row[2:]):
        ad_rank_val = ad_rank_val.split(';')
        ad_list_row.extend(ad_rank_val)

    df = pd.DataFrame(ad_list_rows[1:], columns=ad_list_rows[0])
    print(df)

    write_to_excel(ad_list_rows, 'output.xlsx')


def write_to_excel(data, fname):
    wb = xlsxwriter.Workbook(fname, options={'strings_to_urls': False})
    ws = wb.add_worksheet('sheet1')

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            ws.write(i, j, val)

    wb.close()


if __name__ == "__main__":
    main()
