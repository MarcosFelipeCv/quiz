import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    

def test_add_multiple_choices():
    q = Question(title="q1")
    q.add_choice("a")
    q.add_choice("b")
    assert len(q.choices) == 2
    
def test_remove_choice():
    q = Question(title="q1")
    choice = q.add_choice("a")
    q.remove_choice_by_id(choice.id)
    assert len(q.choices) == 0

def test_remove_invalid_choice():
    q = Question(title="q1")
    with pytest.raises(Exception):
        q.remove_choice_by_id(999)  # id invalido

def test_select_correct_choices():
    q = Question(title="q1")
    q.add_choice("a", True)
    q.add_choice("b", False)
    correct_ids = q.select_choices([1])
    assert correct_ids == [1]


def test_exceed_max_selections():
    q = Question(title="q1", max_selections=1)
    q.add_choice("a", True)
    with pytest.raises(Exception):
        q.select_choices([1, 2])
        
def test_set_correct_choices():
    q = Question(title="q1")
    q.add_choice("a")
    q.set_correct_choices([1])
    assert q.choices[0].is_correct


def test_clear_all_choices():
    q = Question(title="q1")
    q.add_choice("a")
    q.remove_all_choices()
    assert len(q.choices) == 0


def test_reject_invalid_choice_text():
    q = Question(title="q1")
    with pytest.raises(Exception):
        q.add_choice("")
    with pytest.raises(Exception):
        q.add_choice("a" * 101)


def test_auto_increment_choice_ids():
    q = Question(title="q1")
    choice1 = q.add_choice("a")
    choice2 = q.add_choice("b")
    assert choice1.id == 1 and choice2.id == 2


def test_filter_correct_choices():
    q = Question(title="q1")
    q.add_choice("a", True)
    q.add_choice("b", False)
    correct_ids = q._correct_choice_ids() 
    assert correct_ids == [1]
