# Allan please dont forget to delete ur Oauth and Google sheets token k thx
import gspread 
import Processingdoc

gc = gspread.service_account(filename="pleaseworkk.json")

# Open a sheet from a spreadsheet in one go
wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1VbY_7pU1xZDDdw5o-tzKoRqI6VOeyLiQJK5xgdG_23M/edit?gid=0#gid=0")
# Update a range of cells using the top left corner address
# wks.update([[1, 2], [3, 4]], 'A1')
worksheet = wks.sheet1
# Or update a single cell

k =0
for i in Processingdoc.words:
    k+=1
    worksheet.update_acell('B'+str(k), i.get_text(strip = True))

# Format the header
#wks.format('A1:B1', {'textFormat': {'bold': True}})