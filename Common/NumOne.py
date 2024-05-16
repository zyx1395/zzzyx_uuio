'''
通过函数调用，实现代码自动化，只需要传参，提高代码复用率---参数化
'''

def login(username,password,driver,By):
   driver.find_element(By.NAME, 'username').send_keys('admin')
   driver.find_element(By.NAME, 'password').send_keys('admin123')
   driver.find_element(By.ID, 'btnSubmit').click()

def open_url(url,driver):    #打开网页函数
    driver.get(url)
    driver.maximize_window()
def search_key(url,driver,username,password,By,s_key):
    open_url(url, driver)
    login(username,password,driver,By)
    driver.find_element(By.XPATH,"//span[text()='蜕变用户']").click()
    driver.find_element(By.XPATH,"//a[text()='蜕变用户']").click()
    driver.switch_to.frame('iframe2')
    driver.find_element(By.XPATH,"//input[@name='phoneNumber']").send_keys(10947435029)
    driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-rounded btn-sm']").click()
    pwd = driver.find_element(By.XPATH,"//td[text()='381a2c6d5703518cea0330bbf14edde8']").text
    return pwd

