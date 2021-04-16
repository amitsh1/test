from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from okapi.models import Rent

def get_table(driver,table_id):
    table = driver.find_element(By.ID, table_id)
    rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    headers = rows[0].find_elements(By.TAG_NAME, "th")
    headers = [x.text for x in headers]

    rows_data = []
    for row in rows[1:]:
        row_data = row.find_elements(By.TAG_NAME, "td")
        rows_data.append( [x.text for x in row_data])


    return headers,rows_data
class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.selenium = webdriver.Chrome(chrome_options=chrome_options)
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_table_before_upload(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))

        headers,rows = get_table(self.selenium,'rent_table')
        assert headers == ["PropertyName","City","tenents"]  
        assert len(rows)==0


    def test_upload(self):
        assert list(Rent.objects.all())==[]
        

        # go to upload page
        self.selenium.get('%s%s' % (self.live_server_url, '/upload'))

        # # select file and click sunbit
        
        # self.selenium.findElement(By.xpath("//input[@type='file']")).send_keys(os.getcwd()+"/image.png")
        self.selenium.find_element(By.XPATH,"//input[@type='file']").send_keys( "/code/test_data/Rent-Roll.csv")
        self.selenium.find_element(By.XPATH,"//button[@type='submit']").click()



        # verify the information is in the db
        objects = list(Rent.objects.all())
        # not empty
        assert objects!=[]

        # verify length equals 4(one entry annual rent is less then 1.3 M)
        assert len(objects)==4

        # verify data types in db
        assert type(objects[0].AnnualRent)==int

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        
        headers,rows = get_table(self.selenium,'rent_table')
        assert headers == ["PropertyName","City","tenents"]        
        assert len(rows)==2     
        assert rows[0][0]=='The Blue Building'
        assert rows[1][0]=='The Red Building'

        # verify no filtering
        assert len(rows[0][2].split(','))==2


        # add filter by greater then
        self.selenium.find_element(By.ID,"id_PropertySqft_min").send_keys( "53000\n")

        # verify filtering
        headers,rows = get_table(self.selenium,'rent_table')
        assert len(rows[0][2].split(','))==1   
