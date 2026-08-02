import allure



class BasePage():

    def __init__(self,page):
        self.page = page


    def do_search(self, element: str, text: str):
        with allure.step(f"{element}: '{text}' "):
            print(f"{element}")
            search_line = self.page.locator("#main").get_by_placeholder(element)
            search_line.click()
            search_line.clear()
            search_line.fill(text)


    def go_to_page(self, page_name: str, element_name: str):
        with allure.step(f"Go to '{element_name}' page"):
            print(f"Go to '{element_name}' page")
            page_name_button = self.page.get_by_role("link", name=element_name).first
            page_name_button.click()
            self.page.wait_for_url(f"**/{page_name}/") #Verifies URL change during full execution
            return self.page.url


    def go_to_team(self, team_name: str, link_name: str):
        with allure.step(f"Go to '{link_name}' page by link"):
            print(f"Go to '{link_name}' page by link")
            page_name_link = self.page.get_by_role("link", name=link_name, exact=True)
            page_name_link.click()
            self.page.wait_for_url(lambda url: team_name in url)
            print(f"the URL of '{link_name}' is: {self.page.url}")
            return self.page.url


    def change_roster_per_year(self, year: str):
        with allure.step(f"Change roster to different year"):
            self.page.locator("#main").get_by_role("combobox").select_option(year)


    def float_the_numbers(self, player_stats, stats_type: str):
        with allure.step(f"Getting {stats_type}"):
            print(f"Getting {stats_type}")
            player_stats_text = player_stats.text_content()
            player_stats_as_float = float(player_stats_text)
            print(f"the {stats_type} is: {player_stats_text}")
            return player_stats_as_float


    def take_team_won(self, team_standing):
        with allure.step(f"Getting team's won standing"):
            team_standing_text = team_standing.text_content()
            lost_index = team_standing_text.index("L")
            the_teams_won = team_standing_text[4:lost_index]
            return int(the_teams_won)


    def take_team_lost(self, team_standing):
        with allure.step(f"Getting team's lost standing"):
            team_standing_text = team_standing.text_content()
            lost_index = team_standing_text.index("L")
            the_teams_lost = team_standing_text[lost_index+5:]
            return int(the_teams_lost)


    def press_on_logo(self):
        with allure.step("Clicking on logo"):
            print("Clicking on logo")
            logo_button = self.page.locator("[href='/en/euroleague/']").first
            logo_button.click()
            self.page.wait_for_url(f"**/euroleague/")
            return self.page.url

