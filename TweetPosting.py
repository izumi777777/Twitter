# =========================================================================================================
# 各使用するライブラリを宣言
# =========================================================================================================
import tweepy  # Twitter APIを使用するライブラリ
import SecretVariable
import os
import time

# =========================================================================================================
# Twitter APIキーの設定
# =========================================================================================================
client = tweepy.Client(
    consumer_key=SecretVariable.consumer_key,
    consumer_secret=SecretVariable.consumer_secret,
    access_token=SecretVariable.access_token,
    access_token_secret=SecretVariable.access_token_secret
)

# =========================================================================================================
# ファイルからツイートする内容の元を取得
# =========================================================================================================
text_files_directory = '/Users/izumi/Desktop/izumi/PythonDev/Twitter運用/dev/LangChain/output_files' # テキストファイルのあるディレクトリを指定
text_files_tags_directory = '/Users/izumi/Desktop/izumi/PythonDev/Twitter運用/dev/LangChain/output_files_tags' # タグファイルのあるディレクトリを指定

while True:
    # ディレクトリ内のテキストファイル一覧を取得
    text_files = [f for f in os.listdir(text_files_directory) if f.endswith(".txt")]
    text_files.sort()
    print(text_files)
    if not text_files:
        print("ファイルは存在しませんでした")
        break
    # ディレクトリ内のタグ一覧を取得
    text_tags = [f for f in os.listdir(text_files_tags_directory) if f.endswith(".txt")]
    text_tags.sort()
    print(text_tags)
    if not text_tags:
        print("ファイルは存在しませんでした")
        break
# =========================================================================================================
# ツイート実行
# =========================================================================================================
    # ファイルを順番に読み込んでツイート
    count = 0
    for text_file in text_files:
        text_file_path = os.path.join(text_files_directory, text_file)
        
        with open(text_file_path, 'r', encoding='utf-8') as file:
            tweet_text = file.read()
            print(tweet_text)
        
        # タグ文字列があるファイルを読み込む
        tags_file_path = os.path.join(text_files_tags_directory, text_file)
        if os.path.exists(tags_file_path):
            with open(tags_file_path, 'r', encoding='utf-8') as tags_file:
                tags = tags_file.read()
                print(tags)
                
                # ツイート本文 + タグ
                messages = f"{tweet_text}\n\n#{tags}"  # 投稿するメッセージ
                print(messages)
        else:
            # タグファイルが存在しない場合は、タグなしのツイートを投稿
            messages = tweet_text
            
        count += 1 # ツイート投稿の処理がされるたびにカウントを1追加する

        # Twitterへ投稿する
        client.create_tweet(text=messages)  # Twitterへ投稿するためのツイート
        print(str(count) + "回目: " + "Twitterへツイート投稿が完了しました")
        
        # 5分待機
        time.sleep(1800)
    print("ツイートの投稿が完了しました")
