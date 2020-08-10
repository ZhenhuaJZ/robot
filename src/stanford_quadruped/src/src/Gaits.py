class GaitController:
    def __init__(self, config):
        self.config = config


    def phase_index(self, ticks):
        """Calculates which part of the gait cycle the robot should be in given the time in ticks.

        Parameters
        ----------
        ticks : int
            Number of timesteps since the program started
        gaitparams : GaitParams
            GaitParams object

        Returns
        -------
        Int
            The index of the gait phase that the robot should be in.

        The phase index calculates which phase the current robot should be in
            base on the current tick,
        T
        """
        print("phase_length: ", self.config.phase_length)
        print("num_phases: ", self.config.num_phases)
        phase_time = ticks % self.config.phase_length
        print("Phase_time: ", phase_time)
        phase_sum = 0
        for i in range(self.config.num_phases):
            phase_sum += self.config.phase_ticks[i]
            # If the current tick is within the sum of phase ticks, then its in current phase
            # ie. phase_time 0-10 is first phase, 10-25 is second phase and so on.
            if phase_time < phase_sum:
                return i
        assert False


    def subphase_ticks(self, ticks):
        """Calculates the number of ticks (timesteps) since the start of the current phase.

        Parameters
        ----------
        ticks : Int
            Number of timesteps since the program started
        gaitparams : GaitParams
            GaitParams object

        Returns
        -------
        Int
            Number of ticks since the start of the current phase.
        """
        phase_time = ticks % self.config.phase_length
        phase_sum = 0
        subphase_ticks = 0
        for i in range(self.config.num_phases):
            phase_sum += self.config.phase_ticks[i]
            if phase_time < phase_sum:
                subphase_ticks = phase_time - phase_sum + self.config.phase_ticks[i]
                return subphase_ticks
        assert False


    def contacts(self, ticks):
        """Calculates which feet should be in contact at the given number of ticks

        Parameters
        ----------
        ticks : Int
            Number of timesteps since the program started.
        gaitparams : GaitParams
            GaitParams object

        Returns
        -------
        numpy array (4,)
            Numpy vector with 0 indicating flight and 1 indicating stance.
        """
        return self.config.contact_phases[:, self.phase_index(ticks)]
