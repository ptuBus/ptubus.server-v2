import sqlite3


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
