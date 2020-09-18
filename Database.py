import string
from dataclasses import dataclass

from typing import List


@dataclass
class Album:
    id: int
    title: string
    year: int
    artist: string


@dataclass
class DBTable:
    albums: List[Album]

    def print_row(self, row):
        if len(self.albums) >= row >= 0:
            album = self.albums[row]
            return "ID: %d Title: %s Release Year: %d Artist: %s " \
                % (album.id, album.title, album.year, album.artist)



