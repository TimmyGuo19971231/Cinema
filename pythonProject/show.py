import datetime
import sys


def get_files(filename) -> list:
    with open(filename,"r",encoding="utf-8") as file:
        return [i.rstrip("\n") for i in file.readlines()]


def check_movie_time(movie_info: list[list],check_time: datetime) -> list:
    ls = []
    i = 0
    while i < len(movie_info):
        j = 0
        while j < len(movie_info[i]):
            movie_time_str = movie_info[i][j].split(". ")[-2]
            movie_time_hour = int(movie_time_str.split(":")[0])
            movie_time_minute = int(movie_time_str.split(":")[1])
            movie_time = datetime.time(movie_time_hour,movie_time_minute,0)
            if movie_time >= check_time:
                ls.append(movie_info[i][j])
            j += 1
        i += 1
    return ls

def main():
    time = sys.argv[-1]
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    check_time = datetime.time(hour, minute,0)
    movie1 = get_files("movie1.txt")
    movie2 = get_files("movie2.txt")
    movie3 = get_files("movie3.txt")
    for i in check_movie_time([movie1,movie2,movie3],check_time):
        print(i)
    print("\nBye.")

if __name__ == '__main__':
    main()