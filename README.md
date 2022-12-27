# **various-scripts**
Small scripts written in various languages that perform small tasks. The scripts are explained below, categorized by programming language.

## **powershell**
### *recursive-unzipper*
This program unzips ZIP files which have single folders within folders (e.g. main > com > companyName > projectName, and projectName contains all project files), and extracts all files to the root level (main in the example).

### *folder-capitalizer*
This program capitalizes the first letters of all folder names in a directory. ("example" turns into "Example", and "example folder" turns into "Example Folder").

## **python**
### *timer*
When each element of an Iterable is processed in a long time (e.g. querying a database for each element in a 500 element list), this script keeps track of progress. Displays last processed element, elapsed time and estimated remaining time depending on previous operations.
