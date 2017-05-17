def start():

    # Database of currency values and standard abbreviations
    crypto_currency_dictionary = {
        'bitcoin' : ['BTC', 1732.4800],
        'litecoin' : ['LTC', 22.9100],
        'ethereum' : ['ETH', 87.5700],
        'burstcoin' : ['BURST',0.0079],
        'peercoin' : ['PPC', 1.5574]
        }

    dollars = float(raw_input('\nHow many dollars do you want to exchange? $'))

    print ("\n:: Bitcoin, Burstcoin, Ethereum, Litecoin, Peercoin ::\n")
    crypto_currency = raw_input('Enter a currency listed above: ').lower()
    
    try:
        x_data = crypto_currency_dictionary[crypto_currency]

        # Print dollars to nearest hundredths and crypto currency to nearest ten-thousandths
        print '\n$' + str("%.2f" % dollars) + ' will convert to ' + x_data[0] + ' ' + str("%.4f" % (dollars/x_data[1]))
        more()
    except:
        
        print '\nI cannot find that type of crypto currency.'
        more()


def more():
    
    search_again = raw_input('\nWould you like to try another search? ').lower()
    if  search_again == 'no':
        return
    if search_again == 'yes':
        start()
    else:
        print "Please enter Yes or No."
        more()


start()
