class Commands(object):
    """
    commands only
    """

    def __init__(self):
        super().__init__()
        self.ESC = '\x1B'

    def reset(self):
        """
        Commandcode:<ESC>a
        Hexcode: 1B61
        Response: none
        Description: This command reset the MSR605 to initial state.
        """
        return self.ESC + '\x61'

    def read_iso(self):
        """
        Commandcode:<ESC>r
        Hexcode: 1B72
        Response:[DataBlock]<ESC>[StatusByte]
        Description:This command request MSR605 to read a card swiped and respond with the data read
        Note: ISO7811
        """
        return self.ESC + '\x72'

    def write_iso(self):
        """
        Commandcode: <ESC>w[DataBlock]
        Hexcode:1B77[DataBlock]
        Response: <ESC>[StatusByte]
        Description:This command request MSR605 to write the Data Block into the card swiped.
        Note: ISO7811
        """
        return self.ESC + '\x77'

    def communication_test(self):
        """
        Commandcode:<ESC>e
        Hexcode:1B65
        Response:<ESC>y[1B][79]
        Description:This command is used to verify that the communication link between computer and MSR605 is up and good.
        """
        return self.ESC + '\x65'

    def all_leds_off(self):
        """
        Command code: < ESC > < 81 >
        Hexcode: 1B81
        Response: none
        Description: This command is used to turn off all the LEDs.
        """
        return self.ESC + '\x81'

    def all_leds_on(self):
        """
        Command code: < ESC > < 82 >
        Hexcode: 1B82
        Response: none
        Description:This command is used to turn on all the LEDs.
        """
        return self.ESC + '\x82'

    def green_led_on(self):
        """
        Commandcode: < ESC > < 83 >
        Hexcode: 1B83
        Response: none
        Description:This command is used to turn on the Green LED.
        """
        return self.ESC + '\x83'

    def yellow_led_on(self):
        """
        Commandcode: < ESC > < 84 >
        Hexcode: 1B84
        Response: none
        Description:This command is used to turn on the Yellow LED.
        """
        return self.ESC + '\x84'

    def red_led_on(self):
        """
        Commandcode: < ESC > < 85 >
        Hexcode: 1B85
        Response: none
        Description:This command is used to turn on the Red LED.
        """
        return self.ESC + '\x85'

    def sensor_test(self):
        """
        Command code:<ESC><86>
        Hexcode:1B86
        Response:<ESC>0(1B30) if test ok
        Description:This command is used to verify that the card sensing circuit of MSR605 is working properly. MSR605 will
        not response until a card is sensed or receive a RESET command
        """
        return self.ESC+'\x86'

    def ram_test(self):
        """
        Command code:<ESC><87>
        Hexcode:1B87
        Response:<ESC>0(1B30) ram test ok;<ESC>A(1B41) ram test fail
        Description:This command is used to request MSR605 to perform a test on its on board RAM
        """
        return self.ESC+'\x87'

    def set_leading_zero(self):
        """
        Command code:<ESC>z[leading zero of track 1 & 3][leading zero of track 2]
        Hexcode:1B7A[00~ff][00~ff]
        Response:<ESC>0(1B30) set ok <ESC>A (1B41) set fail
        Description: This command is used to set how many leading zeros will be written before the card data starts,
        and the space should calculated as [leading zero]X25.4/BPI(75or210)=mm
        Default setting of leading zero:[3D][16] TK1 & TK3: [3D] means leading zero = 61 TK2:[16] means leading zero=22
        TODO:Test
        """
        return self.ESC+'\x7A'

