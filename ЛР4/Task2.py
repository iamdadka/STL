import time

class TrafficLight:

    __color = "red"

    def __int__(self):
        self.__color = 'red'

    def running(self):
        while True:
            if self.__color == 'red':
                print("Red light")
                time.sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print("Yellow light")
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print("Green light")
                time.sleep(5)
                self.__color = "red"
            else:
                print("Invalid traffic light color!")
                break

t1 = TrafficLight()
t1.running()
