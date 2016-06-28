# The Irish lottery draw takes place twice weekly
# on a Wednesday and a Saturday at 8pm.
# Write a function that calculates and returns the
# next valid draw date based on the
# current date and time and also on an optional supplied date.

from datetime import datetime, time, timedelta
RESULT_TIME = time(20, 00, 00)
current_time = datetime.now()


def next_result_datetime(user_input=current_time):
    """ A function that takes a user input (date)
    and returns the next valid lottery draw date.
    If there is no user input then the next draw
    is based on current date
    :param user_input :
    User input date / default is current datetime
    :return time_for_draw : next valid draw date
    """
    # Get the numbered weekday from userInput (1:Monday...7:Sunday)
    user_input_week_num = user_input.isoweekday()
    # if the user_input_weekday is draw day (either Wednesday or
    # saturday) and the user input time is greater than or equal to
    # 8:00PM(lottery draw time) then the valid draw date would be the
    # following wednesday or Saturday which ever occurs first
    if user_input_week_num in (3, 6) and user_input.hour >= 20:
        user_input_week_num += 1
        user_input += timedelta(days=1)
    # Draw days ( Wednesday and Saturday ) are perfectly
    # divisible by 3. Therefore 3 percentile of
    # ((two's compliment of (weekday)) + 1) gives the
    # number of days to next draw day (except for sunday).
    # in case of sunday we need to add an extra day.
    # floor division of user_input_week_num by 7 will give 1
    # for sunday and 0 for others.
    # ---------------------------------------------------------
    #    weekday         MON  Tue  *WED*  THU  FRI *SAT* SUN
    #    week_no          1    2     3     4    5    6   7
    # ---------------------------------------------------------
    # (~(week_no)+1)%3    2    1     0     2    1    0   2
    #    week_no//7       0    0     0     0    0    0   1
    # ---------------------------------------------------------
    #    delta            2    1     0     2    1    0   3
    #    draw_day = delta day/s from weekday
    draw_day = (((~user_input_week_num) + 1) % 3) + (user_input_week_num//7)
    time_for_draw = datetime.combine(user_input + timedelta(days=draw_day),
                                     RESULT_TIME)
    return time_for_draw

if __name__ == '__main__':
    print "Input 2016-6-26 19:00 (Su).   Next draw: {}".format( next_result_datetime(datetime(2016, 6, 26, 19, 0, 0)))
    print "Input 2016-6-27 19:00 (M).    Next draw: {}".format( next_result_datetime(datetime(2016, 6, 27, 19, 0, 0)))
    print "Input 2016-6-28 19:00 (T).    Next draw: {}".format( next_result_datetime(datetime(2016, 6, 28, 19, 0, 0)))
    print "Input 2016-6-29 20:00 (*W*).  Next draw: {}".format( next_result_datetime(datetime(2016, 6, 29, 20, 0, 0)))
    print "Input 2016-6-30 19:00 (Th).   Next draw: {}".format( next_result_datetime(datetime(2016, 6, 30, 19, 0, 0)))
    print "Input 2016-7-01 20:00 (F).    Next draw: {}".format( next_result_datetime(datetime(2016, 7, 01, 20, 0, 0)))
    print "Input 2016-7-02 19:00 (*Sa*). Next draw: {}".format( next_result_datetime(datetime(2016, 7, 02, 19, 0, 0)))
    print "Input 2016-7-02 20:00 (*Sa*). Next draw: {}".format( next_result_datetime(datetime(2016, 7, 02, 20, 0, 0)))
    print "Input NOne                    Next draw: {}".format(next_result_datetime())
