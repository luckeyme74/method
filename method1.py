class Time(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

#I understand that converting a function to a method is just rearranging the function to be within the class.
#But I don't understand a lot of this and the last few chapters have been completely indecipherable to me.
#I keep going back and rereading the chapters but it is completely incomprehensible
#I understood much of this class up to a few weeks ago but I'm completely lost.
#I can't even figure out how to call this.

