# Fundação Potência's database manager, built with Streamlit and integrated with Google Sheets.

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Pages](#pages)

## Overview

This repository contains a Streamlit application designed to manage and update many datasets stored on Google Drive/Sheets. It also includes a mechanism to handle authentication if the Google Drive API token expires.

## Files

The repository consists of four main files, each representing a page of the Streamlit app:

1. **main.py**: Home page
2. **tutorial.py**: Page that briefly explains how to use the application
3. **update_db.py**: Page to update the `db_Olimpidas` and `dAlunos` dataset
4. **update_entrevistas.py**: Page to update the `dEntrevistas` dataset

Additionally, the repository includes the next packages:

- **classes**: Contains the basic structure of the Streamlit app.
- **utils**: Includes other utilities such as background images and logos.
- **requirements.txt**: Lists the libraries needed to run the app.

## Installation

To run this app locally, you need to have the dependencies installed. You can install the required libraries using the following command:

```sh
pip install -r requirements.txt
```

## Running the App

To run the app locally, use the following command in your terminal:

```sh
streamlit run main.py
```

Feel free to explore and update the datasets as needed. For any issues or contributions, please open an issue or submit a pull request. Enjoy using the app!
