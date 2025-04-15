class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.position = 0

    def count_words(self):
        word_list = self.title.split() + self.contents.split()
        return len(word_list)

    def reading_time(self, wpm):
        if self.count_words() == 0:
            return "No entries yet"
        else:    
            minutes = (self.count_words()//wpm) + 1
            return  minutes
        

    def reading_chunk(self, wpm, minutes):
        full_reading_time = self.reading_time(wpm)
        if minutes >= full_reading_time:
            return self.format()
        else:
            entry = self.format()
            word_list = entry.split()
            max_words_per_session = wpm * minutes
            start = self.position
            end = start + max_words_per_session

            if end < len(word_list):
                self.position = end
            else:
                self.position = 0

            chunk = " ".join(word_list[start:end])
        
            return chunk
