def stock_picker(li):
    '''Picks 2 days with the highest stock price difference.'''

    max_dif = 0

    for i in range (len(li)):
        for j in range(i+1, len(li)):
            if (li[i] - li[j]) > max_dif:
                max_dif = li[i] - li[j]
                max_buy = i
                max_sell = j

    print "Stock should've been bought on day %s, and sold on day %s." % (max_buy + 1, max_sell + 1)
    print "Price difference is %s dollars." % max_dif


prob = [2, 4, 100, 20, 1]

stock_picker(prob)
