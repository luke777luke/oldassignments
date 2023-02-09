#Lukasz Grzybek

shares = eval(input('Number of shares purchased/sold: '))
buying_price = eval(input('Purchase price of one share: '))
selling_price = eval(input('Selling price of one share: '))

buying_service_fee = (shares * buying_price) * 0.025
selling_service_fee = (shares * selling_price) * 0.025
total_service_fee = buying_service_fee + selling_service_fee

amount_invested = shares * buying_price
amount_sold = shares * selling_price

investment_results = (amount_sold - amount_invested) - total_service_fee

print('Amount invested: ' + str(amount_invested))
print('Total service fee: ' + str(total_service_fee))
print('Amount of investment gains or losses: ' + str(investment_results))

#Case 1 Investing 10250.00 by purchaseg 1000 shares at 10.25 a share, and selling at 35.90 a share, generates a total gain of 24496.25 and total service fees of 1153.75. 

#Case 2 Investing 56780.00 by purchaseg 1000 shares at 56.78 a share, and selling at 23.80 a share, generates a total loss of 34994.50 and total service fees of 2014.50. 