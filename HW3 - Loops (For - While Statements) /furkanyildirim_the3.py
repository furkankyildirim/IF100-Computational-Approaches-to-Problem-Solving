
moviesInput = input('Please enter movie names and remaining quota: ')
moviesList = moviesInput.split(',')

moviesDetail = {}
for i in moviesList:
    movie = i.split(':')
    movie[1] = int(movie[1])

    if movie[0] in moviesDetail:
        moviesDetail[movie[0]][0] += movie[1]
    else:
        moviesDetail[movie[0]] = [movie[1],movie[2]]

requested_movie = input('Please enter the movie you want to watch: ')

if requested_movie in moviesDetail:
    ticketsNumber = int(input('Please enter the number of tickets you want to buy: '))

    if ticketsNumber <= moviesDetail[requested_movie][0]:
        print('The reservation is done!')
    else:
        movie_genre = moviesDetail[requested_movie][1]
        genreList = []
        for i in moviesDetail.items():
            if ticketsNumber <= i[1][0] and i[1][1] == movie_genre:
                genreList.append(i[0])
            else:
                pass
        if len(genreList) != 0:
            print('There are not enough seats for {}! But you can watch one of the following movies from the genre {}:'.format(requested_movie,movie_genre))
            genreList.sort()
            seq = 0
            while seq < len(genreList):
                print('*',genreList[seq])
                seq += 1
        else:
            print('There are not enough seats for {} and any other movie with the genre {}!'.format(requested_movie,movie_genre))

else:
    print('There is no such movie in the theater.')