total_ext_price = 0

item_file = 'items.txt' 
with open (item_file) as item_file: item_records = item_file.readlines()
clean_item_records = [item_record.strip() for item_record in item_records]
# print(clean_item_records)

for clean_item_records in clean_item_records:
        split_item_record = clean_item_records.split(';')
        item = split_item_record[0]
        quantity = float(split_item_record[1])
        price = float(split_item_record[2])
        ext_price = quantity * price
        print('Item:',item,'|Quantity:',quantity,'|Price:$',price,'|Extended Price:$',ext_price)
        total_ext_price += ext_price

print('Total Bonus given is', total_ext_price)

