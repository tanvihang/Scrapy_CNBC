# scrape Make It 
https://www.cnbc.com/make-it/

## Defining Items
| Calculated field | python expression  |
| ---------------- | ------------------ |
| images           | In images pipeline |
| location         | In geocoding pipeline |

| Housekeeping fields | python expression             |
| ------------------- | ----------------------------- |
| url                 | response.url                  |
| project             | self.settings.get('BOT_NAME') |
| spider              | self.name                     |
| server              | socket.gethostname()          |
| date                | datetime.datetime.now()       |

| News field | python expression                         |
| ---------- | ----------------------------------------- |
| Block      | //div[@data-test = 'ThreeUpCard']         |
| Title      | //a[contains(@class, 'title')]/text()     |
| Tag        | //a[contains(@class, 'eyebrow')]/text()   |
| Author     | string(//div[contains(@class, 'footer')]) |
| URL        | (.//a/@href)[1]                           |
| ImageURL   | (.//a)[1]/div/@style                      |
|            | ~~background-image:\s*url\("([^"]+)"\);~~     |
|            | background-image:url\((.*?)\)             |



