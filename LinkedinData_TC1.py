import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from src.helper.googlesheet import googleSheetOpen
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

scrappedJobLink = []
scrappedJobTitle = []
scrappedNameOfCompany = []
scrappedLocation = []
scrappedActivelyRequiting = []


@pytest.fixture(params=["chrome"], scope="class")
# (params=["chrome", "firefox"], scope="class")
def driver_init(request):
    # selenium code(Python, Java) -> API HTTP Request -> ChromeDrive / GeckoDriver -> Chrome / Firefox
    if request.param == "chrome":
        # web_driver = webdriver.Chrome()
        options = Options()
        options.headless = True
        web_driver = webdriver.Chrome(options=options)
        # web_driver = webdriver.Safari(options=options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    # selenium > 4, Driver path is not needed, they will handle automatically.
    # selenium < 4, Use to set the Driver path.
    yield
    time.sleep(3)
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL_Chrome(BasicTest):
    def test_open_url_and_verify_the_dataScrapping(self):
        # self.driver.maximize_window()
        self.driver.get("https://www.linkedin.com/")
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID, "session_key").send_keys("XXXX.com")
        self.driver.find_element(By.ID, "session_password").send_keys("XXXXX")
        self.driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
        self.driver.find_element(By.XPATH, '//a[@href="https://www.linkedin.com/jobs/?"]').click()

        self.driver.implicitly_wait(15)
        element_org = self.driver.find_element(By.XPATH, '//input[contains(@autocomplete,"organization-title")]')
        element_location = self.driver.find_element(By.XPATH, '//input[contains(@autocomplete,"address-level2")]')
        action = ActionChains(self.driver)
        action.click(on_element=element_org).send_keys("qa engineer").click(on_element=element_location).send_keys(
            "Gurugram, Haryana, India").send_keys(Keys.ENTER).perform()

        self.driver.implicitly_wait(3)
        # JobLink = self.driver.find_elements(By.XPATH, '//a[contains(@id,"ember")]')






        # '//a[contains(@class,"disabled ember-view job-card-container__link job-card-list__title")]')
        # JobTitle = self.driver.find_elements(By.XPATH,
        #                                      '//span[contains(@class,"job-card-container__primary-description")]')
        NameOfCompany = self.driver.find_elements(By.XPATH, '//ul[contains(@class,"job-card-container__metadata-wrapper")]')
                                                  # '//li[4]/div/div/div/div[2]/div[3]/ul/li')
                                                  # '//span[contains(@class,"job-card-container__primary-description")]')

        for i, (job) in enumerate(NameOfCompany):
            print(type(job))
            scrappedJobLink.append(job.text)
        print(scrappedJobLink)

        # Location = self.driver.find_elements(By.XPATH, '//li[contains(@class,"job-card-container__metadata-item")]')
        # ActivelyRequiting = self.driver.find_elements(By.XPATH,
        #                                               '//div[contains(@class,"job-card-container__job-insight-text")]')

        # for i, (Job_Link) in enumerate(JobLink):
        #     scrappedJobLink.append(Job_Link.text)
        # print(scrappedJobLink)


        # =============================

        # for i, (Job_Titles, Names_OfCompany, Locations, Actively_Requiting) in enumerate(
        #         zip(JobTitle, NameOfCompany, Location, ActivelyRequiting)):
        #     scrappedJobTitle.append(Job_Titles.text), scrappedNameOfCompany.append(Names_OfCompany.text), \
        #     scrappedLocation.append(Locations.text()), scrappedActivelyRequiting.append(Actively_Requiting.text())
        #
        # mappedData = zip(scrappedJobTitle, scrappedNameOfCompany, scrappedLocation, scrappedActivelyRequiting)
        # mappedList = list(mappedData)
        #
        # current_excelsheet = googleSheetOpen()
        # # Add a fix range of google cells manually.
        # cell_list_JobTitle = current_excelsheet.range('A1:A50')
        # cell_list_NameOfCompany = current_excelsheet.range('B1:B50')
        # cell_list_Location = current_excelsheet.range('C1:C50')
        # cell_list_ActivelyRequiting = current_excelsheet.range('D1:D50')
        # # [TODO] global cell_list
        # # the enumerate() function is used to iterate over an iterable and return both the index and the
        # # corresponding element at that index. It is often used in for loops to keep track of the index of the current
        # # iteration.
        # for i, (Job, Company, Locality, StatusRequiting) in enumerate(mappedList):
        #     # [TODO] Trying to add range dynamically.
        #     # [TODO] cell_list = current_excelsheet.range('A1:A{}'.format(i+1))
        #     cell_list_JobTitle[i].value = Job
        #     cell_list_NameOfCompany[i].value = Company
        #     cell_list_Location[i].value = Locality
        #     cell_list_ActivelyRequiting[i].value = StatusRequiting
        #
        # current_excelsheet.update_cells(cell_list_JobTitle)
        # current_excelsheet.update_cells(cell_list_NameOfCompany)
        # current_excelsheet.update_cells(cell_list_Location)
        # current_excelsheet.update_cells(cell_list_ActivelyRequiting)
