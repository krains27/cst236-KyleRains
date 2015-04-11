"""
Test for source.game
"""
from source.orc import Orc
from source.game import Game
from unittest import TestCase
from testfixtures import LogCapture
import logging
import __builtin__


class TestGame(TestCase):
    original_raw = None

    def setUp(self):
        self.original_raw = __builtin__.raw_input

    def tearDown(self):
        __builtin__.raw_input = self.original_raw
        logging.getLogger('source.orc').setLevel(logging.INFO)
        logging.getLogger('source.kingdom').setLevel(logging.INFO)
        logging.getLogger('source.game').setLevel(logging.INFO)

    def test_perimeter_no_breach(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'P'
            test_game = Game()
            test_game.handle_command()

        l.check()

    def test_perimeter_breach(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'P'
            test_game = Game()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=0)])
            test_game.handle_command()

        l.check(
            ('source.orc', 'INFO', 'Orc created with velocity=0 and distance=0'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 and distance=0'),
            ('source.game', 'INFO', 'Perimeter Breached')
        )

    def test_alert_issue_all_classes(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'P'
            test_game = Game()
            test_game.start()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=1, velocity=0)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Game has started'),
            ('source.orc', 'INFO', 'Orc created with velocity=0 and distance=1'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 and distance=1')
        )

    def test_alert_issue_game_class(self):
        with LogCapture() as l:
            test_game = Game()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.start()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=0)])

        l.check(
            ('source.game', 'INFO', 'Game has started')
        )

    def test_alert_issue_orc_class(self):
        with LogCapture() as l:
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.start()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=0)])

        l.check(
            ('source.orc', 'INFO', 'Orc created with velocity=0 and distance=0')
        )

    def test_alert_issue_kingdom_class(self):
        with LogCapture() as l:
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.start()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=0)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 and distance=0')
        )

    def test_X_ends_game(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'X'
            test_game = Game()
            test_game.start()
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Game has started'),
            ('source.game', 'INFO', 'Game has ended')
        )
        
    def test_orc_distance(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'D'
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=1, velocity=0)])
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=2, velocity=0)])
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=3, velocity=0)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc distance=1'),
            ('source.game', 'INFO', 'Orc distance=2'),
            ('source.game', 'INFO', 'Orc distance=3')
        )

    def test_orc_velocity(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'V'
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=3)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=1'),
            ('source.game', 'INFO', 'Orc velocity=2'),
            ('source.game', 'INFO', 'Orc velocity=3')
        )