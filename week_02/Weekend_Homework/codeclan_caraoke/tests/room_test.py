import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room = Room("pro_room", 2)

        self.guest1 = Guest("bob", "starman", 25.5)
        self.guest2 = Guest("steve", "starman", 47.5)
        self.guest3 = Guest("dave", "another one bites the dust", 20)

        # self.guest_list = [self.guest1, self.guest2]

        self.song1 = Song("another one bites the dust", "queen", 3.35)
        self.song2 = Song("beat it", "michael jackson", 4.19)
        self.song3 = Song("starman", "david bowie", 4.14)

    # @unittest.skip
    def test_add_guest(self):
        self.room.add_guest(self.guest3)
        self.assertEqual(1, len(self.room.guest_list))


    # @unittest.skip
    def test_can_remove_guest(self):
        self.room.add_guest(self.guest1)
        self.room.remove_guest(self.guest1)
        self.assertEqual(0, len(self.room.guest_list))


    # @unittest.skip
    def test_cannot_add_guest_if_over_capacity(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.assertEqual(2, len(self.room.guest_list))


    # @unittest.skip
    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song1)
        self.assertEqual(1, len(self.room.playlist))
    

    # @unittest.skip
    def test_clear_playlist(self):
        self.room.add_song_to_playlist(self.song1)
        self.room.add_song_to_playlist(self.song2)
        self.room.clear_playlist()
        self.assertEqual(0, len(self.room.playlist))

