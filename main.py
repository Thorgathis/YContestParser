import requests
from bs4 import BeautifulSoup
import argparse
import signal

signal.signal(signal.SIGINT, lambda signum, frame: exit(0))

parser = argparse.ArgumentParser(description='Yandex Contest parser')
parser.add_argument('-l', '--show_links', help='Отображение ссылок', action="store_true")
parser.add_argument('-c', '--dis_checker', help='Выключает отображение сообщений раз в 100 запросов', action="store_true")
parser.add_argument('start_num', type=int, help='Номер начального контеста (default = 0)', default=0)
parser.add_argument('end_num', type=int, help='Номер конечного контеста (default = 30000)', default=30000)
parser.add_argument('find_par', type=str, help='Ключевое слово')

args = parser.parse_args()
print("Добро пожаловать в программу для парсинга данных из Контест системы от Яндекса")
print("")

for contests_num in range(args.start_num, args.end_num):
    soup = BeautifulSoup(requests.get(f"https://contest.yandex.ru/contest/{contests_num}/").content, "html.parser")
    results = soup.find(href=f"/contest/{contests_num}/enter/?retPage=")
    if results is not None:
        a = str(results).index("=\">")
        if str(results)[a:].find(args.find_par) > 0:
            print(f"{contests_num} - {str(*results)}"
                  f"{f' - https://contest.yandex.ru/contest/{contests_num}/' if args.show_links else ''}", end="")
            print()
    if contests_num % 100 == 0 and not args.dis_checker:
        print(f"# {contests_num} - EMPTY")


