import pytest


@pytest.mark.critical
class TestTeamInformation():


    def test_press_on_team(self, setup_euroleague):
        print("Test press on team Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        team_full_name = teams_page.press_on_team("Hapoel IBI Tel Aviv")
        assert team_full_name == "Hapoel IBI Tel Aviv Roster", "it's not hapoel"


    def test_team_standing(self, setup_euroleague):
        print("Test team standing Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("Real Madrid")
        teams_page.press_on_the_founded_team("Real Madrid")
        team_wins = teams_page.take_team_standing()
        assert team_wins >= 0, "the standing not impossible"


    def test_maccabi_standing(self, setup_euroleague):
        print("Test team standing Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("maccabi")
        teams_page.press_on_the_founded_team("maccabi")
        team_wins = teams_page.take_team_standing()
        assert team_wins >= 0, "the team need to improve"


    def test_get_team_roster(self, setup_euroleague):
        print("Test team roster Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("maccabi")
        teams_page.press_on_the_founded_team("maccabi")
        len_roster = teams_page.teke_the_team_roster()
        assert len_roster >= 15, "the roster too small"


    def test_get_team_coach(self, setup_euroleague):
        print("Test team coach Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("maccabi")
        teams_page.press_on_the_founded_team("maccabi")
        coach_name = teams_page.valid_the_coach("ODED KATTASH")
        assert coach_name == "ODED KATTASH", "it's not the original coach"


    def test_get_fenerbahce_coach(self, setup_euroleague):
        print("Test fenerbahce coach Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("fenerbahce")
        teams_page.press_on_the_founded_team("fenerbahce")
        coach_name = teams_page.valid_the_coach("Saras")
        assert coach_name == "SARAS JASIKEVICIUS", "it's not the original coach"


    def test_get_coach_nationality(self, setup_euroleague):
        print("Test get coach nationality Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.search_a_team("Maccabi")
        teams_page.press_on_the_founded_team("maccabi")
        coach_nationality = teams_page.get_coach_nationality("ODED KATTASH") #they have a failure here: '500 code' (API Server error)
        assert coach_nationality == "Israel", "the nationality incorrect"


    def test_get_old_roster(self, setup_euroleague):
        print("Test get coach nationality Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_teams_page()
        teams_page.press_on_team("Maccabi")
        teams_page.change_roster_to_year("E2013")
        teams_page.teke_the_team_roster()
        assert "season=2013-14" in page.url, "the roster incorrect"

