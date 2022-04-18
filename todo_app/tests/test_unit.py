import pytest
from todo_app.data.trello_items import *
from view_model import view_model

@pytest.fixture
def board_prep(): 
    to_do_item = Item("1", "To Do Title", "To Do", "To Do Description")
    in_progress_item = Item("2", "In Progress Title", "In Progress", "In Progress Description")
    done_item = Item("3", "Done Title", "Done", "Done Description")
    test_items = [to_do_item, in_progress_item, done_item]
    return view_model(test_items)

def test_pytest(): 
    assert(True)

def test_not_started(board_prep):
    assert len(board_prep.to_do) == 1
    assert board_prep.to_do[0].title == "To Do Title"
    assert board_prep.to_do[0].status == "To Do"

def test_done(board_prep):
    assert len(board_prep.complete) == 1
    assert board_prep.complete[0].title == "Done Title"
    assert board_prep.complete[0].status == "Done"  

def test_doing(board_prep):
    assert len(board_prep.in_progress) == 1
    assert board_prep.in_progress[0].title == "In Progress Title"
    assert board_prep.in_progress[0].status == "In Progress"