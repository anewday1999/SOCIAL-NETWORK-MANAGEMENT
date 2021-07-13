import requests, json, pprint
import config

class facebookAPI:

    def __init__(self, app_id, app_secret, access_token):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.host_url = "https://graph.facebook.com/"
        self.ver = 'v11.0/'
        self.url = self.host_url + self.ver

    def get_info(self, object_id):
        url = self.url + object_id + '/'
        payload = {'access_token': self.access_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_likes(self, object_id):
        url = self.url + object_id + '/likes'
        payload = {'access_token': self.access_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_posts(self, object_id):
        url = self.url + object_id + '/posts'
        payload = {'access_token': self.access_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_comments(self, object_id):
        url = self.url + object_id + '/comments'
        payload = {'access_token': self.access_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_sharedposts(self, object_id):
        url = self.url + object_id + '/sharedposts'
        payload = {'access_token': self.access_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res




if __name__ == '__main__':
    app_id = config.app_id
    print(app_id)
    app_id_secret = config.app_id_secret
    acces_token = config.acces_token
    id = '107310934648059'
    id_post = '107310934648059_114844293894723'


    fa = facebookAPI(app_id = app_id, app_secret = app_id_secret, access_token = acces_token)
    pprint.pprint(fa.get_info(id))
    pprint.pprint(fa.get_likes(id))
    pprint.pprint(fa.get_posts(id))
    pprint.pprint(fa.get_likes(id_post))
    pprint.pprint(fa.get_comments(id_post))
    pprint.pprint(fa.get_sharedposts(id_post))



    
