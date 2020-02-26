# write a class, name it "Song"
class Song(object):
    # call function "__init__", (self)
    def __init__(self, lyrics):
        # assign fucntion self. lyrics to variable "lyrics"
        self.lyrics = lyrics
        # call function sing_me_a_song (self)
    def sing_me_a_song(self):
        # assign all the elements in "self.lyrics" to variable "line"
        for line in self.lyrics:
            print(line)
# object is a list of ["happy birthday to you", "I don' want to ", ect.]
# Song ([])
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally aroung tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
