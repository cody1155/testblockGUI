import time
import piplates.DAQCplate as DAQC

#------INPUTS waiting for values
                               
battery_volt_HIGH = 11
battery_volt_LOW = 0

chamberPT_max = 500
chamberPT_volt_HIGH = 5
chamberPT_volt_LOW = 0

thrustPT_max = 1500
thrustPT_volt_HIGH = 5
thrustPT_volt_LOW = 0

temp_max = 257
temp_volt_HIGH = 1.2
temp_volt_LOW = 0
offset = 0.5

fileName = input("what would you like your file to be named?\n")
fileName = str(fileName)



def adcFormula(data, max_value, volt_HIGH, volt_LOW, divisionFactor):
    volt_range = volt_HIGH - volt_LOW
    data = (max_value/volt_range) * (data-volt_LOW)

    #going to fill once components are chosen

    return data


def main():

    while(1):
        f = open(fileName, "a")

        currentTime = time.strftime("%H:%M:%S")

        battery_raw = DAQC.getADC(1,0)
        battery = adcFormula(battery_raw, 1, battery_volt_HIGH, battery_volt_LOW, 4)
    
        chamberPT_raw = DAQC.getADC(1,1)
        chamberPT = adcFormula(chamberPT_raw, chamberPT_max, chamberPT_volt_HIGH, chamberPT_volt_LOW, 2)
    
        thrustPT_raw = DAQC.getADC(1,2)
        thrustPT = adcFormula(thrustPT_raw, thrustPT_max, thrustPT_volt_HIGH, thrustPT_volt_LOW, 2)
    
        temp_raw = DAQC.getADC(1,3)
        tempC = (temp_raw - offset) * 100
        tempF = (tempC * 1.8) + 32
        #temp = adcFormula(temp_raw, temp_max, temp_volt_HIGH, temp_volt_LOW, 2)

        print('{}, {}, {}, {}, {}'.format(currentTime, battery, chamberPT, thrustPT, temp_raw))
        f.write('{}, {}, {}, {}, {}\n'.format(currentTime, battery, chamberPT, thrustPT, tempF))

        time.sleep(.1)
        f.close()
        

if __name__ == '__main__':
    main()


