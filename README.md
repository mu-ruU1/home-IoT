# home-IoT

Raspberry Pi を使用した自宅 IoT

## 使用機器

- [Raspberry Pi 4 Model B 8GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [RPZ-IR-Sensor](https://www.indoorcorgielec.com/products/rpz-ir-sensor/)

## 準備

[pigpio](http://abyz.me.uk/rpi/pigpio/index.html)ライブラリのインストール

```bash
$ sudo apt install pigpio python3-pigpio -y

$ sudo systemctl enable pigpiod

$ sudo systemctl start pigpiod
```

赤外線制御プログラムの準備  
[IR Record and Playback](http://abyz.me.uk/rpi/pigpio/examples.html#Python_irrp_py)を使う方法もありますが、[cgir](https://github.com/IndoorCorgi/cgir)を使いました。

```bash
$ sudo apt-get install python3-pip

$ sudo python3 -m pip install -U cgir
```

## ディレクトリ構成

- [`docs`](./docs/)
  - 赤外線信号の解析

## 参考

- [Python と pigpio で Raspberry Pi の赤外線制御](https://www.indoorcorgielec.com/resources/raspberry-pi/python-pigpio-infrared/)
- [パナソニック製エアコンの信号解析](https://ak1211.com/7141/#%E3%83%91%E3%83%8A%E3%82%BD%E3%83%8B%E3%83%83%E3%82%AF%E8%A3%BD%E3%82%A8%E3%82%A2%E3%82%B3%E3%83%B3%E3%81%AE%E4%BF%A1%E5%8F%B7%E8%A7%A3%E6%9E%90)
- [A75C4269](https://github.com/wtks/A75C4269)
- [Reverse engineering the Panasonic AC Infrared protocol](https://www.analysir.com/blog/2014/12/27/reverse-engineering-panasonic-ac-infrared-protocol/)
