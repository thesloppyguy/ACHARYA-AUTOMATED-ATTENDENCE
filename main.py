from re import sub
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from timediff import time_difference,retun_day,zero_time_clock,format_time

driver = webdriver.Chrome()
driver.get("https://alive.university/")
# LOGIN INTO THE PAGE


ID = driver.find_element_by_name("user_email")
ID.send_keys("AIT19BECS080")
PASS = driver.find_element_by_name("user_password")
PASS.send_keys("Sahil@123")
driver.find_element_by_class_name("MuiButton-label").click()

#FIND DAY
day=retun_day()

# PERIOD TIME
sleep(10)
classButtons = driver.find_elements_by_xpath(
    "//div[@class='MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded']")
noofclasses = len(classButtons)
classtime = []
classtime_end =[]

for i in range(noofclasses):
    #START TIME
    classt = classButtons[i].find_element_by_xpath(
        ".//p[@class='MuiTypography-root mb-1 MuiTypography-body2 MuiTypography-colorTextSecondary']").get_attribute(
        "innerHTML")
    kk = classt[14:22]
    if kk[len(kk) - 1] == "-":
        kk = sub("-", "", kk)

    bigtime = format_time(kk)
    bigtime = bigtime.time()
    classtime.append(bigtime)
    #END TIME
    mm=classt[22:len(classt)]
    if mm[0]== "-":
        mm=sub("-","",mm)

    endtime=format_time(mm)
    endtime=endtime.time()
    classtime_end.append(endtime)



# PERIOD SEQUENCE

for i in range(noofclasses):
   for j in range(0, noofclasses - i - 1):
       if classtime[j] > classtime[j + 1]:
           classtime[j], classtime[j + 1] = classtime[j + 1], classtime[j]
           classtime_end[j], classtime_end[j + 1] = classtime_end[j + 1], classtime_end[j]
           classButtons[j], classButtons[j + 1] = classButtons[j + 1], classButtons[j]

def class_accese(pasta):
    try:
        pasta.click()
    except NoSuchElementException:
        return False
    return True



# PERIOD SELECT
running = True
zero_time = zero_time_clock()
condition = False


for i in range(noofclasses):

    #SLEEPTIME CALCULATION
    difference = time_difference(classtime_end[i])
    #SKIPS CLASS IF ALREADY DONE ELSE ASSIGNS SLEEPTIME
    if difference <= zero_time:
        continue
    else:
        sleeptime=difference.total_seconds()+300

    #FIND CLASS NAME FOR LAB SLEEPTIME
    classname = classButtons[i].find_element_by_xpath(
       ".//h2[@class='MuiTypography-root MuiTypography-h5']").get_attribute("innerHTML")

    #CHECKS FOR CORRECT LAB DEPENDING ON THE DAY
    if day=="Thursday" and classname =="Subject : 18DSL" or day=="Tuesday" and classname =="Subject : 18ADEL":
        continue

    #JOIN CLASS BUTTON
    bingo = classButtons[i].find_element_by_xpath(
       ".//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-textSizeLarge MuiButton-sizeLarge']").find_element_by_xpath(
       ".//span[@class='MuiButton-label']")

    #JOINING CLASS
    while running:
        condition=class_accese(bingo)

        if condition==True:
            print("in class",classname)
            sleep(20)
            #CLICK ON AUDIO ONLY
            #driver.find_elements_by_xpath("//span[@class='button--Z2dosza jumbo--Z12Rgj4 default--Z19H5du circle--Z2c8umk']")[1].click()
            #GO TO SLEEP
            print(sleeptime)
            sleep(sleeptime)
            #CLICK ON HOME
            homebutton = driver.find_element_by_class_name("jss10").find_elements_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-colorInherit MuiButton-textSizeLarge MuiButton-sizeLarge']")
            homebutton[0].find_element_by_class_name("MuiButton-label").click()
            #EXIT OUT OF WHILE TO GO TO NEXT CLASS
            break
        #RETRY CLASS
        else:
            print("sleeping 5min")
            sleep(300)
            if time_difference(classtime_end[i])<zero_time:
                break

driver.close()
#END