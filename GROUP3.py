from machine import Pin，PWM
import time
import dht
sensor = dht.DHT11(Pin(0))
rLED = PWM(Pin(12))  # 控制紅燈
gLED = PWM(Pin(13))  # 控制綠燈
bLED = PWM(Pin(15))  # 控制藍燈
sensor.measure()
while True:
    PP=sensor.humidity()
    if PP <= 45:
        gLED.duty(0)
        bLED.duty(0)
        rLED.duty(1000)    #濕度太低顯示紅燈
        temp_humi="{0}% 濕度太低".format(PP)
        print(temp_humi)
    elif PP>45 and PP<=55:
        gLED.duty(1000)
        bLED.duty()
        rLED.duty(0)     #濕度正常顯示綠燈
        temp_humi="{0}% 濕度正常".format(PP)
        print(temp_humi)   
    else: #55 up
        gLED.duty(0)
        bLED.duty(1000)
        rLED.duty(0)     #濕度太高顯示藍燈
        temp_humi="{0}% 濕度太高".format(PP)
        print(temp_humi)
    time.sleep(10)         #每半小時更新一次燈號
