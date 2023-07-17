import scrapy


# Spider to collect tags top 1000 games from steam
class SteamSpider(scrapy.Spider):
    name = 'SteamSpider'

    url = 'https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s'
    page = 1
    start_urls = [url % page]

    parsed_games = 0

    # Function to jump on each game
    def parse(self, response):
        for link in response.css('#search_resultsRows a::attr(href)'):
            # We use cookies to go to 18+ games
            yield response.follow(link, callback=self.parse_tags, cookies={
                'birthtime': '943981201',
            })
        # Go to the next page if the number of games is less than 1000
        if self.parsed_games < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        # Avoiding Playsets
        if 'sub/' in response.url:
            return
        # If you have already parsed 1000 games, then finish
        if self.parsed_games == 1000:
            return

        self.parsed_games += 1

        yield {
            'appName': response.css('#appHubAppName::text').get(),
            'link': response.url.split('/?')[0],
            'tags': list(map(str.strip, response.css('a.app_tag::text').getall()))
        }
