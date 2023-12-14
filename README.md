# BNumbers

Welcome to the BNumbers CLI Application, a Python-based command-line tool designed to capture, process, and analyze data effortlessly. This application simplifies data management and statistical analysis through an intuitive command-line interface.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
  - [Running Manually with Python](#running-manually-with-python)
  - [Running with Make](#running-with-make)

- [Contributing](#contributing)
- [License](#license)

## Introduction

The BNumbers CLI Application offers a seamless experience for capturing and analyzing numerical data. With a straightforward command-line interface, it allows users to perform various operations, including data capture, statistical analysis, and generating insights, all within a convenient terminal environment.

## Project Structure

The project directory structure is organized as follows:
- /app
    - /cli.py:  Contains the command-line interface module responsible for user interaction and commands handling.
    - /process.py: Includes functionalities for data capturing, statistical analysis, and data processing.
    - /exceptions.py: Houses custom exception classes for handling specific errors related to data capture and statistics.
- /tests: Directory for unit tests, including test files to validate the functionalities of the application's modules.
- /other_files: Contains other dependencies as Dockerfile, poetry file e.g

## Running the Application

### Running Manually with Python

1. **Installation:**
   - Ensure you have Python installed (version 3.11 above).
   - Install dependencies:

   ```bash
   pip install poetry 
   poetry install
   ```
1. **Execution:**
  Run the application:
   ```bash
    python main.py
   ```
   
### Running with Make

1. **Installation:**
   - Ensure you have Python installed (version 3.11 above).
   - Install dependencies:

   ```bash
   pip install poetry 
   poetry install
   ```
1. **Execution:**
  - Ensure you have `make` and `docker` installed.
   ```bash
    make build_docker
    make run_docker
   ```

### Contributing


### License

