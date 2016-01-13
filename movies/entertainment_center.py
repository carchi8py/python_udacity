import media

toy_story = media.Movie("Toy Story", 
						"A Story of a boy and his toys that come to life",
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)
avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"http://cafmp.com/wp-content/uploads/2012/11/avatar.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")
print avatar.storyline
avatar.show_trailer()