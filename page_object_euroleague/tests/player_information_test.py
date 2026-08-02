import pytest


@pytest.mark.regression
class TestPlayerInformation():


    def test_search_player_without_result(self, setup_euroleague):
        print("Test search player without result Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("Deni Avdija")
        not_found = players_page.print_no_players_found()
        assert not_found == "No players found yet", "the search not succeeded"


    def test_search_tamir_blatt(self, setup_euroleague):
        print("Test search tamir blatt Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("Tamir") #they have failure in the names- it's work only with one word without full names
        player_name = players_page.press_on_player("Blatt")
        assert player_name == "TAMIR BLATT", "the search of tamir blatt was failed"


    def test_search_player_by_last_name(self, setup_euroleague):
        print("Test search player by last name Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("sorkin")
        player_name = players_page.press_on_player("sorkin")
        assert player_name == "ROMAN SORKIN", "the search player by last name was failed"


    def test_teke_player_information(self, setup_euroleague):
        print("Test teke player information Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("DIBARTOLOMEO")
        players_page.press_on_player("JOHN")
        number_and_position = players_page.get_player_information()
        assert number_and_position == "#12•Guard", "the information is wrong"


    def test_take_player_stats(self, setup_euroleague):
        print("Test take player stats Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("YAM")
        players_page.press_on_player("MADAR")
        player_points_avg = players_page.take_player_points_avg()
        players_page.take_player_rebounds_avg()
        players_page.take_player_assists_avg()
        assert player_points_avg == 4.7, "the average is not correct"


    def test_take_player_point_record(self, setup_euroleague):
        print("Test take point record Start")
        page, home_page, players_page, teams_page = setup_euroleague
        home_page.go_to_players_page()
        players_page.search_player("SASHA")
        players_page.press_on_player("VEZENKOV")
        player_points = players_page.take_player_points_record()
        assert player_points >= 45, "the record is not correct"

