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

## 参考

- [Python と pigpio で Raspberry Pi の赤外線制御](https://www.indoorcorgielec.com/resources/raspberry-pi/python-pigpio-infrared/)
