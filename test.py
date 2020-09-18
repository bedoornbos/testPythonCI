import unittest

from Database import Album, DBTable

testAlbums1 = [
    Album(10, "The Dark Side of the Moon", 1973, "Pink Floyd"),
    Album(14, "Back in Black", 1980, "AC/DC"),
    Album(23, "Their Greatest Hits", 1976, "Eagles")]

testAlbums2 = [
    Album(37, "Falling into You", 1996, "Celine Dion"),
    Album(43, "Come Away With Me", 2002, "Norah Jones"),
    Album(55, "21", 2001, "Adele")]


class TestingDB(unittest.TestCase):
    test_db = DBTable(testAlbums1)

    def test_adding_albums1(self):
        self.assertEqual(testAlbums1, self.test_db.albums)

    def test_print(self):
        self.assertEqual("ID: 10 Title: The Dark Side of the Moon Release Year: 1973 Artist: Pink Floyd ",
                         self.test_db.print_row(0))


if __name__ == '__main__':
    unittest.main()