# GPT Tutorial

## How to install

```bash
pip install openai==1.35.3
export OPENAI_API="sk-..."  # ターミナルごとで，APIキーを指定
```

- bashrcに書き込んでしまう方法もあります．
  - 使い方がわからない場合は検索してみてください．

```bash
echo "export OPENAI_API=\"sk-your-api-key\"" >> ~/.bashrc 
source ~/.bashrc
```

## GPTを使った簡単なタスク理解を実行

- サンプルプログラム

```bash
python3 script/01_simple_question.py
```

- [ ] プロンプトの与え方を理解する
- [ ] 結果の受け取り方を理解する

## 対話的に動かすサンプル

```bash
python3 script/02_interactive_question.py
```

- [ ] 対話をすすめていく方法を理解する

## 画像の扱い

```bash
python3 script/03_image_question.py
```

- [ ] 画像の入力方法を理解する
