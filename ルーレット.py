from flask import Flask,render_template, request, redirect, url_for
import random

app=Flask(__name__)

#オプションの設定
A_options=['好きなタイプは？','何フェチ？','好きな服装','清楚派？ギャル派？','年上？年下？',
           '年齢差どこまで？','身長差どこまで？','露出多めと少なめどっちが好き？','甘えたい？甘えられたい？',
           '好きな顔のジャンル','好きな仕草','恋人の求める条件','理想の告白のセリフ','好きな人いる？',
           '浮気はどこから？','きゅんとしたエピソード発表','好きな人が一日言うこと聞いてくれるなら何したい？',
           '理想のデートとは？','好きな人にどう接する？','外でも手をつなぎたい？','失恋エピソード発表',
           '大事なのは見た目？中身？','甘えたい？甘えられたい？']
B_options=['性癖一つ発表','S?M?','NTRいける？','AV派？漫画派？','好きな人をオカズにできる？','好きな体位',
           '巨乳派？貧乳派？','好きなプレイ','好きなオカズのジャンル','同性とヤれる？','異性の好きな体の部位',
           '相手のどこにキスしたい？','ラッキースケベエピソード発表','優しめと激しめ、どっちが好き？',
           '処女or童貞すき？','経験人数','胸派？尻派？','何歳で卒業したorしたい？','恋人と猥談したい？',
           'どんなふうにキスされたい？','好きなオモチャ','どこでもセックスしていいならどこでしたい？',
           '口淫すき？','好きな喘ぎ声','異性のムラっと来る仕草','理想の毛量は？','コスプレで興奮する？',
           '学校でヤれる？','異性の友達とヤれる？','求めたい？求められたい？']
custom_results=[]

#HTMLにデータを渡す
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mode = request.form.get('mode')
        if mode=='A':
            result=random.choice(A_options+custom_results)
            message="軽めの話題(恋バナ向け)のルーレットです"
        elif mode=='B':
            result=random.choice(B_options+custom_results)
            message="重めの話題(猥談向け)のルーレットです"
        else:
            result=random.choice(A_options+B_options+custom_results)
            message="話題混合のルーレットです"

    # 結果とメッセージをテンプレートに渡す
        return render_template('index.html', result=result, message=message, 
                               current_results=A_options if mode == 'A' else B_options, 
                               custom_results=custom_results, mode=mode)
    return render_template('index.html', custom_results=custom_results)

@app.route('/add_result',methods=['POST'])
def add_result():
    custom_result=request.form.get('custom_result')
    if custom_result:
        custom_results.append(custom_result)
    return redirect(url_for('index'))

@app.route('/')
def home():
    return render_template('index.html')  # index.htmlがpublicにあると仮定

if __name__ == '__main__':
    app.run(debug=True)