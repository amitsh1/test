from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
import os
from okapi.models import Rent
# from django.core.urlresolvers import reverse
from django.urls import reverse
class AnimalTestCase(TestCase):
    def test_upload_video(self):
        # verify db is empty
        assert list(Rent.objects.all())==[]

        # upload a csv file
        data = open("/code/test_data/Rent-Roll.csv", 'rb')        
        file_ = SimpleUploadedFile(content=data.read(), name="file_content",content_type='multipart/form-data')
        response=self.client.post("", {'video': file_})

        # verify the information is in the db
        assert list(Rent.objects.all())!=[]
        # some important assertions ...