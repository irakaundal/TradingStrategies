from res import id as id, values as values, constants as constants
import handler.database as db


def __is_bear(open, close):
    return close < open


# check if the bear candle open between and close lower
# values of 1 is more recent than 2
def __is_lower(open_1, close_1, open_2, close_2, low_2):
    return open_2 > open_1 > low_2 and close_1 < close_2


def __body(open, close):
    return abs(open-close)


def __small_lower_wick(price):
    return __body(price[id.close], price[id.low]) / __body(price[id.open], price[id.close]) \
           < constants.three_black_crow[id.wick_percentage]


def __downtrend(price_action, window_size):
    # will replace this by library function
    total = 0
    for i, p in enumerate(price_action):
        total += p[id.close]
        if i % window_size == 0:
            sma = total/window_size
            total -= price_action[i-window_size][id.close]
            if p[id.close] > sma:
                return False
    return True


# main strategy call
def three_black_crows(key, price_action, time_frame):
    window_size = constants.three_black_crow[id.window_size]
    # crows=check if the last 3 candles are crows
    crows = __is_bear(price_action[-1][id.open], price_action[-1][id.close]) \
            and __is_bear(price_action[-2][id.open], price_action[-2][id.close]) \
            and __is_bear(price_action[-3][id.open], price_action[-3][id.close]) \
            and __is_lower(price_action[-1][id.open], price_action[-1][id.close],
                           price_action[-2][id.open], price_action[-2][id.close], price_action[-2][id.low]) \
            and __is_lower(price_action[-2][id.open], price_action[-2][id.close],
                           price_action[-3][id.open], price_action[-3][id.close], price_action[-3][id.low])
    # check lower wick
    lower_wick = __small_lower_wick(price_action[-1]) \
                 and __small_lower_wick(price_action[-2]) \
                 and __small_lower_wick(price_action[-3])

    # find trend for candles from -17 to -3
    trend = __downtrend(price_action[-2*window_size - 3:-3], window_size)

    # check strategy
    if trend and crows and lower_wick:
        db.insert_strategy(key, time_frame, values.three_black_crow, price_action[-1][id.time])


