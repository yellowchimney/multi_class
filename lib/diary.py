from lib. diary_entry import DiaryEntry

class Diary():
    def __init__(self):
        self.entry_list = []
        self.word_counter = 0

    def add(self, entry):
        self.entry_list.append(entry)

    def all(self):
        return self.entry_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        self.word_counter = 0
        for entry in self.entry_list:
            self.word_counter += entry.count_words()
        return self.word_counter

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_words = self.count_words()
        if total_words:
            return int(total_words/wpm) + 1
        else:
            return 0

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        dict_of_all_suitable_entries = {}
        for entry in self.entry_list:
            # word_count_per_entry = entry.count_words()
            reading_time_per_entry = entry.reading_time(wpm)
            if reading_time_per_entry <= minutes:
                dict_of_all_suitable_entries[reading_time_per_entry] = entry
        best_entry = max(dict_of_all_suitable_entries.keys())
        return dict_of_all_suitable_entries[best_entry]

        


