"""
Calificación del laboratorio
-----------------------------------------------------------------------------------------
"""

import sqlite3
import sys

import pandas as pd


def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur


def test_01():
    conn, _ = load_data()
    with open("pregunta_01.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {"SUM(c12)": {0: 15137.63}}


def test_02():
    conn, _ = load_data()
    with open("pregunta_02.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {"COUNT(*)": {0: 30}}


def test_03():
    conn, _ = load_data()
    with open("pregunta_03.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "C", 2: "E", 3: "B", 4: "E"},
        "K1": {0: 20, 1: 15, 2: 22, 3: 12, 4: 14},
        "c12": {0: 938.16, 1: 370.58, 2: 118.77, 3: 999.72, 4: 832.44},
        "c13": {0: 300, 1: 900, 2: 900, 3: 800, 4: 800},
        "c14": {
            0: "2016-09-12",
            1: "2016-10-01",
            2: "2016-10-29",
            3: "2016-11-09",
            4: "2016-11-22",
        },
        "c15": {0: 0.19, 1: 0.11, 2: 0.32, 3: 0.26, 4: 0.39},
        "c16": {0: "BECB", 1: "GCDD", 2: "GEFE", 3: "FCGD", 4: "EGFD"},
    }


def test_04():
    conn, _ = load_data()
    with open("pregunta_04.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "E", 1: "B", 2: "C"},
        "c16": {0: "EGFD", 1: "BDEE", 2: "CCCE"},
    }


def test_05():
    conn, _ = load_data()
    with open("pregunta_05.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "B", 1: "C", 2: "D", 3: "G"},
        "c01": {0: 7000, 1: 1000, 2: 4000, 3: 5000},
        "c02": {0: 100, 1: 600, 2: 600, 3: 100},
        "c03": {0: "OLPKN", 1: "LMMML", 2: "PJLJL", 3: "NLPLO"},
        "c04": {0: 0.2, 1: 0.2, 2: 0.4, 3: 0.2},
    }


def test_06():
    conn, _ = load_data()
    with open("pregunta_06.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "A", 2: "A", 3: "A", 4: "A", 5: "A"},
        "K1": {0: 20, 1: 30, 2: 18, 3: 26, 4: 6, 5: 10},
        "c12": {0: 938.16, 1: 135.8, 2: 142.99, 3: 456.47, 4: 391.42, 5: 816.51},
        "c13": {0: 300, 1: 900, 2: 100, 3: 400, 4: 300, 5: 600},
        "c14": {
            0: "2016-09-12",
            1: "2017-01-26",
            2: "2017-02-12",
            3: "2018-01-28",
            4: "2018-05-15",
            5: "2019-04-25",
        },
        "c15": {0: 0.19, 1: 0.23, 2: 0.48, 3: 0.11, 4: 0.22, 5: 0.4},
        "c16": {0: "BECB", 1: "EGAB", 2: "GGFD", 3: "FGED", 4: "BFGB", 5: "DAGC"},
    }


def test_07():
    conn, _ = load_data()
    with open("pregunta_07.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {
            0: "E",
            1: "E",
            2: "E",
            3: "E",
            4: "D",
            5: "E",
            6: "C",
            7: "C",
            8: "C",
            9: "E",
            10: "D",
            11: "C",
            12: "C",
        },
        "K1": {
            0: 14,
            1: 8,
            2: 1,
            3: 27,
            4: 4,
            5: 3,
            6: 13,
            7: 5,
            8: 7,
            9: 25,
            10: 2,
            11: 19,
            12: 24,
        },
        "c12": {
            0: 832.44,
            1: 302.86,
            2: 273.08,
            3: 720.9,
            4: 662.69,
            5: 305.43,
            6: 712.61,
            7: 822.81,
            8: 755.27,
            9: 600.9,
            10: 756.37,
            11: 570.43,
            12: 482.32,
        },
        "c13": {
            0: 800,
            1: 700,
            2: 600,
            3: 800,
            4: 800,
            5: 100,
            6: 400,
            7: 100,
            8: 800,
            9: 700,
            10: 500,
            11: 400,
            12: 300,
        },
        "c14": {
            0: "2016-11-22",
            1: "2016-12-22",
            2: "2016-12-31",
            3: "2017-01-16",
            4: "2017-03-26",
            5: "2017-05-21",
            6: "2017-10-23",
            7: "2017-11-17",
            8: "2018-07-04",
            9: "2018-11-07",
            10: "2019-02-28",
            11: "2019-04-12",
            12: "2019-05-03",
        },
        "c15": {
            0: 0.39,
            1: 0.14,
            2: 0.21,
            3: 0.12,
            4: 0.23,
            5: 0.21,
            6: 0.31,
            7: 0.35,
            8: 0.47,
            9: 0.36,
            10: 0.37,
            11: 0.48,
            12: 0.11,
        },
        "c16": {
            0: "EGFD",
            1: "DFCC",
            2: "BDGD",
            3: "FBGD",
            4: "BGDD",
            5: "BAED",
            6: "EDDA",
            7: "GGFC",
            8: "GCDB",
            9: "BBBA",
            10: "BCCC",
            11: "FBEE",
            12: "CCCE",
        },
    }


def test_08():
    conn, _ = load_data()
    with open("pregunta_08.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "strftime('%Y', c23)": {0: "2016", 1: "2017", 2: "2018", 3: "2019"},
        "avg(c21)": {
            0: 564.4764285714285,
            1: 515.1563636363637,
            2: 557.5593749999999,
            3: 550.9985714285714,
        },
    }


def test_09():
    conn, _ = load_data()
    with open("pregunta_09.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K1": {0: 29},
        "c21": {0: 101.11},
        "c22": {0: 100},
        "c23": {0: "2017-11-17"},
        "c24": {0: 0.42},
        "c25": {0: "MV-CB"},
    }


def test_10():
    conn, _ = load_data()
    with open("pregunta_10.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "C", 2: "D", 3: "F", 4: "I"},
        "c01": {0: 5000, 1: 1000, 2: 4000, 3: 2000, 4: 3000},
        "c02": {0: 900, 1: 600, 2: 600, 3: 300, 4: 300},
        "c03": {0: "NMNJL", 1: "LMMML", 2: "PJLJL", 3: "NNPJO", 4: "PPPPL"},
        "c04": {0: 0.4, 1: 0.2, 2: 0.4, 3: 0.3, 4: 0.3},
    }


def test_11():
    conn, _ = load_data()
    with open("pregunta_11.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {"COUNT(*)": {0: 6}}


def test_12():
    conn, _ = load_data()
    with open("pregunta_12.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"},
        "MAX(c12)": {0: 938.16, 1: 999.72, 2: 822.81, 3: 756.37, 4: 832.44},
        "MIN(c12)": {0: 135.8, 1: 283.4, 2: 267.42, 3: 317.77, 4: 118.77},
    }


def test_13():
    conn, _ = load_data()
    with open("pregunta_13.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"},
        "avg(c12)": {
            0: 476.155,
            1: 536.5233333333333,
            2: 490.8299999999999,
            3: 709.53,
            4: 474.82500000000005,
        },
    }


def test_14():
    conn, _ = load_data()
    with open("pregunta_14.sql", encoding="utf-8") as file:
        query = file.read()
    assert pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"},
        "avg(c21)": {
            0: 593.495,
            1: 575.47,
            2: 530.7529999999999,
            3: 655.6125,
            4: 555.323076923077,
        },
    }


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
    "04": test_04,
    "05": test_05,
    "06": test_06,
    "07": test_07,
    "08": test_08,
    "09": test_09,
    "10": test_10,
    "11": test_11,
    "12": test_12,
    "13": test_13,
    "14": test_14,
}[sys.argv[1]]

test()
