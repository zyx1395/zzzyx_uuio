'''
通过函数调用，实现代码自动化，只需要传参，提高代码复用率---参数化
'''

def login(username,password,driver):
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('btnSubmit').click()
def open_url(url,driver):    #打开网页函数
    driver.get(url)
    driver.maximize_window()
def search_key(url,driver,username,password,s_key):
    open_url(url, driver)
    login(username,password,driver)
    driver.find_element_by_xpath("//span[text()='蜕变用户']").click()
    driver.find_element_by_xpath("//a[text()='蜕变用户']").click()
    driver.switch_to.frame('iframe2')
    driver.find_element_by_xpath("//input[@name='phoneNumber']").send_keys(10947435029)
    driver.find_element_by_xpath("//a[@class='btn btn-primary btn-rounded btn-sm']").click()
    pwd = driver.find_element_by_xpath("//td[text()='381a2c6d5703518cea0330bbf14edde8']").text
    return pwd

