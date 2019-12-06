from .msrexception import MSRException
import serial

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

    def check_leading_zero(self):
        """
        Command code:<ESC>l
        Hexcode:1B6C
        Response:1B[00~ff][00~ff]
        Description:This command is used to ask MSR605 the present setting number of leading zeros.
        """
        return self.ESC+'\x6C'

    def erase_card(self):
        """
        TODO:INCOMPLETE
        Commandcode:<ESC>c[SelectByte]
        Hexcode:1B63[SelectByte]
        Response:<ESC>0[1B][30] command Select Byte ok
                 <ESC>A[1B][41] command Select Byte fail
        Description:This command is used to erase the card data when card swipe.
                    *[SelectByte]format:
                    00000000:Track 1 only
                    00000010:Track 2 only
                    00000100:Track 3 only
                    00000011:Track 1 & 2
                    00000101:Track 1 & 3
                    00000110:Track 2 & 3
                    00000111:Track 1, 2 & 3
        """
        return self.ESC+'\x63'

    def select_bpi(self):
        """
        TODO:INCOMPLETE
        Command code:<ESC>b [Density]
        Hexcode:track2：1B62[D2or4B]//[D2]:210bpi,[4B]:75bpi
                track1：1B62[A1orA0]//[A1]:210bpi,[A0]:75bpi
                track3：1B62[C1orC0]//[C1]:210bpi,[C0]:75bpi
        Response:<ESC>0[1B][30] select ok <ESC>A[1B][41] select fail
        Description:This command is used to select the density
        """
        return self.ESC+'\x62'

    def read_raw_data(self):
        """
        Command code:<ESC>m
        Hexcode:1B6D
        Response:[RawDataBlock]<ESC>[StatusByte]
        Description:This command requests MSR605 to read a card swipe but send with out ASCII de code.
                    Referto [RawDataBlock] & [RawData] format.
        """
        return self.ESC+'\x6D'

    def write_raw_data(self):
        """
        TODO: Incomplete
        Command code:<ESC>n [RawDataBlock]
        Hexcode:1B6E [RawDataBlock]
        Response:<ESC> [StatusByte]
        Description:This command requests MSR605 to write raw Data Block into the card swiped.
                    Referto [RawDataBlock] & [RawData] format.
        """
        return self.ESC+'\x6E'

    def get_device_model(self):
        """
        Command code:<ESC>t
        Hexcode:1B74
        Response:<ESC>[Model]S
        Description: This command is used to get the model of MSR605
        """
        return self.ESC+'\x74'

    def get_firmware_version(self):
        """
        Command code:<ESC>v
        Hexcode:<ESC>76
        Response:<ESC>[version]
        Description:This command can get the firmware version of MSR605.
        """
        return self.ESC+'\x76'

    def set_bpc(self):
        """
        Command code:<ESC>o [tk1bit][tk2bit][tk3bit]
        Hexcode:<ESC>6F[05-08][05-08][05-08]
        Response:<ESC>30[tk1bit][tk2bit][tk3bit]
        Description:This command is used to set the bit per character of every track.
        """
        return self.ESC+'\x6F'

    def set_hi_co(self):
        """
        Command code:<ESC>x
        Hexcode:1B78
        Response:<ESC>0
        Description:This command is used to set MSR605 status to write Hi-Co card.
        """
        return self.ESC+'\x78'

    def set_low_co(self):
        """
        Command code:<ESC>y
        Hexcode:1B79
        Response:<ESC>0
        Description:This command is used to set MSR605 status to write Low-Co card.
        """
        return self.ESC+'\x79'

    def get_hi_co_or_low_costatus(self):
        """
        Command code:<ESC>d
        Hexcode:1B64
        Response:<ESC>H-------to write Hi-Co:
                 <ESC>L-------to write Low-Co
        Description:This command is to get MSR605 write status.
        """
        return self.ESC+'\x64'


class MSR(serial.Serial):

    def __init__(self,dev ,test=True,timeout=10):
        """
        Por defecto se le da una cohecion baja ya que son tarjetas para hoteles no deben de tener larga duracion de grabado

        :param dev:
        :param test:
        :param timeout:
        """
        super(MSR, self).__init__(dev, 9600, 8, serial.PARITY_NONE, timeout=timeout)
        self.comando = Commands()
        self.excep = MSRException
        self.estado = ""
        self.tracks = {
            '1': self.comando.ESC + '\x01',
            '2': self.comando.ESC + '\x02',
            '3': self.comando.ESC + '\x03',
            '12': b'00000011',
            '13': b'00000101',
            '23': b'00000110',
            '123': b'00000111',
        }
        self._send_command(self.comando.reset())
        self._send_command(self.comando.set_low_co())
        if test:
            self._send_command(self.comando.communication_test())

    def leer(self):
        """
        Lee la tarjeta 1 track a la ves y regresa el valor de cada uno de los espacios por separado en caso
        de que el dispositivo envie un error regresa un mensaje
        :return:
        """

        self._send_command(self.comando.read_iso())
        track1 = self._read_until(self.tracks.get('1'))[:-2]
        track2 = self._read_until(self.tracks.get('2'))[:-2]
        track3 = self._read_until('\x1C')[:-1]
        _, status = self.read(2)
        if status == '\x31':
            return "error de lectura"

        return track1, track2, track3

    def escribir_tracks(self, t1="", t2="", t3=""):
        """
        Metodo para escribir en nuestra tarjeta magnetica si se requiere dejar un track vacio poner un
        string en blanco o doble comilla
        ademas nada mas acepta letras en mayuscula si introduces letras en minuscula apareceran espacios en blanco
        :param t1:
        :param t2:
        :param t3:
        :return True: Cuando el sistema escribe los datos correctamente en la tarjeta
        :return False: Cuando el sistema no puede escribir los datos correctamente en la tarjeta
        """
        self._send_command(self.comando.set_hi_co())
        data= "\x1B\x77\x1B\x73\x1B\x01" + t1 + "\x1B\x02" + t2 + "\x1B\x03" + t3 + '\x3F\x1C'
        self._send_command(data)
        _,_,_,_,_,_,_,self.estado = self.read(8)
        if self.estado == '\x30':
            return True
        else:
            return False


    def borrar_tracks(self,tracks ):
        """
        Metodo que recive un string con el valor del track que quieres borrar a corde a la siguiente informacion
            track1: 1
            track2: 2
            track3: 3
            track1 y 2: 12
            track1 y 3: 13
            track2 y 3: 13
            track1,2 y 3: 123
        """
        self._send_command(self.comando.set_hi_co())
        self._send_command(self.comando.erase_card(),self.tracks.get(tracks))

    def _send_command(self, command, *args):
        """
        Envia los comandos al dispotivo a partir del diccionario comandos

        :param command:
        :param args:
        :return:
        """
        self.flushInput()
        self.flushOutput()
        self.write(command + ''.join(args))
        self.flush()

    def _read_until(self, end):
        """
        Obtiene los datos del dispositivo utilizando los comandos seleccionados y retorna
        :param end:
        :return:
        """
        data = ''
        while True:
            data += self.read(1)
            if data.endswith(end):
                return data
