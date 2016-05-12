# 31TEN DEV RESSOURCES & DOCUMENTATION

## INTRODUCTION

The goal of that repository is increasing the code reusability and code quality. There will be several types of elements

 * Snippets of code
 * Scripts
 * Coding Guidelines for each language

## USING THE REPOSITORY

- You can search on the repository for a specific function or functionality by either
	- Cloning the repository and use the global search of your code editor (CTRL+SHIFT+F on sublime text 2 for example, I recommend here sublime text 2 because you can have a )
	- Using the [github repository search ](https://github.com/31ten/documentation/search?utf8=%E2%9C%93&q=javascript "github repository search")

## CONTRIBUTION GUIDELINES

- The most critical point when contributing on the documentation is making your contribution self-explanatory to another developer.

#### COMMENTS
Place comments before each class or function respecting PSR2 standards.

Example : 

    /**
    * A great method which shows how to indent control structures.
    *
    * @param MyClass $object An instance of MyClass
    * @param array $someArray Some array
    * @return void
    * @throws \Exception
    */
	{
	 $this->fanOfFlow = $isFan;
	}

Try as much as possible to put the maximum information as possible on the comments. If the information to write is more than 6 lines (apart from the @params, @return, @throws), create a new markdown file in the same folder GUIDE-name-of-the-file.md

Examples :

- CLASS-wechat-qrcode-scanner.php 
- GUIDE-wechat-qrcode-scanner.md

#### FILE CONTENT 
Each file should have one main functionality. The functionality should be reflected by the name of the file. 
The name of the file should be one or several words separated by dashes describing the content of the file. The first word, uppercased, represent the nature of the file content : 

- CLASS
- FUNCTION
- SCRIPT
- TEMPLATE
- GUIDELINES
- GUIDE (Should be written using markdown synthax and should have the .md extension)

Examples : 

- CLASS-wechat-qrcode-scanner.php
- GUIDE-website-backup-system.md

#### FOLDER STRUCTURE 
The folder structure is divided by technology first and then by functionality

Examples : 

- Linux > Nginx
- Bash > Maintenance
- MeteorJS > Migration