class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class News:
    '''
    Categorized news class to define News Objects
    '''

    def __init__(self,name, author,title, description, url, urlToImage, publishedAt, content):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
