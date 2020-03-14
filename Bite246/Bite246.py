import pytest

from Bite246.tests import print_workout_days

WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}


def test_print_workout_days_lower(capsys):
    print_workout_days('lower', WORKOUTS)
    captured = capsys.readouterr()
    assert captured.out == 'Tue, Fri\n'


def test_print_workout_days_upper(capsys):
    print_workout_days('upper', WORKOUTS)
    captured = capsys.readouterr()
    assert captured.out == 'Mon, Thu\n'


def test_print_workout_days_cardio(capsys):
    print_workout_days('cardio', WORKOUTS)
    captured = capsys.readouterr()
    assert captured.out == 'Wed\n'


def test_print_workout_days_no_matching(capsys):
    print_workout_days('arms', WORKOUTS)
    captured = capsys.readouterr()
    assert captured.out == 'No matching workout\n'