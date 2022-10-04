import CustomerClass as c
import CarClass as s
import ServiceQuoteClass as q 

car = s.car('Toyota','Tacoma',2019)
cust = c.customer('Eric Gilmore','123 Baylor', '4698734567')
serv = q.ServiceQuote(123,234)

print('*** Customer Information ***')
print('Name: ', cust.get_name())
print('Address: ', cust.get_address())
print('Phone: ', cust.get_phone())
print()
print('*** Vehicle Information ***')
print('Make: ',car.get_make())
print('Model: ',car.get_model())
print('Year: ',car.get_year())
print()
print('*** Service Quote ***')
print('Parts: ', '$' + str(serv.get_pcharge()))
print('Labor: ', '$' + str(serv.get_lcharge()))
print('Total Charges: ', '$' + str(serv.get_total_charges()))