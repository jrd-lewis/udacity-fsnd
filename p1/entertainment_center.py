import fresh_tomatoes
import media

hunger_games = media.Movie("Hunger Games",
                           "Young kids are sent to fight to the death in an "
                           "arena",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/"
                           "HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo",
                           "2h 22m",
                           "PG-13")

force_awakens = media.Movie("Star Wars VII",
                            "The Force rekindles during a search for the "
                            "last of the Jedi",
                            "http://upload.wikimedia.org/wikipedia/en/a/a2/Star"
                            "_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                            "https://www.youtube.com/watch?v=OMOVFvcNfvE",
                            "2h 15m",
                            "PG-13")

the_hobbit = media.Movie("The Hobbit",
                         "The most unlikely creature goes on a journey",
                         "https://upload.wikimedia.org/wikipedia/en/b/b3/The_"
                         "Hobbit-_An_Unexpected_Journey.jpeg",
                         "https://www.youtube.com/watch?v=T90Holdcrps",
                         "3h 2m",
                         "PG-13")

princess_bride = media.Movie("The Princess Bride",
                             "A classic tale of true love, miracles, and "
                             "revenge",
                             "https://upload.wikimedia.org/wikipedia/en/d/db/"
                             "Princess_bride.jpg",
                             "https://www.youtube.com/watch?v=WNNUcHRiPS8",
                             "1h 38m",
                             "PG")

les_miserables = media.Movie("Les Miserables",
                             "An ex-convict's struggle to turn his life around",
                             "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                             "Les-miserables-movie-poster1.jpg",
                             "https://www.youtube.com/watch?v=IuEFm84s4oI",
                             "2h 40m",
                             "PG-13")

batman_begins = media.Movie("Batman Begins",
                            "Bruce Wayne dedicates himself to fight injustice "
                            "in Gotham",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/"
                            "Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=dYYRjVof6TU",
                            "2h 21m",
                            "PG-13")

fav_movies = [force_awakens, batman_begins, the_hobbit, princess_bride,
              hunger_games, les_miserables]
fresh_tomatoes.open_movies_page(fav_movies)
