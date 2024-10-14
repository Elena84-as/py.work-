import multiprocessing
import datetime



all_data = []


def read_info(name):
    with open(name,encoding='utf-8') as file:
        for line in file:
            line = file.read()
            if not line:
                break
            else:
                all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.datetime.now()
for files in filenames:
    read_info(files)
    end1 = datetime.datetime.now()
    print(f' {end1-start1} - Линейный')

if __name__ == "__main__":
    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, all_data)
        end2 = datetime.datetime.now()
    print(f'{end2 - start2} - Многопроцессорный')
