# -*- coding: cp1252 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtu.be/XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille ",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://youtu.be/c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://youtu.be/FAfR8omt-CY")


movies = [toy_story, avatar, school_of_rock, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)
