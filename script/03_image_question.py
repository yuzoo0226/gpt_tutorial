#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import base64
import openai


class TaskParser():
    def __init__(self) -> None:
        # 環境変数からAPIキーを取得
        self.api_key = os.environ.get("OPENAI_API")
        self.gpt_version = "gpt-4o"

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

    def encode_image(self, image_path: str) -> str:
        """chatgptが必要とする形式にエンコードする関数
        """
        _, image_extension = os.path.splitext(image_path)

        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            url = f"data:image/{image_extension};base64,{image_base64}"

        return url

    def chat(self) -> None:
        """
        画像を含んだ会話サンプル
        """

        # プロンプトの初期化
        self.set_inital_prompt()

        # GPTが扱えるような形式での，画像の読み込み
        image_path = "./assets/Mandrill.jpg"
        image_url = self.encode_image(image_path=image_path)

        # 文字列と画像をプロンプトに追加
        self.messages.append(
            {"role": "user", "content":
                [
                    {
                        "type": "text",
                        "text": "この画像について簡潔に説明してください．"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        )

        # GPTの推論
        response = self.client.chat.completions.create(
            model=self.gpt_version,
            messages=self.messages
        )

        # 結果の表示
        answer = response.choices[0].message.content
        print(answer)


if __name__ == "__main__":
    cls = TaskParser()
    cls.chat()
