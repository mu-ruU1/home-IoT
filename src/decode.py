import json
import sys
import statistics

T_NEC = 562
T_AEHA = 425
T_SONY = 600


def output(bit):
    byte = []
    print(len(byte))
    if len(byte) <= 8:
        byte.append(bit)
    else:
        byte.clear
        print(len(byte))
    with open("decode.json", "w") as f:
        json.dump(byte, f, indent=4)


def format_data(first, second, i):
    first /= T_AEHA
    second /= T_AEHA

    fr = round(first)
    sr = round(second)

    if fr//sr == 1 or sr//fr == 1:
        # print(fr, sr, " -> ", 0, " i->", i)
        output(0)
    elif sr//fr == 3:
        # print(fr, sr, " -> ", 1, " i->", i)
        output(1)
    elif fr//sr == 2:
        print(fr, sr, "leader")
    else:
        print(fr, sr, "no data")


def decode(value):
    for i in range(len(value)-1):
        if i % 2 == 0:
            format_data(value[i], value[i+1], i)


def calc_period(value):
    res = []
    median = 0  # 中央値

    # 信号ON時のデータを取得
    for i in range(len(value)):
        if (i % 2 == 0) and (value[i] < 1000):
            res.append(value[i])

    median = statistics.median(value)
    print("T (変調単位): ", median)

    # 通信フォーマットの判別
    nec = abs(median - T_NEC)
    aeha = abs(median - T_AEHA)
    sony = abs(median - T_SONY)

    format = [nec, aeha, sony]

    index = format.index(min(format))

    if index == 0:
        print("NECフォーマット\nこのプログラムは対応していません")
        exit(0)
    elif index == 1:
        print("AEHAフォーマット\nデコードを行います\n")
    elif index == 2:
        print("SONYフォーマット\nこのプログラムは対応していません")
        exit(0)


def main(path, key):
    with open(path, "r") as f:
        values = json.load(f)
        value = values[key]

    calc_period(value)

    # AEHAフォーマットのみに対応
    decode(value)


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 3:
        path = args[1]
        key = args[2]
        main(path, key)
    else:
        print("error: pathとkeyを指定して下さい")
        print("$ decode.py <json_path> <json_key>")
        sys.exit(1)
