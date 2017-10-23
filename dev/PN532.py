import serial
import time


class PN532(object):

    wake_byte_array = \
        b'\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x03\xFD\xD4\x14\x01\x17\x00'

    wake_return_array = \
        b'\x00\x00\xff\x00\xff\x00\x00\x00\xff\x02\xfe\xd5\x15\x16\x00'

    ser = serial.Serial()
    tmp_byte_array = b''
    is_wait = True

    def connect_serial(self):
        self.ser = serial.Serial('/dev/tty.usbserial', 115200)
        print(str(self.ser.is_open))
        self.wake()

    # wake
    def wake(self):
        self.ser.write(data=self.wake_byte_array)
        while self.is_wait:
            self.tmp_byte_array = self.ser.read(len(self.wake_return_array))
            if self.tmp_byte_array == self.wake_return_array:
                self.is_wait = False
            else:
                self.start()
                return
        print("pn532 wake")
        self.is_wait = True
        self.tmp_byte_array = b''
        self.find_card()

    # find card
    def find_card(self):
        find_card_byte_array = b'\x00\x00\xFF\x04\xFC\xD4\x4A\x01\x00\xE1\x00'
        self.ser.write(data=find_card_byte_array)

        while self.is_wait:
            print("start")
            aaa = self.ser.read(20)
            print(aaa)
            print("stop")





        self.start()



        # while True:
        #     # print("readten:"+str(self.ser.read(10)))
        # self.start()

    def start(self):
        if self.ser:
            if self.ser.isOpen():
                self.ser.close()
                time.sleep(2)
        self.ser = None
        self.connect_serial()



    pass
















a = PN532()
a.start()
