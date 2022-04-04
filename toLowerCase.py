import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Products_in_database_with_MSRP.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = ['a41312', 'a11515', 's505ms', 'a49022', 'a59523', 'a71514', 'p608ms', 'zt464', 's119ln', 'p608ls', 's231ml', 'a21510', 'j123ml', 'a41022', 'ac41511', 'bb410', 'zt465', 'c502', 'a59000', 'zw013', 'j920l', 'zt481', 's231lt', 'zw005', 'a11519', 'a59510', 'a41012', '60111', '99200', 'zw350', 'a41011', 'a71519', 'zj355', 'ac42412', '44520', 'ac42812', 'zt566', 'ac41412', 'zp902', 'a59100', '44522', 'a49012', 'zt478', 'a59513', 'a59520', 'ac42912', '64011', 'zt480', 'nc10100']


# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item in expenses:
    worksheet.write(row, col,     item)
    row += 1

workbook.close()
