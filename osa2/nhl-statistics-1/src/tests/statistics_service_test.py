import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        pelaaja = self.stats.search("Semenko")
        self.assertAlmostEqual(pelaaja.team, "EDM")
        self.assertAlmostEqual(pelaaja.goals, 4)

        pelaajaa_ei_ole = self.stats.search("Semenkko")
        self.assertIsNone(pelaajaa_ei_ole)
    
    def test_team(self):
        players_of_team = self.stats.team("EDM")
        names = [player.name for player in players_of_team]
        edm_players = ["Semenko", "Kurri", "Gretzky"]
        self.assertAlmostEqual(names, edm_players)

    def test_top(self):
        top3 = self.stats.top(2)
        top3_names = [player.name for player in top3] # funktion top palauttama top 3 pelaajan lista
        names = ["Gretzky", "Lemieux", "Yzerman"] # hardcodattu lista oikeilla arvoilla
        
        self.assertEqual(top3_names, names)
