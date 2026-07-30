
## Automation Project - 'EuroLeague' 
<br>


My test project on the 'EuroLeague' basketball website.
<br>
For the tests, I used the Playwright framework in Python and wrote functions following Object-Oriented Programming (OOP) principles,
and designed them in the Page Object model.

### The Project Architecture:

**Pages:**
-	home page
-	players page
-	teams page

**Tests:**
-	'conftest'
-	navigation test
-	player information test
-	team information test
<br>

I added run parameters in the 'config' file for test execution, <br>
and introduced a 'BasePage' for shared page functionality.


<br>
 
**There are functions that perform:**
<br>
Searching players with and without results, navigating to a player profile by first or last name,
<br> 
taking player information and statistics, validating player records, taking team standings, validating current coach,
<br>
getting team roster, and navigating through all main site pages such as players, teams, games, stats, videos and more.
<br>
<br>


<p align="center"><b>In the attached video, you can see the execution of the player information tests:</b></p>

<video src="https://github.com/user-attachments/assets/6d82bb4f-d49b-4265-be59-e8ff5a1cf610"
  controls 
       width="640">
</video>

<br>

<p align="center"><b>The Test result from Allure Report:</b></p>
<div align="center">
  <img src="https://github.com/user-attachments/assets/cc8be8da-ec1d-4e5f-b0fb-b2a111c7fe40"
       alt="Image"
       style="max-width: 100%; height: auto;">
</div>

<br>
This project includes a fully integrated CI/CD pipeline using GitHub Actions, which automatically generates and deploys the Allure Test Report.
The CI environment configuration was assisted by Microsoft Copilot.

You can view the full test report here:
<div align="center">

### [**Open The Allure Report**](https://david-kahana1.github.io/AutomationProject-EuroLeague/)
</div>

<br>
<br>

### Related bugs:

During testing, I identified a failure (bug) in the player search feature:
<br>
the search works only with a first name or last name, but not with a full name.

<br>

And also in the team page I identified a failure:
<br>
Clicking the coach's name causes the site to crash and return a server error (500 code).

<p align="center"><b>The server error screen shot:</b></p>
<div align="center">
  <img src="https://github.com/user-attachments/assets/77ea6a6c-0564-4247-8394-fde4ea0f10cb"
       alt="Image"
       style="max-width: 100%; height: auto;">
</div>



<br>

You are welcome to explore the source code in the project folders.
