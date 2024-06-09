import requests
from bs4 import BeautifulSoup
import argparse
import signal

signal.signal(signal.SIGINT, lambda signum, frame: exit(0))

parser = argparse.ArgumentParser(description='Yandex Contest full parser')
parser.add_argument('start_num', type=int, help='Номер начального контеста (default = 0)', default=0)
parser.add_argument('end_num', type=int, help='Номер конечного контеста (default = 30000)', default=30000)
args = parser.parse_args()


def header():
    with open('parse.txt', 'r+') as f:
        if not len(f.read()) > 0:
            print(f"(Contest №)".ljust(12) + " - " +
                  f"(Contest name)".ljust(128) + " - " +
                  f"(Contest link)", file=f)
    f.close()


def parse():
    for contests_num in range(args.start_num, args.end_num):
        soup = BeautifulSoup(requests.get(f"https://contest.yandex.ru/contest/{contests_num}/").content, "html.parser")
        results = soup.find(href=f"/contest/{contests_num}/enter/?retPage=")
        with open('parse.txt', 'a') as f:
            if results is not None:
                print(f"{contests_num}".ljust(12) + " - " +
                      f"[{str(*results)}]".ljust(128) + " - " +
                      f"https://contest.yandex.ru/contest/{contests_num}/", end="", file=f)
                print(file=f)
            else:
                print(f"{contests_num}".ljust(12) + " - " +
                      f"[N/A]".ljust(128) + " - " +
                      f"https://contest.yandex.ru/contest/{contests_num}/", end="", file=f)
                print(file=f)
        f.close()


print("Добро пожаловать в программу для парсинга данных из Контест системы от Яндекса")
header()
parse()


