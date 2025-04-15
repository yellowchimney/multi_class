from lib.diary_entry import DiaryEntry
from lib.diary import Diary

def test_adds_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry("13.04.2025", "Dear Diary, it was a wonderful day")
    diary.add(entry1)
    entry2 = DiaryEntry("14.04.2025", "OMG, it's Monday again")
    diary.add(entry2)

    assert len(diary.all()) == 2
    assert diary.all()[0].title == "13.04.2025"
    assert diary.all()[1].title == "14.04.2025"
    assert diary.all()[0].contents == "Dear Diary, it was a wonderful day"
    assert diary.all()[1].contents == "OMG, it's Monday again"


def test_word_counter_returns_number_of_words():
    diary = Diary()
   
    assert diary.count_words() == 0

    entry1 = DiaryEntry("13.04.2025", "Dear Diary, it was a wonderful day")
    diary.add(entry1)

    assert diary.count_words() == 8

    entry2 = DiaryEntry("14.04.2025", "OMG, it's Monday again")
    diary.add(entry2)

    assert diary.count_words() == 13

def test_reading_time_returns_number_of_minutes():
    diary = Diary()

    assert diary.reading_time(2) == 0

    entry1 = DiaryEntry("13.04.2025", "Dear Diary, it was a wonderful day")
    diary.add(entry1)
    entry2 = DiaryEntry("14.04.2025", "OMG, it's Monday again")
    diary.add(entry2)

    assert diary.reading_time(2) == 7


def test_best_entry_returns_closest_num_words():
    diary = Diary()
    entry1 = DiaryEntry("13.04.2025", "Dear Diary, it was a wonderful day")
    diary.add(entry1)
    entry2 = DiaryEntry("14.04.2025", "OMG, it's Monday again")
    diary.add(entry2)

    result = diary.find_best_entry_for_reading_time(2,3)
    
    assert result == entry2

    result2 = diary.find_best_entry_for_reading_time(2,5)

    assert result2 == entry1