#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import openai


class TaskParser():
    def __init__(self) -> None:
        # 環境変数からAPIキーを取得
        self.api_key = os.environ.get("OPENAI_API")
        self.gpt_version = "gpt-3.5-turbo"

        if self.api_key is None:
            print("OPENAI_API is not set.")
            sys.exit()
        else:
            self.client = openai.OpenAI(api_key=self.api_key)

    def set_inital_prompt(self) -> None:
        self.messages = [
            # inital promptの定義
            {"role": "system", "content": "サービスロボットぽく振る舞ってください．"},

            # 会話の例を書くこともできます．
            {"role": "user", "content": "あなたはどんなことができるのですか？"},
            {"role": "assistant", "content": "ぼくはずんだもんなのだ．ずんだ餅の妖精なのだ．"},
        ]

    def chat(self) -> None:
        """
        サービスロボットとの会話するための関数
        """

        # プロンプトの初期化
        self.set_inital_prompt()

        while True:
            user_prompt = input("User >> ")

            if user_prompt == "q":
                break

            # 入力された文字列をプロンプトに追加
            self.messages.append(
                {"role": "user", "content": user_prompt}
            )

            # GPTの推論
            response = self.client.chat.completions.create(
                model=self.gpt_version,
                messages=self.messages
            )

            # 結果の表示
            answer = response.choices[0].message.content            
            print(f"HSR >> {answer}")

            # 出力された文字列もプロンプトに追加（会話の流れを記録）
            self.messages.append(
                {"role": "assistant", "content": answer}
            )


if __name__ == "__main__":
    cls = TaskParser()
    print("サービスロボットとの会話を楽しむプログラム，qで終了できます．")
    cls.chat()
