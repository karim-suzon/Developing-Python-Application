#2.Create class Clock and it's subclass AlarmClock. Test clocks in main.
#There has to be ticking and alarming methods..

import time

class Clock:

    def __init__(self, hours, minutes, seconds):
        # Just store total seconds.
        self.total_secs = self.hms_to_seconds(hours, minutes, seconds)

    def hms_to_seconds(self, hours, minutes, seconds):
        # Simple converter.
        return hours * 3600 + minutes * 60 + seconds

    # Properties to retrieve user-facing values when needed.

    @property
    def hours(self):
        return self.total_secs // 3600

    @property
    def minutes(self):
        return (self.total_secs - (3600 * self.hours)) // 60

    @property
    def seconds(self):
        return self.total_secs - 3600 * self.hours - 60 * self.minutes

    def tick(self):
        # Make tick do less, so you can re-use it.
        print(f'{self.hours:>02}:{self.minutes:>02}:{self.seconds:>02}')
        self.total_secs += 1
        time.sleep(1)

    def run(self):
        # A basic clock just ticks forever.
        while True:
            self.tick()

class AlarmClock(Clock):

    def __init__(self, hours, minutes, seconds, alarm_hr, alarm_min, alarm_sec):
        super().__init__(hours, minutes, seconds)
        self.alarm_secs = self.hms_to_seconds(alarm_hr, alarm_min, alarm_sec)

    def run(self):
        # An alarm clock ticks and alarms.
        while True:
            self.tick()
            if self.total_secs >= self.alarm_secs:
                print("ALARM ALARM ALARM ALARM ALARM!!!!")
                break

AlarmClock(1, 15, 0, 1, 15, 5).run()