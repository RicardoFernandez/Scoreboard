import pytest

from scoreboard.Scoreboard import Scoreboard


def test_scoreboard_validInitialitation():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.__str__() == "000:000"


def test_scoreboard_validLocalScoreboard():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.get_local_score() == "000"


def test_scoreboard_validVisitorScoreboard():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.get_visitor_score() == "000"


# region mantengo los test para documentar el proceso seguido
def test_scoreboard_scoreLocalForOne():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_one_for_local() == "001"


def test_scoreboard_scoreLocalForTwo():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_two_for_local() == "002"


def test_scoreboard_scoreLocalForthree():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_three_for_local() == "003"


def test_scoreboard_scoreVisitorForOne():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_one_for_visitor() == "001"


def test_scoreboard_scoreVisitorForTwo():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_two_for_visitor() == "002"


def test_scoreboard_scoreVisitorForthree():
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score_three_for_visitor() == "003"


# endregion


@pytest.mark.parametrize("scorer,points,result",
                         [("local", 2, "002:000"), ("visitor", 1, "000:001"), ("local", 3, "003:000")])
def test_scoreboard_updateToCorrectScore(scorer, points, result):
    new_scoreboard = Scoreboard()
    assert new_scoreboard.score(scorer, points) == result
