from oneM2M_functions import *

server = "http://127.0.0.1:8080"
cse = "/~/in-cse/in-name/"


# ------------------------------------------
# Fill code here to create AE
# specified by the URI
# ------------------------------------------
ae = "Test-1"
lbl = ["AE-Label-1", "AE-Label-2"]
create_ae(server+cse, ae, lbl)
# ------------------------------------------


# ------------------------------------------
# Fill code here to create container in the AE
# specified by the URI
# ------------------------------------------
container_name = "Data"
lbl = ["CNT-Label-1", "CNT-Label-2"]
create_cnt(server+cse+ae, container_name)
# ------------------------------------------


# ------------------------------------------
# Fill code here to create content_instance
# specified by the URI
# ------------------------------------------
content_instance = 0
lbl = ["CIN-Label-1", "CIN-Label-2"]
create_data_cin(server+cse+ae+"/"+container_name, content_instance)
# ------------------------------------------

# ------------------------------------------
# Fill code here to get latest content_instance
# specified by the URI
# ------------------------------------------
# ret_code, latest_data = get_data(server+cse+ae+"/Data/la")
# print(latest_data)
# ------------------------------------------

# ------------------------------------------
# Fill code here to get oldest content_instance
# specified by the URI
# ------------------------------------------
# ret_code, oldest_data = get_data(server+cse+ae+"/Data/ol")
# print(oldest_data)
# ------------------------------------------

# ------------------------------------------
# Fill code here to get all content_instances
# specified by the URI
# Note: change the return statement as given in get_data function inside the oneM2M_functions.py
# ------------------------------------------
# ret_code, all_data = get_data(server+cse+ae+"/Data?rcn=4")
# print(all_data)
# ------------------------------------------
