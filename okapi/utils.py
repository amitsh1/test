from .models import Rent
import csv
import io
def insert_csv_to_db(csv_file):
    """
    not using pandas for simplicity
    """

    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)

    dataReader = csv.reader(io_string, delimiter=',', quotechar='"')

    # Save the uploaded data, but only leases where annual rent > $1.3M
    for row in dataReader:
        if eval(row[11]) >1300000:
            rent_object=Rent()
            rent_object.firm_url=row[0]


            rent_object.PropertyName = row[0]
            rent_object.PropertySqft = row[1]
            rent_object.City = row[2]
            rent_object.LeaseNumber = row[3]
            rent_object.LeaseType = row[4]
            rent_object.TenantName = row[5]
            rent_object.UnitNumber = row[6]
            rent_object.UnitSqft = row[7]
            rent_object.LeaseBeginDate = row[8]
            rent_object.LeaseEndDate = row[9]
            rent_object.AnnualRentSqft= row[10]
            rent_object.AnnualRent = row[11]

            rent_object.save()    