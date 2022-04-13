celeb_list = []

def get_last_id():
    if celeb_list:
        last_celeb = celeb_list[-1]
    else:
        return 1
    return last_celeb.id + 1


class Celeb_list:
    
    def __init__(self, name, website, description):
        self.id = get_last_id()
        self.name = name
        self.website = website
        self.description = description


    @property
    def data(self):
        return{
            'id':self.id,
            'name':self.name,
            'website':self.website,
            'description':self.description
        }