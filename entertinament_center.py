# In order to use Movie class in the media module we have to import it first
from media import Movie 

# we need to import fresh_tomatoes 
import fresh_tomatoes as ft

# Create instances of the movie class 
toy_story=Movie("Toy Story",
	"Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcRKk8fPFSi83NmjO4hlth9VpXsqigxNXrG10hXum8ljJ_fZ07c1",
	"https://www.youtube.com/watch?v=rNk1Wi8SvNc"
	)


solo=Movie("Solo: A Star Wars Story",
"Young Han Solo finds adventure when he joins a gang of galactic smugglers, including a 196-year-old Wookie named Chewbacca. ",
"https://m.media-amazon.com/images/M/MV5BOTM2NTI3NTc3Nl5BMl5BanBnXkFtZTgwNzM1OTQyNTM@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=jPEYpryMp2s"
	)

avengers=Movie("Avengers: Infinity War",
"Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality.",
"http://t2.gstatic.com/images?q=tbn:ANd9GcQoBtRhueP0Kn_O7e89DXSBKBUz-1Nu4Ngb9eqFzqF3EbPGWYVP",
"https://www.youtube.com/watch?v=6ZfuNTqbHE8"
	)



deadpool2=Movie("Deadpool 2",

	"Wisecracking mercenary Deadpool meets Russell, an angry teenage mutant who lives at an orphanage. When Russell becomes the target of Cable -- a genetically enhanced soldier from the future -- Deadpool realizes that he'll need some help saving the boy from such a superior enemy.",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcTkbXNbwGV0npOKCGSndE-YCGpRb2xQDRV8VyMfGlsEfej-sVMv",
	"https://www.youtube.com/watch?v=D86RtevtfrA"

	)


jurassic=Movie("Jurassic World: Fallen Kingdom",

	"Three years after the destruction of the Jurassic World theme park, Owen Grady and Claire Dearing return to the island of Isla Nublar to save the remaining dinosaurs from a volcano that's about to erupt.",
	"http://t3.gstatic.com/images?q=tbn:ANd9GcR7nb6jKLhuTeSyO2CtELj-KQyYM6PxLwTtnKGCh74KSdJe9XWt",
	"https://www.youtube.com/watch?v=1FJD7jZqZEk",

	)

missionimp=Movie("Mission: Impossible Fallout",

	"Ethan Hunt and his IMF team find themselves in a race against time after a mission goes wrong.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcTDuzrnxIkh11AqI-6PrU9Qrycml22OhFHM9UwGmlkxCsPctLTr",
	"https://www.youtube.com/watch?v=wb49-oV0F78",
	)

rampage=Movie("Rampage",

	"Global icon Dwayne Johnson headlines the action adventure Rampage directed by Brad Peyton. Johnson stars as primatologist Davis Okoye, a man who keeps people at a distance but shares an unshakable bond with George.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcQpTCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ",
	"https://www.youtube.com/watch?v=coOKvrsmQiI",
	)

aquaman=Movie("Aquaman",

	"uaman finds himself caught between a surface world that ravages the sea and the underwater Atlanteans who are ready to revolt.",
	"https://cdn.images.express.co.uk/img/dynamic/36/590x/Aquaman-movie-trailer-news-918327.jpg",
	"https://www.youtube.com/watch?v=r9-DM9uBtVI",

	)

venom=Movie("Venom",

	"One of Marvels most enigmatic, complex and badass characters comes to the big screen, starring Academy Award nominated actor Tom Hardy as the lethal protector Venom.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcT1wbV7jcFXm3f8sKbZx_bruPB_w75w0FwBDLEA52DcbI2hRr3k",
	"https://www.youtube.com/watch?v=u9Mv98Gr5pY"
	)


# Python List for the above instances 
movies_list=[toy_story,solo,avengers,deadpool2,jurassic,missionimp,rampage,aquaman,venom]

# call to the open_movies_page function (which takes the movies_list as an argument) in the fres_tomatoes module
# This function is responsible to render movies with their name poster and trailer on an HTML page
ft.open_movies_page(movies_list)




