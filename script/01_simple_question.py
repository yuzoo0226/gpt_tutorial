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

    def action_parser(self, order_txt: str) -> str:
        """
        お客さんの話から，次に行動すべき内容を決定する
        Args:
            order_txt(str): 注文内容
        Returns:
            str: 理解した内容
        """
        openai.api_key = self.api_key
        response = self.client.chat.completions.create(
            model=self.gpt_version,
            messages=[
                {"role": "system", "content": "次の文章から，お客さんがどんな動作を求めているのか出力してください．"},
                {"role": "system", "content": "注文を求めている場合は[order]，下げ膳を求めている場合は[clean]，商品の説明を求めている場合は[explain]と出力してください．"},
                {"role": "system", "content": "雑談を求めている場合は，[talk]と出力してください．"},
                {"role": "system", "content": "戻ってくださいと言われているときや，求められている動作がないときは，[done]と出力してください．"},
                {"role": "system", "content": "商品名だけを伝えられた場合は，注文を行っていると解釈してください．"},
                {"role": "user", "content": "りんごとばなな。"},
                {"role": "assistant", "content": "[order]"},
                {"role": "user", "content": order_txt},
            ]
        )

        answer = response.choices[0].message.content
        answer = answer[1:-1]
        print("=============== show all result ==============\n")
        print(response.choices)

        print("===============      action     ==============\n")
        print(answer)

        return answer


if __name__ == "__main__":
    text = "スイーツをください．"
    cls = TaskParser()
    cls.action_parser(text)
