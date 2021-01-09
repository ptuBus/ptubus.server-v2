import sqlite3
import csv


def get_line_data(queryset):
    conn = sqlite3.connect("ptu_subway/KorailDB/korail.db")
    cur = conn.cursor()
    cur.execute(queryset)
    db_data = cur.fetchall()

    line_data = []
    for db_datum in db_data:
        line_data.append(
            {
                "lineName": db_datum[0],
                "lineCode": db_datum[1],
                "lineColorCode": db_datum[2],
                "lineSaidName": db_datum[3],
            }
        )
    return line_data


def get_station_data():
    f = open("ptu_subway/KorailDB/line.csv", "r")
    temp = []

    rows = list(csv.reader(f))
    station_data = []

    for row in rows:
        temp2 = []
        index = 0
        for data in row:
            if data.find("◆") != -1:
                data = data.replace("◆", ",")
            if index == 6:
                if data.find(",") != -1:
                    data = data[: (data.find(","))]
                data = data.zfill(4)
            temp2.append(data)
            index += 1
        station_data.append(
            {
                "stationName": temp2[1],
                "stationCode": temp2[6],
                "lineCode": temp2[7],
                "railLineCode": temp2[12],
            }
        )

    f.close()
    del station_data[0]
    return station_data
