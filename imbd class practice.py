import csv


class ETL:
    def __init__(self):
        self.csvfile = ''
        self.header = [['TitleType', 'Title', 'StartYear', 'RunTimeMins', 'Genres']]
        self.movies_shows = []
        self.movie_genres = []
        self.csv = []

    def extract(self):
        with open(self.csvfile) as file:
            readcsv = csv.reader(file, delimiter=',')
            next(readcsv)
            self.csv = list(readcsv)
            return self.csv

    def transform_movies_shows(self):
        for i in self.csv:
            if i[0] == 'movie' or i[0] == 'tvseries':
                self.movies_shows.append(i)
        return self.movies_shows

    def transform_secondary_genres(self):
        for i in self.movies_shows:
            i[7] = i[7].split(',', 1)[0]
        return self.movies_shows

    def transform_remove(self):
        for i in self.movies_shows:
            i.pop(5)
            i.pop(3)
            i.pop(2)
        return self.movies_shows

    def loading_csv(self, new_file_name):
        self.header.extend(self.movies_shows)
        with open(new_file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.header)


    def main(old_file_name, new_file_name):
        Example = ETL()
        Example.csvfile = old_file_name
        Example.extract()
        Example.transform_movies_shows()
        Example.transform_secondary_genres()
        Example.transform_remove()
        Example.loading_csv(new_file_name)


ETL.main('imdbtitles.csv', 'newimdb.csv')



