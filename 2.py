import numpy as np

arrayNum=np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
def temperatureSwitch(num):
    result=0.0
    if num==1:
        average=np.mean(arrayNum)
        result=average
    elif num==2:
        highest= np.max(arrayNum)
        result=highest
    elif num==3:
        lowewst=np.min(arrayNum)
        result=lowewst
    return result

def temperatureConvertToFab():
    result=arrayNum*9/5+32
    print(result)

def indetifyTemperature():
    result=np.where(arrayNum>20)[0]
    print(result)

    
    

if __name__=="__main__":
    # Determine and display the highest and lowest recorded temperatures.
    num=int(input("Please input a int num: 1:average,2:highest,3:lowest : "))
    ans= temperatureSwitch(num)
    if(ans==0.0):
        print("You inputed a wrong number, please choose one number between 1,2,3")
    else:
        print("\n Final result:", ans)

    #Convert all temperatures to Fahrenheit and print the converted values.
    temperatureConvertToFab()
    #Identify and print the indices of days where the temperature exceeded 20°C.
    indetifyTemperature()
