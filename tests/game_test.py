"""
Test for source.game
"""
from source.orc import (Orc, StrongOrc, UglyOrc, StinkyOrc, GiantOrc, WeakOrc, ZombieOrc,
                        ArmoredOrc, FastOrc)
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
        Orc.orc_id = 0

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
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 MI/HR and distance=0 MI'),
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
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 MI/HR and distance=1 MI')
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
            ('source.orc', 'INFO', 'Orc #1 created')
        )

    def test_alert_issue_kingdom_class(self):
        with LogCapture() as l:
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.start()
            test_game._Game__kingdom.add_orc(orcs=[Orc(distance=0, velocity=0)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=0 MI/HR and distance=0 MI')
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
            ('source.game', 'INFO', 'Orc distance=1 MI'),
            ('source.game', 'INFO', 'Orc distance=2 MI'),
            ('source.game', 'INFO', 'Orc distance=3 MI')
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
            ('source.game', 'INFO', 'Orc velocity=1 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=2 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=3 MI/HR')
        )

    def test_command_display(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: '?'
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Command: P Desc: Check Perimeter'),
            ('source.game', 'INFO', 'Command: X Desc: Stop Game'),
            ('source.game', 'INFO', 'Command: D Desc: Display Orc Distance'),
            ('source.game', 'INFO', 'Command: V Desc: Display Orc Velocity'),
            ('source.game', 'INFO', 'Command: T Desc: Display Orc Types'),
            ('source.game', 'INFO', 'Command: R Desc: Remove Orc By ID'),
            ('source.game', 'INFO', 'Command: U Desc: Set Units'),
            ('source.game', 'INFO', 'Command: PR [ID] [Priority] Desc: Sets orc with [ID] to [Priority]'),
            ('source.game', 'INFO', 'Command: OD [ID] Desc: Shows orc details'),
            ('source.game', 'INFO', 'Command: G Desc: Generates a list of 5 random orcs'),
            ('source.game', 'INFO', 'Command: ENTer the Trees Desc: Clears all orcs from game'),
            ('source.game', 'INFO', 'Command: ? Desc: Display Commands')
        )

    def test_test_orc_velocity(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'V'
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=0, velocity=1)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=1 MI/HR')
        )

    def test_orc_types(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'T'
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc type: Strong'),
            ('source.game', 'INFO', 'Orc type: Ugly'),
            ('source.game', 'INFO', 'Orc type: Stinky'),
            ('source.game', 'INFO', 'Orc type: Giant'),
            ('source.game', 'INFO', 'Orc type: Weak'),
            ('source.game', 'INFO', 'Orc type: Zombie'),
            ('source.game', 'INFO', 'Orc type: Armored'),
            ('source.game', 'INFO', 'Orc type: Fast'),
        )

    def test_orc_remove_valid_id(self):
        num_orcs = 8
        num_orcs_after = 7
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 1
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])
            self.assertEqual(num_orcs, len(test_game._Game__kingdom.orcs),
                             'There should have been 8 orcs')
            test_game.remove_orc()
            self.assertEqual(num_orcs_after, len(test_game._Game__kingdom.orcs),
                             'There should have been 7 orcs')

        l.check(
            ('source.game', 'INFO', 'Orc 1 was removed')
        )

    def test_orc_remove_invalid_id(self):
        num_orcs = 8
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 0
            test_game = Game()
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])
            self.assertEqual(num_orcs, len(test_game._Game__kingdom.orcs),
                             'There should have been 8 orcs')
            test_game.remove_orc()
            self.assertEqual(num_orcs, len(test_game._Game__kingdom.orcs),
                             'There should still be 8 orcs')

        l.check(
            ('source.game', 'WARNING', 'Orc ID 0 is an invalid ID')
        )

    def test_units_orc_creation_imperial(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Imperial'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 MI/HR and distance=1 MI'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=20 MI/HR and distance=1 MI')
        )

    def test_units_orc_creation_metric(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Metric'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 KM/HR and distance=1 KM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=20 KM/HR and distance=1 KM')
        )

    def test_units_orc_creation_parsec(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Parsec'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 PS/HR and distance=1 PS'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=20 PS/HR and distance=1 PS')
        )

    def test_units_orc_creation_nautical(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Nautical'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=1, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=1, velocity=20)])

        l.check(
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=1 NM/HR and distance=1 NM'),
            ('source.kingdom', 'INFO', 'Orc spotted with velocity=20 NM/HR and distance=1 NM')
        )

    def test_units_display_orc_distance_imperial(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Imperial'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'D'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc distance=1 MI'),
            ('source.game', 'INFO', 'Orc distance=2 MI'),
            ('source.game', 'INFO', 'Orc distance=3 MI'),
            ('source.game', 'INFO', 'Orc distance=4 MI'),
            ('source.game', 'INFO', 'Orc distance=5 MI'),
            ('source.game', 'INFO', 'Orc distance=6 MI'),
            ('source.game', 'INFO', 'Orc distance=7 MI'),
            ('source.game', 'INFO', 'Orc distance=8 MI')
        )

    def test_units_display_orc_distance_metric(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Metric'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'D'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc distance=1 KM'),
            ('source.game', 'INFO', 'Orc distance=2 KM'),
            ('source.game', 'INFO', 'Orc distance=3 KM'),
            ('source.game', 'INFO', 'Orc distance=4 KM'),
            ('source.game', 'INFO', 'Orc distance=5 KM'),
            ('source.game', 'INFO', 'Orc distance=6 KM'),
            ('source.game', 'INFO', 'Orc distance=7 KM'),
            ('source.game', 'INFO', 'Orc distance=8 KM')
        )

    def test_units_display_orc_distance_parsec(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Parsec'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'D'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc distance=1 PS'),
            ('source.game', 'INFO', 'Orc distance=2 PS'),
            ('source.game', 'INFO', 'Orc distance=3 PS'),
            ('source.game', 'INFO', 'Orc distance=4 PS'),
            ('source.game', 'INFO', 'Orc distance=5 PS'),
            ('source.game', 'INFO', 'Orc distance=6 PS'),
            ('source.game', 'INFO', 'Orc distance=7 PS'),
            ('source.game', 'INFO', 'Orc distance=8 PS')
        )

    def test_units_display_orc_distance_nautical(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Nautical'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'D'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc distance=1 NM'),
            ('source.game', 'INFO', 'Orc distance=2 NM'),
            ('source.game', 'INFO', 'Orc distance=3 NM'),
            ('source.game', 'INFO', 'Orc distance=4 NM'),
            ('source.game', 'INFO', 'Orc distance=5 NM'),
            ('source.game', 'INFO', 'Orc distance=6 NM'),
            ('source.game', 'INFO', 'Orc distance=7 NM'),
            ('source.game', 'INFO', 'Orc distance=8 NM')
        )

    def test_units_display_orc_velocity_imperial(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Imperial'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'V'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=7 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=6 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=5 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=4 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=3 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=2 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=1 MI/HR'),
            ('source.game', 'INFO', 'Orc velocity=20 MI/HR'),
        )

    def test_units_display_orc_velocity_metric(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Metric'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'V'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=7 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=6 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=5 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=4 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=3 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=2 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=1 KM/HR'),
            ('source.game', 'INFO', 'Orc velocity=20 KM/HR'),
        )

    def test_units_display_orc_velocity_parsec(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Parsec'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'V'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=7 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=6 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=5 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=4 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=3 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=2 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=1 PS/HR'),
            ('source.game', 'INFO', 'Orc velocity=20 PS/HR'),
        )

    def test_units_display_orc_velocity_nautical(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'Nautical'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game._Game__kingdom.add_orc(orcs=[UglyOrc(distance=2, velocity=6)])
            test_game._Game__kingdom.add_orc(orcs=[StinkyOrc(distance=3, velocity=5)])
            test_game._Game__kingdom.add_orc(orcs=[GiantOrc(distance=4, velocity=4)])
            test_game._Game__kingdom.add_orc(orcs=[WeakOrc(distance=5, velocity=3)])
            test_game._Game__kingdom.add_orc(orcs=[ZombieOrc(distance=6, velocity=2)])
            test_game._Game__kingdom.add_orc(orcs=[ArmoredOrc(distance=7, velocity=1)])
            test_game._Game__kingdom.add_orc(orcs=[FastOrc(distance=8, velocity=20)])
            __builtin__.raw_input = lambda _: 'V'
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc velocity=7 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=6 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=5 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=4 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=3 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=2 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=1 NM/HR'),
            ('source.game', 'INFO', 'Orc velocity=20 NM/HR'),
        )

    def test_units_invalid_unit(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'LightYears'
            test_game = Game()
            test_game.set_units()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)

        l.check(
            ('source.game', 'WARNING', 'Invalid units entered')
        )

    def test_priority_HIGH_orc(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'PR 1 HIGH'
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game.handle_command()

        l.check(
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.orc', 'INFO', 'Orc 1 priority set to HIGH')
        )

        self.assertEqual(test_game._Game__kingdom.orcs[0].priority, 'HIGH',
                         'Priority should have been changed to HIGH')

    def test_priority_MEDIUM_orc(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'PR 1 MEDIUM'
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game.handle_command()

        l.check(
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.orc', 'INFO', 'Orc 1 priority set to MEDIUM')
        )

        self.assertEqual(test_game._Game__kingdom.orcs[0].priority, 'MEDIUM',
                         'Priority should have been changed to MEDIUM')

    def test_priority_LOW_orc(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'PR 1 LOW'
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game.handle_command()

        l.check(
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.orc', 'INFO', 'Orc 1 priority set to LOW')
        )

        self.assertEqual(test_game._Game__kingdom.orcs[0].priority, 'LOW',
                         'Priority should have been changed to LOW')

    def test_priority_invalid_priority(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'PR 1 CUSTOM'
            test_game = Game()
            test_game.set_alert_level(module='source.game', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            original_priority = test_game._Game__kingdom.orcs[0].priority
            test_game.handle_command()

        l.check(
            ('source.orc', 'INFO', 'Orc #1 created'),
            ('source.orc', 'WARNING', 'Invalid orc priority')
        )

        self.assertEqual(original_priority, test_game._Game__kingdom.orcs[0].priority,
                         'Priority should not have changed')

    def test_priority_invalid_command(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'PR 1'
            test_game = Game()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.handle_command()

        l.check(
            ('source.game', 'WARNING', 'Invalid priority command')
        )

    def test_show_orc_details(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'OD 1'
            test_game = Game()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game.handle_command()

        l.check(
            ('source.game', 'INFO', 'Orc ID: 1'),
            ('source.game', 'INFO', 'Orc Type: Strong'),
            ('source.game', 'INFO', 'Orc Distance: 1 MI'),
            ('source.game', 'INFO', 'Orc Velocity: 7 MI/HR'),
            ('source.game', 'INFO', 'Orc Priority: LOW')
        )

    def test_show_orc_details_invalid_id(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'OD 3'
            test_game = Game()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game._Game__kingdom.add_orc(orcs=[StrongOrc(distance=1, velocity=7)])
            test_game.handle_command()

        l.check(
            ('source.game', 'WARNING', 'Orc ID 3 is an invalid ID')
        )

    def test_show_orc_details_invalid_detail_command(self):
        with LogCapture() as l:
            __builtin__.raw_input = lambda _: 'OD'
            test_game = Game()
            test_game.set_alert_level(module='source.orc', level=logging.WARNING)
            test_game.set_alert_level(module='source.kingdom', level=logging.WARNING)
            test_game.handle_command()

        l.check(
            ('source.game', 'WARNING', 'Invalid detail command')
        )

    def test_generate_orcs(self):
        __builtin__.raw_input = lambda _: 'G'
        test_game = Game()
        test_game.handle_command()

        self.assertEqual(len(test_game._Game__kingdom.orcs), 5)

    def test_enter_trees(self):
        __builtin__.raw_input = lambda _: 'G'
        test_game = Game()
        test_game.handle_command()

        self.assertEqual(len(test_game._Game__kingdom.orcs), 5)

        __builtin__.raw_input = lambda _: 'ENTer the Trees'
        test_game.handle_command()

        self.assertEqual(len(test_game._Game__kingdom.orcs), 0)