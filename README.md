# portfolio
Portfolio for Internship

このプログラムは2021年iU情報経営イノベーション専門職大学、
イノベーションプロジェクトのSA用のプログラムです。
プログラムはアンケート課題用とストリーム用の2種類あります。
プログラム作成時はWindows10で動かしています。（macOSだと動きません）
プログラムによりGoogleCromeが起動します。この時PCでほかの操作をしないでください。

必要なもの
・クラスルームのURLが必要です。
・クラスルームに入っている教員アカウントのメールアドレスが必要です。
・教員アカウントのログインパスワードが必要です。

-----------------------------------

classroom_que_rep_count.py
・アンケート課題返信集計用プログラムです。
・1つのアンケートずつしか集計できません。
・クラスルームの各アンケート課題URLから、その課題の提出有無と提出日、各学生の課題への返信の数を集計してcsvファイルにします。

使い方
1.classroom_que_rep_count.pyを起動してください。
2.コンソールが表示されるまで待機してください。
3.集計したいアンケート課題の「すべての生徒の解答」画面を開き、コンソールへURLを入力（コピー＆ペースト）してください。
4.クラスルームに入っている教員アカウントのメールアドレスを入力してください。
5.教員アカウントのログインパスワードを入力してください。
6.GoogleChromeが起動するので、閉じるまで待機してください。
7.コンソールでcsvファイルに出力されたことを確認してください。
8.Enterキーでコマンドラインを閉じてください。
9.同じフォルダにあるcsvファイルを確認してください。
10.csvファイルに結果が出力されていたら成功です。

-----------------------------------

classroom_str_rep_count.py
・ストリームでの返信集計用プログラムです。
・1つのストリームずつしか集計できません。
・クラスルームの各ストリームURLから、人ごとの（投稿への）返信数を集計します。

使い方
1.classroom_str_rep_count.pyを起動してください。
2.コンソールが表示されるまで待機してください。
3.集計したいクラスルームの「ストリーム」画面を開き、コンソールへURLを入力（コピー＆ペースト）してください。
4.クラスルームに入っている教員アカウントのメールアドレスを入力してください。
5.教員アカウントのログインパスワードを入力してください。
6.GoogleChromeが起動するので、閉じるまで待機してください。
7.コンソールでcsvファイルに出力されたことを確認してください。
8.Enterキーでコマンドラインを閉じてください。
9.同じフォルダにあるcsvファイルを確認してください。
10.csvファイルに結果が出力されていたら成功です。
