import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A young boy's favorite toys compete for first place in his heart.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
good_will = media.Movie("Good Will Hunting",
                        "A young genius from the wrong side of the tracks confronts his demons.",
                        "http://upload.wikimedia.org/wikipedia/fi/e/ed/Good_will_hunting_poster.jpg",
                        "https://www.youtube.com/watch?v=WDcMUCpppVs")
the_matrix = media.Movie("The Matrix",
                        "A regular guy discovers his daily life is an illusion, and must fight to save humanity from the force that keeps them captive.",
                        "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqUh")
dead_poets = media.Movie("Dead Poets Society",
                        "An unorthodox poetry teacher at a stern private boys academy stirs his students' hearts, and raises the ire of the academy's traditional faculty.",
                        "http://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
                        "www.youtube.com/watch?v=wrBk780aOis")
silver_linings = media.Movie("Silver Linings Playbook",
                        "A man suffering from depression teams up with an equally unstable woman to win a dance competition.",
                        "http://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",
                        "https://www.youtube.com/watch?v=Lj5_FhLaaQQ")
pearljam_twenty = media.Movie("Pearl Jam Twenty",
                        "Pearl Jam recounts their inigmatic 20-year musical career.",
                        "http://upload.wikimedia.org/wikipedia/en/b/be/Poster_of_Pearl_Jam_Twenty.jpg",
                        "https://www.youtube.com/watch?v=GzI8OhR0IVY")
before_sunrise = media.Movie("Before Sunrise",
                        "A young American touring Europe meets the love of his life on a train, and convinces her to spend the day with him in Vienna.",
                        "http://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                        "https://www.youtube.com/watch?v=9v6X-Dytlko")
movies = [toy_story, the_matrix, good_will, dead_poets, silver_linings,
        pearljam_twenty, before_sunrise]

fresh_tomatoes.open_movies_page(movies)
