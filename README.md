# whisper_sample
このプログラムはWhisperモデルを活用した音声認識を行えるFlaskサーバのサンプルプログラムです。

**やること**

ffmpegのインストール方法を記載



### Macでの事前準備

①ffmpegが必要なのでインストール。インストールするのはbrewが簡単。

```ターミナル
brew install ffmpeg
```

### Windowsでの事前準備

①ffmpegの公式サイトからファイルをダウンロード

②ffmpegのパスを通す

下記コマンドが動くようにする。

```terminal
ffmpeg -version
```

### Linux(Ubuntu)

下記コマンドでインストールから確認までOK

```
$ sudo apt update
$ sudo apt install ffmpeg
$ ffmpeg -version
```

