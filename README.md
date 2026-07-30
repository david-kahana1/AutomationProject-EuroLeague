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
There are functions that perform:
<br>
Searching players with and without results, navigating to a player profile by first or last name,
<br> 
taking player information and statistics, validating player records, taking team standings, validating current coach,
<br>
getting team roster, and navigating through all main site pages such as players, teams, games, stats, videos and more.
<br>
<br>
During testing, I identified a failure (bug) in the player search feature:
<br>
the search works only with a first name or last name, but not with a full name.
<br>
<br>
You are welcome to explore the source code in the project folders.

<br>
<br>

<p align="center"><b>In the attached video, you can see the execution of the automation tests.</b></p>

<video src="https://github.com/user-attachments/assets/adf6a08e-f210-4e07-91c1-1cca49a7aa15"
  controls 
       width="640">
</video>


<p align="center"><b>The Test result from Allure Report</b></p>
<div align="center">
  <img src="https://github.com/user-attachments/assets/08767be3-434d-445b-8cbf-e8497b4dd0f2https://github.com/user-attachments/assets/08767be3-434d-445b-8cbf-e8497b4dd0f2" width="1652" height="426" alt="Image">
</div>

<br>
