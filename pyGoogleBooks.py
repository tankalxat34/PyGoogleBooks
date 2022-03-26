"""
********************************
*------------------------------*
*--------PyGoogleBooks---------*
*------------------------------*
********************************
Author: tankalxat34
Description: 
    Python package for convenient work with Google Books service
Important links:
    

"""

import requests, re

USER_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
}


class InvalidPageToPublicView(Exception):
    def __init__(self):
        super().__init__("This page is unavailable, or incorrect cookies are set")


class BookWithoutAuthors(Exception):
    def __init__(self):
        super().__init__("This book doesn't have any authors")


class GoogleBook:
    def __init__(self, id,
                 lpg="PP1",
                 pg="PA0",
                 hl="ru",
                 jscmd="click3",
                 cookies="NID=511=cF7Xznuqv-ETmVsBfjWsET4b4iUwu4jaOF1cn_uS2r9diR68Bn6M5SXMbVmYYXcSM8CqbwrX6EC87DSGkh5WjIFi2rim90P49dkoYua9QVfTbrnbySDxqo90ThIXMNHVmGSl0vxCQ5iIusdQKFG4Jy0N-_8oMK9m6qpznt8h8rA",
                 w=None
                 ):
        self.id = id
        self.base_url = f"https://books.google.ru/books"

        self.lpg = lpg
        self.pg = pg
        self.hl = hl
        self.jscmd = jscmd
        self.w = w

        self.cookies = cookies
        self.dict_cookies = {"cookie": self.cookies}

        self.req = requests.get(self.base_url + f"?id={self.id}&lpg={self.lpg}&hl={self.hl}&pg={self.pg}&jscmd={self.jscmd}&w={self.w}", headers=USER_HEADERS | self.dict_cookies)
        self.json_main_response = self.req.json()

        self.main_webpage_text = requests.get(self.url).text

    @property
    def name(self):
        return re.findall('<meta name="title" content="(.+?)"/>', self.main_webpage_text)[0].strip()

    @property
    def authors(self):
        try:
            return re.findall("<title.*?>(.+?)</title>", self.main_webpage_text)[0].split("-")[1].strip().split(", ")
        except Exception:
            return ""

    @property
    def description(self):
        local_result = re.findall('<meta name="description" content="(.+?)"/>', self.main_webpage_text)[0].strip()
        if '"' not in local_result:
            return local_result
        else:
            return ""

    @property
    def url(self):
        """Get string url to book"""
        return self.base_url + f"?id={self.id}"

    @property
    def page_type(self):
        """Get string type of page. This type be need to get correct page-link"""
        return self.json_main_response['page'][1]['pid'][:-1]

    @property
    def length(self):
        """Get count of pages"""
        return int(self.json_main_response["page"][len(self.json_main_response["page"])-1]["pid"][2:])

    @property
    def cover_link(self):
        """Get link to cover of book"""
        return self.get_link_to_page(page_number=0)

    def get_link_to_page(self, page_number=1):
        """Get link to page as PNG image"""
        local_req = requests.get(self.base_url + f"?id={self.id}&lpg={self.lpg}&hl={self.hl}&pg={self.page_type}{page_number}&jscmd={self.jscmd}", headers=USER_HEADERS | self.dict_cookies)
        try:
            if self.w != None:
                return local_req.json()["page"][0]["src"]+f"&w={self.w}"
            else:
                return local_req.json()["page"][0]["src"]
        except Exception:
            raise InvalidPageToPublicView()

