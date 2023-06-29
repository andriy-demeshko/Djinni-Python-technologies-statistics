import scrapy
from scrapy.http import Response

from djinni_statistics.items import DjinniStatisticsItem


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        vacancies_urls = response.css("a.profile::attr(href)").getall()

        for vacancy_url in vacancies_urls:
            yield response.follow(url=vacancy_url, callback=self.parse_vacancy)

        next_page = response.css("li:last-child > a.page-link::attr(href)").get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

    @staticmethod
    def parse_vacancy(response: Response):
        title = response.css("h1::text").get().strip().replace("\xa0", " ")

        technologies_raw = response.css(
            ".job-additional-info--item:nth-child(2) > div > span::text"
        ).getall()
        print(technologies_raw)

        technologies = [technology.replace("/", ",") for technology in technologies_raw]
        print(technologies)

        experience = response.css(
            ".job-additional-info--item:last-child > div::text"
        ).get().strip().split()[0]

        if experience.isdigit():
            experience = int(experience)
        else:
            experience = 0

        date = response.css("p.text-muted").re(r"\d+\s+\w+\s+\d+")[0]

        views = int(response.css("p.text-muted").re(r"(\d+) перегляд")[0])

        applications = int(response.css("p.text-muted").re(r"(\d+) відгук")[0])

        yield DjinniStatisticsItem(
            title=title,
            technologies=technologies,
            experience=experience,
            date=date,
            views=views,
            applications=applications
        )
