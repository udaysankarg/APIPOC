# REST API Testing using behave (python based framework)
Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

behave is behaviour-driven development framework based on Python and uses tests written in a natural language style, backed up by Python code, suitable to test and validate REST APIs and Services.

It uses Gherkin language to write business readable tests that validate the behavior of REST APIs

- Sample Gherkin format:
    
      Feature: showing off behave

      Scenario: run a simple test
         Given we have behave installed
          When we implement a test
          Then behave will test it for us!
       
        Scenario Outline: To validate the status code and status message
            When I make a "GET" request to "/Categories/<CategoryID>/Details.json?catalogue=false"
            Then the response status code should equal "<ResponseCode>"
            And the response status message should equal "<Status_msg>"

            Examples: Response code check @<CategoryID>
                |CategoryID|ResponseCode|Status_msg |
                |6327      |200         |OK         |
                |1234      |400         |Bad Request|
behave supports reporting in many ways. It can generate reports in junit xml formats or json format which can be used in continuous integration in Jenkins and customization of reports based on the business users need. 

We can orchestrate our automation using tags which can be applied to scenarios and features

# Project Structure
Feature files are intended to locate in /features folder

Corresponding steps are located in /features/steps

Overall project structure is as follows:

    +-- requirements.txt // store python requirements

    +-- README.md // this file 

    +-- behave.ini // configuration file for behave

    +-- logging_config.ini // configuration file for logger

    +-- features/

        +-- conf.json // store project config (urls, global variables, etc.)

        +-- environment.py // context setup steps (e.g. load from config)

        +-- *.feature // feature files

        +-- steps/

            +-- __init__.py // used to import predefined steps

            +-- *.py // steps related to corresponding feature (e.g. "apitest.py" contains steps that are related to "APIPOC.feature")  
    
    +-- results/
    
        +-- logs/  // To keep all logs
    
        +-- reports // To keep all junit report files
    
    +-- utils/

        +-- __init__.py // used to import predefined steps
    
        +-- apicalls.py // Utils for API call like GET,POST etc    

    +--venv_p3 // Python3 interpreter is installed here using virtualenv

# SETUP and USAGE GUIDE
The framework has been successfully tested in latest Python 3.7.4 version on Windows 10 machine. 
- Prerequisities :

    Any OS (Windows/Linux/Mac)
    
    Git client

- Clone project from Github

    From the terminal 
    
        git clone https://github.com/udaysankarg/APIPOC.git
 

- Activate the virtualenv 

    From the project home folder activate the Python virtualenv (which has all the requirements already installed)

        .\venv_p3\Scripts\activate

- To execute all feature files (all tests)

        behave

- To execture specific feature

        behave features

- run features with specific tags
    
        behave --tags=AC

- Logs and reports will be saved under the results folder

     Sample logs
     
        (venv_p3) C:\Users\Dell\PycharmProjects\APIPOC>behave -t AC
        11:09:08 - INFO  :: Starting scenario: To validate whether details of Carbon credits under Business-farming-industry
        11:09:08 - INFO  :: Base url set to : https://api.tmsandbox.co.nz/v1
        11:09:08 - INFO  :: Calling API: https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
        11:09:10 - INFO  :: Response code received : 200
        11:09:10 - INFO  :: Pattern "6327" found in response
        11:09:10 - INFO  :: Pattern "Carbon credits" found in response
        11:09:10 - INFO  :: Pattern "True" found in response
        11:09:10 - INFO  :: Pattern "2x larger image" found in response
        11:09:10 - INFO  ::     ============= Scenario PASSED ============
        1 feature passed, 0 failed, 0 skipped
        1 scenario passed, 0 failed, 9 skipped
        7 steps passed, 0 failed, 44 skipped, 0 undefined
        Took 0m1.862s

- Reports

    Junit xmls can be found in the results/reports folder which can be integrated with Jenkins
        
        .\results\reports\TESTS-APIPOC.xml