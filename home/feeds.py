from django.contrib.syndication.views import Feed
from pants.home.models import *

class LatestFeed(Feed):
    title = "Pants or no pants Feeds you"
    link = "/"
    description = "New pants or no pants posts"

    def items(self):
        return Dude.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        link = "<a href=\"http://www.pantsornopants.com\">"
        img = "<img src=\"http://www.pantsornopants.com/media/images/%s_undies.png\"/>" % item.name
        return "%s%s</a>" % (link, img)

    def item_link(self, item):
        return "http://www.pantsornopants.com"
