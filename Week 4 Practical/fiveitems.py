

price1 = input('Enter the price of the first sweet: ')
price2 = input('Enter the price of the second sweet: ')
price3 = input('Enter the price of the third sweet: ')
price4 = input('Enter the price of the fourth sweet: ')
price5 = input('Enter the price of the fifth sweet: ')
prices_all = (int(price1 [:-1]),int(price2 [:-1]),int(price3 [:-1]),int(price4 [:-1]),int(price5 [:-1]))
total_prices = int(price1 [:-1]) + int(price2 [:-1]) + int(price3 [:-1]) + int(price4 [:-1]) + int(price5 [:-1])
average_price =(int(price1 [:-1]) + int(price2 [:-1]) + int(price3 [:-1]) + int(price4 [:-1]) + int(price5 [:-1]))/5
highest_price = max(prices_all)
lowest_price = min(prices_all)



print ('Total Price: ',total_prices,'\nAverage Price: ',average_price,'\nHighest Price: ',highest_price,'\nLowest Price: ',lowest_price)