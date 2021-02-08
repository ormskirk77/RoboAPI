from pynq import Clocks


class Driver:

    _duty_cycle = 0
    _pwm_on_time = 0.0
    _pwm_off_time = 0.0

    def set_duty_cycle(self, new_duty_cycle):
        if 0 < new_duty_cycle and new_duty_cycle > 100:
            print("Duty cycle must be between 0 and 100")
        else:
            self._duty_cycle = new_duty_cycle
            self._pwm_on_time, self._pwm_off_time = self._calc_duty_cycle_times(self._duty_cycle)

    def _calc_duty_cycle_times(self, duty_cycle):
        """
        calculates the times required to instigate a duty cycle in a for loop using delays. Uses the fclk0_mhz from
        pynq to calculate these times. Use the returned values in a delay for loop.
        :return: tuple time_on, time 0ff. Both floats
        """
        clock = Clocks.fclk0_mhz
        time_on = duty_cycle / (clock * 100)
        time_off = (1 / clock) - time_on
        return time_on, time_off




