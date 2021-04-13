Assuming you got a task to implement a system that should serve 2 main functions.

HTML page that shall enable users to upload rent rolls data (csv) and store data in a DB (attached is an example)
HTML page that shall read the data from DB and present table of the buildings uploaded to the system
Building Page should present the city, and list of tenens ordered by lease type, for each building in the list
 

Tasks:

Write several options for HTTP server frameworks, that can be used to implement this system.
Describe what is your preferred option and why it is your preference.
Implementation phases:
Build HTTP serve (If you are familiar with django please use it regardless your answer to Q-2)
Implement html page for user to upload data from csv
Save the uploaded data, but only leases where annual rent > $1.3M
Implement html page that present a table of all buildings.
                                                    i.     For each building present its city and the list of tenants in this building (ordered by leas type)

                                                   ii.     Add filter to this page that enable user to filter the list by lease SQFT.

Use simple CSS just so it would be readable.