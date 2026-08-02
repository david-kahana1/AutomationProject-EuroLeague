import allure
import pytest

from page_object_euroleague.config import TEAMS


@pytest.mark.sanity
class TestNavigation():


    def test_go_to_players(self, setup_euroleague):
        print("Test go to players Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/players/", "it's not the URL of players pages"


    def test_go_to_teams(self, setup_euroleague):
        print("Test go to teams Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/teams/", "it's not the URL of teams pages"


    def test_go_to_team_from_menu_bar(self, setup_euroleague):
        print("Test go to team from menu bar Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.get_team_from_menu("FC Barcelona")
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/teams/fc-barcelona/roster/bar/", "it's not the URL of Barcelona"


    def test_go_to_home_page(self, setup_euroleague):
        print("Test test go to home pages Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_games_page()
        home_page.press_on_logo()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/", "it's not the URL of home pages"


    def test_go_to_games(self, setup_euroleague):
        print("Test test go to games Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_games_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/game-center/", "it's not the URL of games pages"


    def test_go_to_standings(self, setup_euroleague):
        print("Test test go to standings Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_standings_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/standings/", "it's not the URL of standings pages"


    def test_go_to_stats(self, setup_euroleague):
        print("Test test go to stats Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_stats_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/stats/", "it's not the URL of stats pages"


    def test_go_to_news(self, setup_euroleague):
        print("Test test go to news Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_news_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/news/", "it's not the URL of news pages"


    def test_go_to_final_four(self, setup_euroleague):
        print("Test test go to final four Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_final_four_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/final-four/", "it's not the URL of final-four pages"


    def test_go_to_fantasy(self, setup_euroleague):
        print("Test test go to fantasy Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_fantasy_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/fantasy/", "it's not the URL of fantasy pages"


    def test_go_to_videos(self, setup_euroleague):
        print("Test test go to videos Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_videos_page()
        assert page.url == "https://www.euroleaguebasketball.net/en/euroleague/videos/all/", "it's not the URL of videos pages"


    def test_go_to_login(self, setup_euroleague):
        print("Test test go to login Start")
        page, home_page, players_page, teams_page = setup_euroleague
        login_message_text = home_page.go_to_login_page()
        assert login_message_text == "Login with your EuroLeague ID", "it's not the URL of login pages"


    @pytest.mark.parametrize("team", TEAMS) #Data Driven Test, running for all the teams.
    def test_go_to_team_by_link(self, setup_euroleague, team):
        allure.dynamic.title(f"Testing navigation to {team['link_name']} Start")
        print(f"Testing navigation to {team['link_name']} Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.get_team_by_link(**team)
        assert team["team_name"] in page.url, f"the Navigation to {team['link_name']} was failed"

