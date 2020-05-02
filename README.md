# Parabot

Utility for tests written using RobotFramework - run test .robot files in parallel even if they are not specifically written for this.

This utility **does not aim to replace pabot**. It is basically a test executor - just a quick project to be able to execute in parallel previously written RF test run in serial fashion. As such, it only offers three basic options.

For much sophisticated solution, use Pabot.

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>

If you want to simply execute your robotframework test files in parallel fashion, you can use this tool.
It leverages multiprocessing package of python, so there is no worry about specifically preparing your tests.

This tool currently supports:

- run all .robot files in parallel: _python[3] -m parabot -a_

  - this options is suitable in case, that your test project is structured in such a way, that each test suite .robot file contains everything. If not, do not use this and use argument _-f_ or _--folders_, see below.

- run all .robot files in specific folders: _python[3] -m parabot -f <relative_path_to_folder_1> ... <relative_path_to_folder_n>_.

  - you can specify multiple relative paths after the argument. This feature uses "extend" option introduced in Python's 3.8 argparse module. In lower versions this will not work and probably throws an error.

- run tagged tests/suites: _python[3] -m parabot -t <tag_1> ... <tag_n>_

  - use this option, if you want to run tagged test/suites in parallel. Since actual execution of tests is done by RobotFramework, parallelization in this case means **one tag == one process**. In each process are then sequentially run all tests/suites tagged by the same tag.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python 3.8+
- RobotFramework library
- RobotFramework selenium library

Just run [sudo] python[3] setup.py install and it will take care of it for you.

### Installing

You can either clone this package from the repository, or install it via pip.

In case of cloning, use these steps to install:

1. Run _[sudo] python[3] parabot/setup.py install_
2. You can try the project on the examples tests in the folder _examples_.
3. To try it on your project:

   3.1 Create a new branch for this, if things get messed up!!!

   3.2 Copy _parabot folder_ into the root of your project

   3.3. Run _[sudo] python[3] parabot/setup.py install_

   3.4. Run some of currently supported commands

   3.5. See what happens :).

In case of using pip:

1. Run command _sudo pip3 install parabot_

2. Then try available commands as described above.

### Test reports

For options _-a_ and _-f_ are timestamped report folders created in the same folder, where .robot file (test suite) is located.

For option _-t_ the timestamped report folders for **each tag** are created in the _reports_ folder located in the root.
