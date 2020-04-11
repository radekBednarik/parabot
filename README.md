# Parabot

Utility for RobotFramework - run test .robot files in paralel even, if they are not specifically written for this.

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)


## About <a name = "about"></a>

If you want to simply execute your robotframework test files in parallel fashion, you can use this tool.
It leverages multiprocessing package of python, so there is no worry about specifically preparing your tests.

Currently, this tool only allows for executing all .robot files it can find in project directories tree.

Because of the parallel execution of the robotramework run module, the console outputs are bit garbled. However, log files are correctly saved to distinct and timestamped directories.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them.

- Python 3+
- RobotFramework library
- RobotFramework selenium library

Just run [sudo] python[3] setup.py install and it will take care of it for you.

### Installing

1. Run _[sudo] python[3] setup.py install_
2. You can try the project on the examples tests in the folder _examples_. For that just run _python[3] manage.py -a_. Unfortunate side effect of running tests as parallel processes is messed console output. However, log files are correctly places in timestamped directories in the appropriate test suite folder.
3. To try it on your project:
    
    3.1 Create a new branch for this, if things get messed up!!!

    3.2 Copy _parabot folder, manage.py and setup.py_ into the root of your project
    
    3.3. Run _[sudo] python[3] setup.py install_
    
    3.4. Run _python[3] manage.py -a_
    
    3.5. See what happens :). Depends on the structure of your project, where the output folders will be created. Rule is, that they are created _one level up_.

