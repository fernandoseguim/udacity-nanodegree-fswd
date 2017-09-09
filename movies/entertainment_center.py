from movies import media, fresh_tomatoes

logan_movie = media.Movie(title="Logan",
                          storyline="In 2029 the mutant population has shrunken significantly and the X-Men have disbanded. Logan, whose power to self-heal is dwindling, has surrendered himself to alcohol and now earns a living as a chauffeur.",
                          poster_image_url="http://t0.gstatic.com/images?q=tbn:ANd9GcR_k0ShtzP-2rhzHtF30v9DiH0bgSogYU99juiiDna_oQEgo2dx",
                          trailer_youtube_url="https://youtu.be/RWSuAC9CYxo")

wonderwoman_movie = media.Movie(title="Wonder Woman",
                                storyline="Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, when a pilot crashes on their shores and tells of a massive conflict raging in the outside world, Diana leaves her home, convinced she can stop the threat. Fighting alongside man in a war to end all wars, Diana will discover her full powers and her true destiny",
                                poster_image_url="http://t1.gstatic.com/images?q=tbn:ANd9GcRyCdWToNKN9fqnTc58XbMF7XC6ryMq-BHICs0aq5_0SFYoK0h3",
                                trailer_youtube_url="https://youtu.be/VSB4wGIdDwo")

guardiansofgalaxy2_movie = media.Movie(title="Guardians of the Galaxy 2",
                                storyline="n 2014, Peter Quill, Gamora, Drax, Rocket, and Baby Groot are renowned as the Guardians of the Galaxy. Ayesha, leader of the Sovereign race, has the Guardians protect valuable batteries from an inter-dimensional monster in exchange for Gamora's estranged sister Nebula, who was caught attempting to steal the batteries. After Rocket steals some for himself, the Sovereign attacks the Guardians' ship with a fleet of drones. The drones are destroyed by a mysterious figure, but the Guardians crash-land on a nearby planet. The figure reveals himself as Quill's father, Ego. He invites Quill, Gamora, and Drax to his home planet, while Rocket and Groot remain behind to repair the ship and guard Nebula.",
                                poster_image_url="http://t0.gstatic.com/images?q=tbn:ANd9GcT3jhaTLkrcaiAxYv7EamUq2R--8wK4l6wH9UwQi97iYwaYn4Zm",
                                trailer_youtube_url="https://youtu.be/dW1BIid8Osg")


thorragnarok_movie = media.Movie(title="Thor Ragnarok",
                                storyline="Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally. Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.",
                                poster_image_url="http://t1.gstatic.com/images?q=tbn:ANd9GcQAmMN0WnVLHXIKsFbj7dp7-HTUmyQ_d46RruMyj7Tv33mqXy7i",
                                trailer_youtube_url="https://youtu.be/UvNnqWLruXA")


movies = [logan_movie, wonderwoman_movie, guardiansofgalaxy2_movie, thorragnarok_movie]
fresh_tomatoes.open_movies_page(movies=movies)
