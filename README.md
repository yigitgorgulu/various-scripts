# various-ps-scripts
Small scripts I wrote in Powershell that perform small tasks. The scripts are explained in small detail below.

## recursive-unzipper.ps1
This program unzips ZIP files which have a single folders within folders (e.g. main > com > companyName > projectName, and projectFiles contains all project files), and extracts all files to the root level (main in the example).

## folder-capitalizer.ps1
This program capitalizes the first letters of all folder names in a directory. ("example" turns into "Example", and "example folder" turns into "Example Folder").