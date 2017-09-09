import unittest
from movies import media


class TestMovie(unittest.TestCase):

    def test_get_instance_toy_story(self):
        title = "Toy Story"
        storyline = "Woody é um boneco cowboy de bom coração que pertence a um jovem chamado Andy. \n" \
                    "Porém vê sua posição como o brinquedo favorito de Andy comprometida quando seus pais \n" \
                    "lhe compram um outro brinquedo, o Buzz Lightyear, uma figura de ação. Ainda pior, Buzz \n" \
                    "é arrogante e acha que ele é um astronauta de verdade em uma missão para retornar ao seu \n" \
                    "planeta natal."
        poster_image_url = "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg"
        trailer_youtube_url = "https://youtu.be/KYz2wyBy3kc"
        toy_story = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)

        self.assertIsInstance(toy_story, media.Movie, msg="Is instance")

    def test_get_instance_avatar(self):
        title = "Avatar"
        storyline = "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser primitivos, \n" \
                    "mas são altamente evoluídos. Como o ambiente do planeta é tóxico, foram criados os avatares, \n" \
                    "corpos biológicos controlados pela mente humana que se movimentam livremente em Pandora. \n" \
                    "Jake Sully, um ex-fuzileiro naval paralítico, volta a andar através de um avatar e se apaixona \n" \
                    "por uma Na'vi. Esta paixão leva Jake a lutar pela sobrevivência de Pandora."
        poster_image_url = "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp"
        trailer_youtube_url = "https://youtu.be/d1_JBMrrYw8"

        avatar = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)

        self.assertIsInstance(avatar, media.Movie, msg="Is instance")
