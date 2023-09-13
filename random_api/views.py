from rest_framework.views import APIView
from rest_framework.response import Response
import random

response = "TALENT PLUS"
quotes = {
    "1":"I won’t be impressed with technology until I can download food.",
    "2":"So, your kids must love the iPad?” I asked Mr. [Steve] Jobs, trying to change the subject. The company’s first tablet was just hitting the shelves. “They haven’t used it,” he told me. “We limit how much technology our kids use at home",
    "3":"The Internet is like alcohol in some sense. It accentuates what you would do anyway. If you want to be a loner, you can be more alone. If you want to connect, it makes it easier to connect. ― Esther Dyson",
    "4":"Technological progress has merely provided us with more efficient means for going backwards.― Aldous Huxley",
    "5":"Even the technology that promises to unite us, divides us. Each of us is now electronically connected to the globe, and yet we feel utterly alone. ― Dan Brown",
    "6":"Books don’t need batteries. ― Nadine Gordimer",
    "7":"We refuse to turn off our computers, turn off our phone, log off Facebook, and just sit in silence, because in those moments we might actually have to face up to who we really are. ― Jefferson Bethke",
    "8":"As cities grow and technology takes over the world, belief and imagination fade away and so do we.” ― Julie Kagawa",
    "9":"We’ve arranged a civilization in which most crucial elements profoundly depend on science and technology. We have also arranged things so that almost no one understands science and technology. This is a prescription for disaster. ― Carl Sagan",
    "10":"Technology has solved old economic problems by giving us new psychological problems. The internet has not just open-sourced information, it has also open-sourced insecurity, self-doubt, and shame. ― Mark Manson",
}
class GetTalent(APIView):
    def get(self, request):
        quote = random.randint(1,10)
        response = quotes[str(quote)]
        res = {
            "quote": response
        }

        return Response(res, status=200)