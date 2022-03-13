from machine import Pin, PWM
from utime import sleep
#Pinout BTS7960 r_is,l_is not connected, ground and vcc to pico 3.3v
r_en_pin = 4
l_en_pin = 5
r_pwm_pin = 2
l_pwm_pin = 3
global ausgeschaltet
ausgeschaltet = 0

R_EN = Pin(r_en_pin, Pin.OUT)
L_EN = Pin(l_en_pin, Pin.OUT)
pwm1 = machine.PWM(Pin(r_pwm_pin, Pin.OUT)) #R_PWM
pwm2 = machine.PWM(Pin(l_pwm_pin, Pin.OUT)) #L_PWM
#ledPWM = machine.PWM(Pin(25, Pin.OUT))    #Pi Pico 25 ItsyBitsy 11 fuer LED

duty = 0
pwm1.freq(50)
pwm1.duty_u16(duty)
pwm2.freq(50)
pwm2.duty_u16(duty)

def enablemotor(aktiviert): #1=enable 0=disable
    if aktiviert == 1:
        R_EN.on()
        L_EN.on()
    else:
        R_EN.off()
        L_EN.off()
        
def stoppmotor():
    pwm1.duty_u16(0) 
    pwm2.duty_u16(0)

     
def runmotor(Richtung,HzZahl,DutyZahl):  
    # CW = 0 , CCW = 1 HzZahl=frequency DutyZahl=Duty between 1 and 65025
    stoppmotor()
    enablemotor(1)   
    if Richtung == 0:
        # CW R_PWM=HIGH/ L_PM=LOW
        pwm2.duty_u16(ausgeschaltet)
        pwm2.deinit()
        pwm1.freq(HzZahl)
        pwm1.duty_u16(DutyZahl)  
       
    elif Richtung == 1:
        # CW R_PWM=LOW/ L_PM=HIGH
        pwm1.duty_u16(ausgeschaltet)
        pwm1.deinit()
        pwm2.freq(HzZahl)
        pwm2.duty_u16(DutyZahl)  
           
    else:
        stoppmotor()
        print("ELSE")

#MainLoop------------Test -----------------------------------------------------    
ausgeschaltet = 0
while True:  
    runmotor(0,1000,5000)  # CW = 0 , CCW = 1 , HzZahl,DutyZahl bis 65025
    sleep(3)
    stoppmotor()
    sleep(3)
    runmotor(1,1000,10000)  # CW = 0 , CCW = 1 , HzZahl,DutyZahl
    sleep(3)
    stoppmotor()
    sleep(3)
    runmotor(0,1000,15000)  # CW = 0 , CCW = 1 , HzZahl,DutyZahl bis 65025
    sleep(3)
    stoppmotor()
    sleep(3)
    runmotor(0,1000,30000)  # CW = 0 , CCW = 1 , HzZahl,DutyZahl
    sleep(3)
    stoppmotor()
    sleep(3)


