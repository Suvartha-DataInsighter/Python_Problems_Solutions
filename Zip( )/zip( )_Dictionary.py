def zip_dictionary(stocks,prices):
    new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
    print(new_dict)
stocks = ['Amazon', 'infosys', 'tcs']
prices = [28910, 32127, 19929]
zip_dictionary(stocks,prices)