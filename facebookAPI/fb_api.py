import requests, json, pprint
import config

class facebookAPI:

    def __init__(self, app_id, app_secret, user_token = None, page_token = None):
        self.app_id = app_id
        self.app_secret = app_secret
        self.user_token = user_token
        self.page_token = page_token
        self.host_url = "https://graph.facebook.com/"
        self.ver = 'v11.0/'
        self.url = self.host_url + self.ver

    #dau tien lay user token tu client id, xu ly tu dong sau voi server
    def get_user_token(self, redirect ,scope):
        url = 'https://www.facebook.com/v11.0/dialog/oauth?response_type=token&client_id=' + self.app_id + '&redirect_uri=' + redirect + '&auth_type=rerequest&scope=' + scope
        
        print("Click this url to get code: ")
        print(url)

    #Dat user token
    def set_user_token(self, token):
        self.user_token = token

    #Lay page token tu pageID va user_token
    def get_page_token(self, pageID):
        url = 'https://graph.facebook.com/{:s}?fields=access_token&access_token={:s}'.format(pageID, self.user_token)
        res = requests.get(url)
        return res.json()['access_token']

    #set
    def set_page_token(self, token):
        self.page_token = token

    def get_user_info(self):
        url = self.url + 'me/'
        payload = {'access_token': self.user_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res
    
    def get_page_info(self):
        url = self.url + 'me/'
        payload = {'access_token': self.page_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    #Thao tac voi page
    def get_likes(self, object_id):
        url = self.url + object_id + '/likes'
        payload = {'access_token': self.page_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_posts(self, object_id):
        url = self.url + object_id + '/posts'
        payload = {'access_token': self.page_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_comments(self, object_id):
        url = self.url + object_id + '/comments'
        payload = {'access_token': self.page_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res

    def get_sharedposts(self, object_id):
        url = self.url + object_id + '/sharedposts'
        payload = {'access_token': self.page_token}
        res = requests.get(url, params=payload)
        res = res.json()
        return res




if __name__ == '__main__':
    app_id = config.app_id
    app_id_secret = config.app_id_secret

    fa = facebookAPI(app_id = app_id, app_secret = app_id_secret)
    #Lay user token xu ly sau voi server, tam thoi su dung api-university de get token
    #fa. get_user_token(scope='pages_show_list%2Cpages_read_engagement%2Cpublic_profile%2Cread_insights%2Cpages_read_user_content%2Cpages_messaging%2Cpages_messaging_phone_number%2Cpages_messaging_subscriptions%2Cpages_manage_posts%2Cpages_manage_instant_articles%2Cpages_manage_metadata%2Cpages_manage_engagement', redirect='https%3A%2F%2Fapi-university.com%2F')

    #Sau khi lay tokeno buoc tren, set user token
    fa.set_user_token('')

    #Lay page token va set
    fa.set_page_token(token = fa.get_page_token(pageID='107310934648059'))

    #Truy xuat 1 so thong tin
    pprint.pprint(fa.get_page_info())
    pprint.pprint(fa.get_user_info())
    pprint.pprint(fa.get_posts('107310934648059'))
    pprint.pprint(fa.get_likes('107310934648059_115114377201048'))
    pprint.pprint(fa.get_comments('107310934648059_115114377201048'))
    pprint.pprint(fa.get_sharedposts('107310934648059_115114377201048'))
