
class VideoGame:

    def __init__(self, rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales, v):
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_sales = na_sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales
        self.v = v

    def get_rank(self):
        return self.rank

    @staticmethod
    def video_game_decoder(obj):
        return VideoGame(obj['rank'], obj['name'], obj['platform'], obj['year'], obj['genre'], obj['publisher'], obj['naSales'], obj['euSales'], obj['jpSales'],obj['otherSales'],obj['globalSales'],obj['__v'])