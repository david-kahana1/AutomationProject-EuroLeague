from playwright.sync_api import expect

from page_object_euroleague.pages.basePage import BasePage


class homePage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.base_page = BasePage(page)
        self.page.wait_for_load_state("networkidle") #Reject All Cookies for GitHub CI/CD runs
        try:
            self.page.get_by_role("button", name="Reject All Cookies").wait_for(state="visible", timeout=60000)
            self.page.get_by_role("button", name="Reject All Cookies").click()
        except:
            print("Cookie banner not shown - continuing")


    def go_to_players_page(self):
        self.base_page.go_to_page("players","Players")


    def go_to_teams_page(self):
        self.base_page.go_to_page("teams","Teams")


    def go_to_games_page(self):
        self.base_page.go_to_page("game-center","Games")


    def go_to_standings_page(self):
        self.base_page.go_to_page("standings","Standings")


    def go_to_stats_page(self):
        self.base_page.go_to_page("stats","Stats")


    def go_to_news_page(self):
        self.base_page.go_to_page("news","News")


    def go_to_final_four_page(self):
        self.base_page.go_to_page("final-four","Final four")


    def go_to_fantasy_page(self):
        self.base_page.go_to_page("fantasy","Fantasy")


    def go_to_videos_page(self):
        self.base_page.go_to_page("videos/all","Watch")


    def go_to_login_page(self):
        print("Go to login page")
        login_button = self.page.get_by_role("button", name="Login")
        login_button.click()
        expect(self.page.locator("#signin_main_title")).to_contain_text("Login with your EuroLeague ID")
        login_message_text = self.page.locator("[id='signin_main_title']").text_content()
        return login_message_text


    def get_team_from_menu(self,team_name):
        print("Get team menu bar")
        self.page.get_by_role("link", name="Teams").first.hover()
        team_button = self.page.get_by_role("link", name=team_name).first
        team_button.click()
        self.page.wait_for_url(f"**/roster/bar/**")
        return self.page.url


    def get_team_by_link(self,team_name: str, link_name: str):
        return self.base_page.go_to_team(team_name,link_name)

