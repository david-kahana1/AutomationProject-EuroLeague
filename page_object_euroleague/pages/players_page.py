import allure

from page_object_euroleague.pages.basePage import BasePage


class playersPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.base_page = BasePage(page)
        self.player_stats = page.locator("[class='stats-item-module-scss-module__YmOhIW__value']")


    def search_player(self, player_name):
        self.page.locator("#main #season").select_option("E2025")  # need for find players
        self.base_page.do_search("Search player...", player_name)


    def press_on_player(self, player_name):
        player = self.page.get_by_text(player_name)
        player.click()
        player_full_name_text = self.page.locator("[class='text-3xl font-bold text-primary']").text_content()
        return player_full_name_text


    def print_no_players_found(self):
        no_players_found_massage_text = self.page.get_by_text("No players found yet").text_content()
        print(no_players_found_massage_text)
        return no_players_found_massage_text


    def take_player_points_avg(self):
        player_stats = self.player_stats.first
        return self.base_page.float_the_numbers(player_stats,"points avg")


    def take_player_rebounds_avg(self):
        player_stats = self.player_stats.nth(1)
        return self.base_page.float_the_numbers(player_stats,"rebounds avg")


    def take_player_assists_avg(self):
        player_stats = self.player_stats.nth(2)
        return self.base_page.float_the_numbers(player_stats,"assists avg")


    def get_player_information(self):
        with allure.step(f"Getting player information"):
            player_name = self.page.locator("[class='text-3xl font-bold text-primary']").text_content()
            number_and_position_info = self.page.locator("[class='flex flex-row gap-2 items-center']").text_content()
            other_information = self.page.locator("[class='flex flex-row flex-wrap gap-y-3 gap-x-3 md:gap-x-16']").text_content()
            print(player_name, number_and_position_info, other_information)
            return number_and_position_info


    def take_player_points_record(self):
        with allure.step(f"Getting player points record"):
            record_button = self.page.get_by_text("Records")
            record_button.click()
            points_record = self.page.locator("[class='player-career-table-row-module-scss-module__8hkRjG__value player-career-table-shared-module-scss-module__uzhN1W__cell']").nth(1)
            return self.base_page.float_the_numbers(points_record,"points record")

