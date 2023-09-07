import csv
import datetime
import sys
import os

if __name__ == '__main__':
    purchase_sku = []
    purchase_list = []

    presale_order = []

    with open("预售.csv", 'r', encoding='utf-8') as f:
        file = csv.reader(f)
        next(file)
        for row in file:
            if row[0] != "" and row[0] != None:
                # print(row[0])
                item = []
                sku = row[0].strip()
                purchase_sku.append(sku)
                date = row[1]
                try:
                    start_date = datetime.datetime.strptime(date, '%Y/%m/%d').date()
                except:
                    start_date = datetime.datetime.strptime(date, '%d/%m/%Y').date()
                # print(start_date)
                item.append(sku)
                item.append(start_date)
                item.append(0)
                purchase_list.append(item)


    # sys.exit()
    # The header: 额外选择BOM和create date 和 Invoice date
    # 0:Order Ref, 1:Company, 2:First Name, 3:Last Name, 4:Created Date, 5:Item Code, 6:Item Qty, 7:Item BOM Load, 8: Invoice Date
    not_invoiced = 0
    path = "cin7 data"
    files = os.listdir(path)
    for file in files:
        f = open(path+"/"+file, encoding='utf-8')
        file = csv.reader(f)
        next(file)
        for line in file:
            if line[8] == None or line[8] == "":
                not_invoiced += 1
                continue
            if len(line) < 2 or line[0] == None or line[0] == '':
                continue
            if line[7] == 'Use':
                continue
            if line[5] == 'SHIPPING' or line[5] == 'OC' or line[5] == 'Installation':
                continue
            
            sku = line[5].strip()
            quantity = line[6]
            date = line[4]
            date = date.split(" ")
            date = date[:3]
            date_str = date[0]+"-"+date[1]+"-"+date[2]
            order_date = datetime.datetime.strptime(date_str, '%d-%b-%Y').date()

            if sku in purchase_sku:
                index = purchase_sku.index(sku)
                start_date = purchase_list[index][1]
                if order_date >= start_date:
                    purchase_list[index][2]+=int(quantity)

    # with open('quantity compare.csv', 'w', encoding='utf-8' ) as csv_file:
    #     csv_write = csv.writer(csv_file)
    #     csv_write.writerow(['SKU', 'Start Date', 'Purchase quantity', 'Sale quantity'])
    #     for i in range(len(purchase_list)):
    #         csv_write.writerow([purchase_list[i][0],purchase_list[i][1],purchase_list[i][2],purchase_list[i][3]])
    
    path = "Leafliving"
    files = os.listdir(path)
    leafliving_order = []
    for file in files:
        f = open(path+"/"+file, encoding='utf-8')
        file = csv.reader(f)
        next(file)

        for line in file:
            leafliving_order.append(line)
            order_date = line[15][:10]
            order_date = datetime.datetime.strptime(order_date, '%Y-%m-%d').date()
            sku = line[20].strip()
            quantity = int(line[16])
            if sku in purchase_sku:
                index = purchase_sku.index(sku)
                start_date = purchase_list[index][1]
                if order_date >= start_date:
                    purchase_list[index][2]+=int(quantity)


    
    index = 0
    with open("预售.csv", 'w', newline='', encoding='utf-8') as f:
        file = csv.writer(f)
        file.writerow(["SKU", "Start Date", "Sales Quantity"])
        for i in range(len(purchase_list)):
            file.writerow([purchase_list[i][0], purchase_list[i][1], purchase_list[i][2]])

    
    print(not_invoiced)