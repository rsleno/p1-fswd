import fresh_tomatoes
import media

mov = []

# Movie data from filmaffinity.com
movie_data = [
{"title": "Star Wars. Episode V", "year": "1980" , "synopsis": "The Empire Strikes Back - Three years later Imperial forces continue to pursue the Rebels. After the Rebellion's defeat on the ice planet Hoth, Luke journeys to the planet Dagobah to train with Jedi Master Yoda, who has lived in hiding since the fall of the Republic. In an attempt to convert Luke to the dark side, Darth Vader lures young Skywalker into a trap in the Cloud City of Bespin. In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...", "poster_image_url": "http://pics.filmaffinity.com/Star_Wars_Episode_V_The_Empire_Strikes_Back-314829878-large.jpg", "trailer_youtube_url": "https://youtu.be/8Hm-9Sai9To", "score": 8.1},
{"title": "Clerks", "year": "1994" , "synopsis": "Dante Hicks is a clerk at a local convenience store in New Jersey. On one particular Saturday morning, he gets called in on his day off. Once there, he must deal with multiple problems. The shutters outside won't open. His ex-girlfriend, whom he is still in love with, is getting married. His girlfriend, who bugs him about starting college, has revealed certain, uh...stuff about her past. His boss hasn't come in to take his place. He has a hockey game at 2 o'clock. Another ex has died, and today's the last day he can go to her wake. He must deal with customers that aren't so intelligent. His friend, Randal, a clerk at the video store next door, is even less dedicated to his job than Dante, and is always bothering Dante's customers. And the biggest problem of them all: HE'S NOT EVEN SUPPOSED TO BE THERE TODAY!! Can Dante manage it all?", "poster_image_url": "http://pics.filmaffinity.com/Clerks-456270250-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=Mlfn5n-E2WE", "score": 7.4},
{"title": "Reservoir Dogs", "year": "1992" , "synopsis": "Critically acclaimed for its raw power and breathtaking ferocity, it's the brillant American gangster movie clasic from writer-director Quentin Tarantino. They were perfect strangers, assembled to pull off the perfect crime. Then their simple robbery explodes into a bloody ambush, and the ruthless killers realize one of them is a police informer. But which one?", "poster_image_url": "http://pics.filmaffinity.com/Reservoir_Dogs-904905830-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=GLPJSmUHZvU", "score": 8.2},
{"title": "The Lord of the Rings", "year": "2001" , "synopsis": "One ring to rule them all, One ring to find them. One ring to bring them all and in the darkness bind them. In this part of the trilogy, the young Hobbit Frodo Baggins inherits a ring; but this ring is no mere trinket. It is the One Ring, an instrument of absolute power that could allow Sauron, the dark Lord of Mordor, to rule Middle-earth and enslave its peoples. Frodo, together with a Fellowship that includes his loyal Hobbit friends, Humans, a Wizard, a Dwarf and an Elf, must take the One Ring across Middle-earth to Mount Doom, where it first was forged, and destroy it forever. Such a journey means venturing deep into territory manned by Sauron, where he is amassing his army of Orcs. And it is not only external evils that the Fellowship must combat, but also internal dissension and the corrupting influence of the One Ring itself. The course of future history is entwined with the fate of the Fellowship.", "poster_image_url": "http://pics.filmaffinity.com/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring-876628736-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=aStYWD25fAQ", "score": 8.0},
{"title": "Snatch", "year": "2000" , "synopsis": "Turkish, an unlicenced boxing promoter is pulled into trouble when he becomes involved in big time criminal Brick Top, who wants him to arrange a fight and fix it. Meanwhile, a diamond theft goes down but the 84 karat stone goes missing. This leads Avi, the boss who was supposed to receive the stone, to come to England to search for it, with the help of his cousin, Doug The Head and Bullet Tooth Tony. As events twist and turn, the two situations blend into one with a chain reaction of events carrying on for each and every character.", "poster_image_url": "http://pics.filmaffinity.com/Snatch-188547491-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=lUloT3Dh3-E", "score": 7.9},
{"title": "Birdman", "year": "2014", "synopsis": "A washed up actor who once played an iconic superhero must overcome his ego and family trouble as he prepares to mount a Broadway play in a bid to reclaim past glory. Movie star Riggan Thomson (Michael Keaton), who became famous for playing iconic superhero Birdman in three successful installments but turned down a fourth one, has decided to stage a comeback by writing, directing and starring in a Broadway play. Pressures mount leading up to the play's opening night. The day before the first preview of the play, he realizes he has to replace one of the actors, who is not up to the job. However, his replacement (Edward Norton), though famous and talented, comes with troubles of his own. Meanwhile, Riggan feels guilt about being a neglectful father to his daughter (Emma Stone), who's now working as his assistant. He also desperately wants the top critic in New York, who could make or break his play, to write a positive review, but he's worried the entire production will be a bust.", "poster_image_url": "http://pics.filmaffinity.com/Birdman-594952048-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=xIxMMv_LD5Q", "score": 7.2},
{"title": "Interstellar", "year": "2014", "synopsis": "In the near future Earth has been devastated by drought and famine, causing a scarcity in food and extreme changes in climate. When humanity is facing extinction, a mysterious rip in the space-time continuum is discovered, giving mankind the opportunity to widen their lifespan. A group of explorers must travel beyond our solar system in search of a planet that can sustain life. The crew of the Endurance are required to think bigger and go further than any human in history as they embark on an interstellar voyage, into the unknown. However, through the wormhole, one hour is the equivalent of seven years back on Earth, so the mission won't work if the people on Earth are dead by the time they pull it off. And Coop, the pilot of the Endurance, must decide between seeing his children again and the future of the human race.", "poster_image_url": "http://pics.filmaffinity.com/Interstellar-366875261-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=zSWdZVtXT7E", "score": 7.8},
{"title": "The Godfather", "year": "1972", "synopsis": "Epic tale of a 1940s New York Mafia family and their struggle to protect their empire from rival families as the leadership switches from the father (Marlon Brando) to his youngest son (Al Pacino). Vito Corleone (Marlon Brando) is The Godfather, the Don (head) of a successful, tightly-knit family whose business is organized crime. Heir apparent is impulsive, hot-tempered Sonny (James Caan), whose brothers are brooding Michael (Al Pacino), who tries to seperate himself from his criminal family, and Fredo (John Cazale), who can't seem to do anything right. Vito has also adopted level-headed Tom Hagan (Robert Duvall), now the family lawyer. Vito's refusal to enter the lucrative drug rackets puts him in a war between the mafia families. Michael gets his hand dirty by taking revenge on the family's behalf, and then taking over as the new calculating, ruthless godfather. In his new role he plots to make the Corleones the leading players in Las Vegas casino industry while arranging for the war in New York City to be settled for once and for all.", "poster_image_url": "http://pics.filmaffinity.com/The_Godfather-485345341-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=1aV9X2d-f5g", "score": 9.1}
]

# Create movie objects from movie_data and append to a list.
for m in movie_data:
	mov.append(media.Movie(m))

fresh_tomatoes.open_movies_page(mov)