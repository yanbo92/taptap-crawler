import requests
from http.cookies import SimpleCookie
import re
import bs4
from retrying import retry
import pymongo



def generate_url(user_id, page):
    return "https://www.taptap.com/user/{}/played?page={}".format(user_id, page)


@retry(stop_max_attempt_number=10, wait_random_min=60000, wait_random_max=120000)
def get_games_pages(userid):
    url1 = generate_url(userid, 1)
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400'
    headers = {r'User-Agent': user_agent}
    requests.adapters.DEFAULT_RETRIES = 1000
    cookies = "自己去抓包"
    cookie = SimpleCookie(cookies)
    cookies = {coo.key: coo.value for coo in cookie.values()}
    r = requests.get(url1, cookies=cookies, timeout=100)
    rstr=str(r.content, encoding="utf-8")
    if rstr.__contains__("找不到页面"):
        print("no user {}", userid)
        return 0
    else:
        bs = bs4.BeautifulSoup(rstr, "html.parser")
        num_str = (str(bs.select('h4 span')[0]))
        games_num = int(re.findall(r'\d+', num_str)[0])
        pages = games_num // 8 + 1
        print("find {} games in user {}, needs {} pages".format(games_num, userid, pages))

        return pages


@retry(stop_max_attempt_number=10, wait_random_min=60000, wait_random_max=120000)
def get_game_list(usid, pgs):
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400'
    headers = {r'User-Agent': user_agent}
    requests.adapters.DEFAULT_RETRIES = 1000
    cookies = "tapadid=f899eb6b-a938-f67d-10e3-c1f0e0b75d0a; _ga=GA1.2.1427902761.1571465801; _gid=GA1.2.247815275.1606822581; acw_tc=2760829916068244229638564e11bfc3fd05707e5346b7b4468ecf14434503; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Ik9Ta2ViYkZQS2RHdHlPZkVpVFUrSUE9PSIsInZhbHVlIjoiQWZJSStFbEpDRW13M2VsSElrMmxvcWNMMGs3aWdnWjRwTkphXC9aRVVZUVl1NzU2RWtjMWtWK1NWNU53RGpGbHp2d2gwaDQ4S3Rsc0MxWExIb1JzREc0Vk1ibXBjTEt3UENsSjNWTFRPTWdFPSIsIm1hYyI6ImUxMzk3NGM4YmJiMWJmYjczODVlY2U0ODViOWM3ODQ5YzJhZWExZjYzMWY0ODZhODcxYmFlMThhOGM5YzM3NzAifQ%3D%3D; user_id=23375060; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223375060%22%2C%22%24device_id%22%3A%2216de2a92cbb4f3-044a31eb458c85-67e1b3f-1327104-16de2a92cbc521%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216de2a92cbb4f3-044a31eb458c85-67e1b3f-1327104-16de2a92cbc521%22%7D; XSRF-TOKEN=eyJpdiI6InlPWUtvS1wvaFpcL01YcG0zYXFqbnZaQT09IiwidmFsdWUiOiJSUG81VVRSN3pvcis5XC93ZWRmd2Q3bXV1NFN0bzA4OHlSTXRNdERJOXpDcEpUNWsyWEpKR1R5Y1B6UEtkaWZhbTRBdkNOY1dTUEtlZnU5Z0FHanFwWFE9PSIsIm1hYyI6IjAxMjJlN2FhOTIzMzJlYzY3NjdjMjY3YTVkYzJhYmM4MDdhYzAxYzM5ZTg1NjdlMmI0N2E2YjEyMjY2MGI1YjEifQ%3D%3D; tap_sess=eyJpdiI6IkVkTmRNTXZLWm1zaG9wSzMxd1VVREE9PSIsInZhbHVlIjoiXC9qVFBlak5IVVhkNDk3ek9HV1NRY1llZno5SXJsQjY1QU4rTWRoNjdjK1JGeEgzWlNhbVVBSlpCWTdreWNNM2luaEd4Z0x4QXQxMXJxXC9BT3UxeldTQT09IiwibWFjIjoiZmFkMmQxMzdiY2M5MTA4NGE0MDFkNjAyNjA1YzcxZWM0NjIxN2U0YzkzMDg5NTgzNjFlNjZiZWNiNGI2YjA0YiJ9"
    cookie = SimpleCookie(cookies)
    cookies = {coo.key: coo.value for coo in cookie.values()}
    game_list = []
    for p in range(1, pgs+1):
        url_str = generate_url(usid, p)
        print(url_str)
        r = requests.get(url_str, cookies=cookies, timeout=100)
        rstr=str(r.content, encoding="utf-8")
        bs = bs4.BeautifulSoup(rstr, "html.parser")
        for item in bs.select('h2 a'):
            game_list.append(item.string)
    return game_list


def save_games_to_db(start_id, end_id):
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
    mango_db = mongo_client["taptap"]
    mango_collection = mango_db["taptap_games_of_users"]
    user_id = start_id
    while user_id < end_id:
        find_list = mango_collection.count_documents({"_id": user_id}, {})
        if find_list:
            print("EXISTED")
        else:
            print("user_id:{}".format(user_id))
            pages = get_games_pages(user_id)
            if pages:
                game_list = get_game_list(user_id, pages)
            else:
                game_list = [""]
            game_set = set(game_list)
            game_list = list(game_set)
            print(game_list)
            game_dict = {"_id": user_id, "games": game_list}
            try:
                mango_collection.insert_one(game_dict)
            except pymongo.errors.DuplicateKeyError:
                print("EXISTED")
            else:
                print("FINISH:" + str(user_id))
        user_id = user_id + 1


if __name__ == "__main__":
    player_id = 1
    print(get_game_list(player_id, get_games_pages(player_id)))

