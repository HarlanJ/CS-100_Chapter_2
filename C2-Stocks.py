stock = 2000		#number of stocks bought
price_o = 40.00		#original price of the stock
price_e = 42.75		#end price of the stock

price_b = stock * price_o		#total price of the stocks when bought
price_s = stock * price_e		#total price of the stocks when sold

commission_b = price_b * 0.03		#the commission when the stock was bought
commission_s = price_s * 0.03		#the commission when the stock was sold

profit = price_s - (commission_b + commission_s + price_b)		#total profit of the stocks sold 

#Prints the output of the above
print('Ammount stocks bought for: $' , format(price_b, '.2f') , '\nCommission paid when bought: $' , \
format(commission_b, '.2f') , '\nAmmount stocks sold for: $' , format(price_s, '.2f') , \
'\nCommission paid when sold: $' , format(commission_s, '.2f') , '\nReal profit: $' , \
format(profit, '.2f') , sep='')