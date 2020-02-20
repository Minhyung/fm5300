Gigamon Inc

Gigamon Automation SDK For Python

Overview
--------

Gigamon Automation SDK for Python:

  - provides programmatic access to GigaVUE-FM to manage and monitor the 
    Gigamon Visibility Fabric

  - bundled with REST API Client which provides the actual binding to FM REST
    APIs. It allows user to create python scripts using all public REST API
    currently supported by FM.


Intended Audience and Applications
----------------------------------

  - IT Operations Management (ITOM) groups can easily automate tasks related to: 

    > Configuration management (ports, maps ..etc) Inventory management
    > (available cards slots, ports ..etc) Fault monitoring and management
    > Maintenance tasks such as Backup/Restore, Reboot ..etc

  - Security administrators

    > Change the traffic forwarding policies in response to threats or
    > anomalous network traffic changes


Prerequisites
-------------

+ Make sure to setup the below environment

  - GigaVUE-FM

  - Ubuntu 14.04 (and latest) / CentOS 7.x / Mac OS / Windows 7 or latest

  - Python 2.7.13 or latest / Python 3.4.X with below modules
    > "cryptography" module "pyopenssl" module "requests" module
    > "tapioca-wrapper" module


Installation Instructions
-------------------------

+ Follow the steps below to download, extract and setup the FM API Python SDK

  $ cd /tmp $ tar -xzf fm_sdk_python<VERSION>.tgz
  $ cd fm_sdk_python<VERSION>

+ Run the below command to setup the environment

  $ source setup.sh
 

+ To test if the installation is successful, run the script below against the
  deployed GigaVUE-FM

  $ cd examples
  $ python test_fm_api.py <FM IP> <FM USER> <FM PASSWORD>


Directory Structure
-------------------

+ fm_api_sdk<VERSION>/lib
 
  - Includes FM API Client module that provides binding to FM REST APIs

+ fm_api_sdk<VERSION>/utils

  - Includes custom modules to exercise various GigaVUE-FM functionalities.

+ fm_api_sdk<VERSION>/examples

  - Includes python script samples that demonstrates capabilities to perform a
    specific task using the base libraries and custom modules.

+ fm_api_sdk<VERSION>/doc
 
  - Includes documentation related to Python SDK.



Reference
---------

+ GigaVUE-FM API Reference can be accessed through the following URL:

  - Open the browser and on one TAB, login to FM

  - Open another TAB and access the GigaVUE-FM API Reference using the link
    below:

    https://<FM IP address>/apiref/apiref.html 

+ Below reference file contains the mapping between API endpoints to methods in
  FM API Client module.

  - fm_api_sdk/doc/api_reference.txt

+ GigaVUE-FM REST API Getting Started Guide

  - This is available as part of the GigaVUE-FM online help.

+ SDK uses Python requests library to communicate with GigaVUE-FM server.
  Link to a quick start guide is below:

  - http://docs.python-requests.org/en/master/user/quickstart/






How to use GigaVUE-FM SDK for Python?
-------------------------------------

There are two ways to take advantage of the SDK:

  I. By directly accessing the API Binding Module

  II. By using the API Services modules
      - Custom modules for performing common tasks with ease


I. Examples using API Binding Module
------------------------------------

+ Create an instance of the FM API Client

  # Create FM API client instance that will log in both standard out and file at
  # a specific location

  from fm_test_api_binding import FmClient

  myClient = FmClient(fm_ip='10.120.4.65', username='admin',
                                              password='admin123A!')
 
+ To use HTTP GET method

  # Make a GET call to endpoint: /nodes
  response = myClient.nodes().get()
 
  # Make a GET call with query parameters in URL, such as
  # /nodes?key1=val1&key2=val2

  payload = {'key1': 'value1', 'key2': 'value2'}
  response = myClient.nodes().get(params=payload)
 
  # Make a GET call to an endpoint that has variables in path, such as
  # /inventory/chassis/cards/{slotId}

  response = myClient.inventorychassiscardsslotId(slotId="id").get()

+ To use HTTP POST method (to create a new resource)

  # Make a post call

  payload = { "nodeAddSpecs": [ { "nodeAddress": device_ip, "username":
                             device_username, "password": device_password }] } 

  response = myClient.nodes().post(data=payload)


+ To use HTTP PATCH method (to modify/update properties of an existing resource)

  portId = '1/1/x1' p_ortId = '1_1_x1'
  
  payload = { 'portId' : portId, 'adminStatus' : 'up' }

  params = { 'clusterId' : '10.120.4.56' }

  response = myClient.inventoryportsportId(portId=p_ortId).patch(params=params,
                                                                  data=payload)

+ To use HTTP DELETE method (to delete an existing resource)

  # Make a DELETE call

  response = myClient.nodes(clusterId='10.120.4.56').delete()

+ Check API response

  # Get the return status code

  return_code = response.status_code
 
  # Get the content of the response in json format

  content = response.content

+ Logging

  Access logs are automatically added to the log file.  For individual log, it
can be added in the script using the built-in logger. 

  Below is the example:

  - log_dir is optional to set where the log file will be generated
  - log_name is optional to set the name of the log file
  - screen_out default is False.  When set to True, logs goes into both file and
    stdout

  myClient = FmClient(fm_ip='10.120.4.56', username='admin',
password='admin123A!', log_dir="/tmp", log_name="test.log", screen_out=True)

  myClient.logger.info("info log") myClient.logger.debug("debug log")
myClient.logger.error("error log")
 
  In the above example,

  - log will be generated at /tmp/test.log
  - if log_path is not specified, the log file will be created on the current
    running directory with file name fmclient.log


II. Examples using API Services Modules
---------------------------------------

+ Current list of services modules

  - available under fm_api_sdk<VERSION>/utils directory

+ Working samples available under fm_api_sdk<VERSION>/examples directory

  1. get_fm_info.py
     - Script to get FM version info

  2. add_node.py
     - Script to add a device to FM

  3. add_nodes_from_csv.py
     - Script to bulk add devices to FM by using a CSV file as input
     - Sample CSV file template provided (NODES.csv.template)

  4. delete_node.py
     - Script to remove a device from FM

  5. update_port.py
     - Script that demonstrates bulk update of port properties for a given
       device

  6. bulk_update_map.py
     - Script to bulk update map (passed using a CSV file) using FM
     - Can be used to add pass/drop rules to an existing map
     - Refer to "MAP_UPDATE.csv.template" for the CSV file format

  7. bulk_update_port.py
     - Script for performing bulk port updates
     - Identifying all TAs and enable neighborDiscovery on all network ports

  8. create_map.py
     - Script for creating a regular map with passRules

  9. update_map.py
     - Script to update an existing map (with alias 'testMap')

  10. get_card_inventory.py
     - Script that generates a "card inventory" report for all the devices
       managed by FM

  11. get_fm_events.py
     - Script that generates a report based on the device traps received by FM
       (for any given time period)

  12. get_node_inventory.py
     - Script to fetch device inventory from FM based on one or more filters

  13. get_port_inventory.py
     - Script that gets ports inventory (from one or more devices) matching one
       or more types

  14. get_unhealthy_ports.py
     - Script that generates a report for all the unhealthy ports across all
       devices managed by FM
     - Unhealthy ports referred here ports that are "admin enabled" but "link
       down" and part of map(s)

  15. identify_ports_not_part_of_map.py
     - Script that identifies number of ports that are not part of map across
       all devices managed by FM
