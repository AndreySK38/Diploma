import requests


headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjIxOTgyLCJpYXQiOjE3Mzk5NjQxMzgsImV4cCI6MTczOTk2NzczOCwidHlwZSI6MjB9.ZOb3Ox9MXb8CIWp9b4PHlydzfLC8oteJmTzXuOPMJhI"}
base_url = "https://web-gate.chitai-gorod.ru"


def test_search_by_name():
     res = requests.get(base_url + "/api/v1/recommend/semantic?phrase=Ребенок Розмари&perPage=48",headers=headers)
     assert res.status_code == 200


def test_search_by_author():
     res = requests.get(base_url + "/api/v1/recommend/semantic?phrase=Айра Левин&perPage=48",headers=headers)
     assert res.status_code == 200


def test_using_part_of_the_title():
     res = requests.get(base_url + "/api/v1/recommend/semantic?phrase=Ребенок Розмари&perPage=48", headers=headers)
     assert res.status_code == 200

def test_search_by_name_from_numbers():
     res = requests.get(base_url + "/api/v1/recommend/semantic?phrase=1984&perPage=48", headers=headers)
     assert res.status_code == 200

def test_search_by_name_with_dots():
     res = requests.get(base_url + "/api/v1/recommend/semantic?phrase=s.n.u.f.f.&perPage=48", headers=headers)
     assert res.status_code == 200
