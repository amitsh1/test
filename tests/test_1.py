from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
import os
from okapi.models import Rent
# from django.core.urlresolvers import reverse
from django.urls import reverse
class AnimalTestCase(TestCase):
    def test_upload_csv(self):
        # verify db is empty
        assert list(Rent.objects.all())==[]

        # upload a csv file
        data = open("/code/test_data/Rent-Roll.csv", 'rb')        
        file_ = SimpleUploadedFile(content=data.read(), name="file_content",content_type='multipart/form-data')
        response=self.client.post("/upload/", {'file': file_})
        # print(response.content)

        # verify the information is in the db
        objects = list(Rent.objects.all())
        # not empty
        assert objects!=[]

        # verify length equals 4(one entry annual rent is less then 1.3 M)
        assert len(objects)==4

        # verify data types in db
        assert type(objects[0].AnnualRent)==int
