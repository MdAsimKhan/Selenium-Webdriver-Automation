import time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


dict = {'payment_type':"",
        'id':"",
        'name':"",
        'course':"",
        'branch':"",
        'adm_yr':"",
        'sem':"",
        'amt':"",
        'remarks':"",
        'birth_yr':"",
        'birth_month':"",
        'birth_date':"",
        'phone':"",
        'emailId':""}


# automation code
def fill_details():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.onlinesbi.sbi/sbicollect/icollecthome.htm")

    # accept TnC
    driver.find_element(by=By.ID, value="proceedcheck_english").click()
    # click proceed
    driver.find_element(by=By.XPATH, value="//*[@id='welcomecollect_english']/div[2]/button").click()
    # select state
    driver.find_element(by=By.XPATH, value="//*[@id='stateID']/div/button").click()
    # input state
    driver.find_element(by=By.XPATH, value="//*[@id='stateID']/div/div/div/input").send_keys("Odisha", Keys.ENTER)
    # select org type
    select = Select(driver.find_element(by=By.XPATH, value="//*[@id='instTypeID']"))
    # input org type
    select.select_by_visible_text("Educational Institutions")
    # click GO
    driver.find_element(by=By.XPATH, value="//*[@id='go']").click()
    # select clg
    driver.find_element(by=By.XPATH, value="//*[@id='select-institute']/div/button").click()
    # input clg
    driver.find_element(by=By.XPATH, value="//*[@id='select-institute']/div/div/div/input").send_keys("INTERNATIONAL INSTITUTE OF INFORMATION TECHNOLOGY", Keys.ENTER)
    # click submit
    driver.find_element(by=By.XPATH, value="//*[@id='institutionform']/div[2]/button[1]").click()
    # select payment type
    driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div/div/div[2]/div/div[2]/div/button").click()
    # input payment type
    driver.find_element(by=By.CSS_SELECTOR, value="#frmFeeParams > div > div > div.panel-collapse.collapse.in > div > div.col-md-9 > div > div.dropdown-menu.open > div > input").send_keys(dict['payment_type'], Keys.ENTER)
    # enter roll no
    driver.find_element(by=By.XPATH, value="//*[@id='outref11']").send_keys(dict['id'])
    # enter name
    driver.find_element(by=By.XPATH, value="//*[@id='outref12']").send_keys(dict['name'])
    # select prog
    driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div[2]/div/div[2]/div/div[4]/div[2]/div/button").click()
    # input prog
    driver.find_element(by=By.CSS_SELECTOR, value="#frmFeeParams > div.panel-group > div > div.panel-collapse.collapse.in > div > div:nth-child(8) > div.col-md-9 > div > div > div > input").send_keys(dict['course'], Keys.ENTER)
    # select branch
    driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div[2]/div/div[2]/div/div[5]/div[2]/div/button").click()
    # input branch
    driver.find_element(by=By.CSS_SELECTOR, value="#frmFeeParams > div.panel-group > div > div.panel-collapse.collapse.in > div > div:nth-child(11) > div.col-md-9 > div > div > div > input").send_keys(dict['branch'], Keys.ENTER)
    # enter year of admission
    driver.find_element(by=By.XPATH, value="//*[@id='outref15']").send_keys(dict['adm_yr'], Keys.ENTER)
    # select sem
    driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div[2]/div/div[2]/div/div[7]/div[2]/div/button").click()
    # input sem
    driver.find_element(by=By.CSS_SELECTOR, value="#frmFeeParams > div.panel-group > div > div.panel-collapse.collapse.in > div > div:nth-child(17) > div.col-md-9 > div > div > div > input").send_keys(dict['sem'], Keys.ENTER)
    # enter fee amt
    driver.find_element(by=By.XPATH, value="//*[@id='outref17']").send_keys(dict['amt'])
    # enter remarks
    driver.find_element(by=By.ID, value="transactionRemarks").send_keys(dict['remarks'])
    # enter name
    driver.find_element(by=By.ID, value="cusName").send_keys(dict['name'])
    # click calender
    driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div[2]/div/div[3]/div[2]/div/div[2]/img").click()
    # select year
    year = Select(driver.find_element(by=By.XPATH, value="//*[@id='ui-datepicker-div']/div/div/select[2]"))
    year.select_by_value(dict['birth_yr'])
    # select month
    month = Select(driver.find_element(by=By.XPATH, value="//*[@id='ui-datepicker-div']/div/div/select[1]"))
    month.select_by_value(dict['birth_month'])
    # select date
    driver.find_element(by=By.XPATH, value="//a[text()=" + dict['birth_date'] + "]").click()
    # enter mobile no
    driver.find_element(by=By.ID, value="mobileNo").send_keys(dict['phone'])
    # enter email
    driver.find_element(by=By.ID, value="emailId").send_keys(dict['emailId'])
    # wait for user to input captcha
    time.sleep(15)
    # click submit
    submit = None
    try:
        submit = driver.find_element(by=By.XPATH, value="//*[@id='frmFeeParams']/div[3]/button[1]")
        submit.click()
    except NoSuchElementException:
        pass

    while(True):
        pass


# read data from file
# count no of lines
with open('text.txt', 'r') as fp:
    sz = len(fp.readlines())

l=[]
# save values from file to empty list l
lines = []
with open('text.txt', 'r') as fp:
    lines = (line.rstrip() for line in fp) 
    lines = list(line for line in lines if line)
i=0
# set key values in dict
for k in dict:
    dict[k] = lines[i]
    i += 1

# -1 from birth month
dict['birth_month'] = str(int(dict['birth_month']) - 1)
# remove special chars from remarks
dict['remarks'] = re.sub('[^A-Za-z0-9 ,.]+',' ', dict['remarks'])
# capitalise branch
dict['branch'] = dict['branch'].upper()

fill_details()