"""Tests for the !help gamename feature – rules class attributes and get_rules()."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from game import Game
from games.connect4 import Connect4Game
from games.snort import SnortGame
from games.hex import HexGame
from games.othello import OthelloGame
from games.gomoku import GomokuGame
from games.hextictactoe import HexTicTacToeGame
from games.grort import GrortGame


# ---------------------------------------------------------------------------
# game.py base-class: rules attribute and get_rules() classmethod
# ---------------------------------------------------------------------------

class TestBaseGameRules:
    def test_base_game_has_rules_attribute(self):
        """Base Game class has a 'rules' class attribute."""
        assert hasattr(Game, 'rules')

    def test_base_game_rules_default_is_empty_string(self):
        """Base Game.rules defaults to an empty string."""
        assert Game.rules == ""

    def test_get_rules_classmethod_exists(self):
        """Game exposes a get_rules() classmethod."""
        assert callable(getattr(Game, 'get_rules', None))

    def test_get_rules_returns_rules_attribute(self):
        """Game.get_rules() returns the value of cls.rules."""
        assert Game.get_rules() == Game.rules


# ---------------------------------------------------------------------------
# Each game class has a non-empty rules string
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("game_class", [
    Connect4Game,
    SnortGame,
    HexGame,
    OthelloGame,
    GomokuGame,
    HexTicTacToeGame,
    GrortGame,
])
class TestGameClassRules:
    def test_rules_attribute_is_non_empty_string(self, game_class):
        """Each concrete game class defines a non-empty rules string."""
        assert isinstance(game_class.rules, str)
        assert len(game_class.rules.strip()) > 0

    def test_get_rules_returns_non_empty_string(self, game_class):
        """get_rules() returns the same non-empty string as the class attribute."""
        assert game_class.get_rules() == game_class.rules
        assert len(game_class.get_rules().strip()) > 0

    def test_get_rules_inherited_from_game(self, game_class):
        """get_rules() resolves to the subclass rules, not the base class empty string."""
        assert game_class.get_rules() != Game.get_rules()
