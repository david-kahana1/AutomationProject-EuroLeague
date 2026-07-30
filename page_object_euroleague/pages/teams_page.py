import re
import allure

from page_object_euroleague.pages.basePage import BasePage


class teamsPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.base_page = BasePage(page)


    def search_a_team(self, team_name: str):
        self.base_page.do_search("Search team...", team_name)


    def press_on_the_founded_team(self, team_name: str):
        team = self.page.locator("li").filter(has_text=team_name).get_by_role("link").nth(3)
        team.click()


    def press_on_team(self, team_name: str):
        team = self.page.locator("[class='grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3']")
        team_button = team.page.get_by_role("link", name=team_name).first
        team_button.click()
        team_full_name_text = self.page.locator("[class='club-info-module-scss-module__ckJnHG__name club-info-module-scss-module__ckJnHG___isTeamHero']").text_content()
        return team_full_name_text


    def take_team_standing(self):
        self.page.get_by_role("link", name="Team", exact=True).click()
        team_standing = self.page.locator("[class='club-info-module-scss-module__ckJnHG__list club-info-module-scss-module__ckJnHG___isTeamHero']")
        the_teams_won_as_int = self.base_page.take_team_won(team_standing)
        the_teams_lost_as_int = self.base_page.take_team_lost(team_standing)

        if the_teams_won_as_int > the_teams_lost_as_int:
            print("the team standing is good")
        elif the_teams_won_as_int == the_teams_lost_as_int:
            print("the team standing is balanced")
        else:
            print("the team need to improve")

        print(f"the team's wins is: {the_teams_won_as_int} games, and the team's lost is: {the_teams_lost_as_int} games")
        return the_teams_won_as_int


    def teke_the_team_roster(self):
        roster = self.page.locator("[class='container-module-scss-module__JdNNcG__container team-roster-module-scss-module__9LCxGW__container container-module-scss-module__JdNNcG___wide']")
        roster_text = roster.text_content()
        names = re.findall(r"[A-Z']+\s+[A-Z'\s]+[A-Z]", roster_text)
        roster_names = []
        for name in names:
            cleaned = " ".join(name.split())
            if cleaned in ["Guard", "Forward", "Center", "Head Coach", "Assistant Coach"]:
                continue
            roster_names.append(cleaned)
        print(roster_names)
        return len(roster_names)


    def valid_the_coach(self, coach_name: str):
        with allure.step(f"valid_the_coach: {coach_name}"):
            coach_text = self.page.get_by_role("link", name=coach_name).text_content()
            start_index = coach_text.find('description":"')
            start_index += len('description":"')
            end_index = coach_text.find('"', start_index)
            coach_name = coach_text[start_index:end_index]
            print(f"the coach name is: {coach_name}")
            return coach_name


    def get_coach_nationality(self, coach_name: str):
        self.page.get_by_role("link", name=coach_name).click() #currently this link got '500 code' (Server error)
        coach_nationality_text = self.page.locator("[class='coach-info-list_info__N4op5']").text_content()
        start_index = coach_nationality_text.find('Nationality')
        start_index += len('Nationality')
        end_index = coach_nationality_text.find('Born', start_index)
        coach_nationality_name = coach_nationality_text[start_index:end_index]
        print(f"the coach nationality is: {coach_nationality_name}")
        return coach_nationality_name



    def change_roster_to_year(self,roster_year: str):
        print("Change roster to year")
        self.base_page.change_roster_per_year(roster_year)
        return self.page.url

