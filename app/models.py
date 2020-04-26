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
    all_news []
    '''
    Categorized news class to define News Objects
    '''

    def __init__(self,Sourcename, author, description, url, urlToImage, publishedAt, content):
        self.Sourcename = Sourcename
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
