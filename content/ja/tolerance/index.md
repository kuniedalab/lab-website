---
title: Tolerance mechanisms
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; gap: 0px; flex-wrap: wrap; justify-content: center; line-height: 1;">
        <a href="../tardigrade/" class="btn btn-green-color btn-lg">
          <i class="fas fa-microscope mr-1"></i> クマムシとは？
        </a>
        <a href="../tolerance/" class="btn btn-glass btn-lg">
          <i class="fas fa-shield-alt mr-1"></i> 耐性のメカニズム
        </a>
        <a href="../rotifer/" class="btn btn-lg btn-green-color">
          <i class="fas fa-spinner mr-1"></i> ワムシとは？
        </a>
        <a href="https://www.sci.u-hyogo.ac.jp/life/biosig/japanese/yan_jiu_nei_rong.html" class="btn btn-lg btn-green-color">
          <i class="fas fa-sync mr-1"></i> 細胞周期
        </a>
        </div>
      #  {{% cta cta_link="./member/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
      spacing:
        padding: ["10px", "0", "10px", "0"]
      background:
        image:
          filename: kumanui2.jpg
          filters:
            brightness: 0.7
          position: left
          color: '#333'
          parallax: false
          size: cover
        text_color_light: true

  - block: markdown
    content:
      title: クマムシの耐性メカニズムの研究
      text: |
        <video width="640" height="360" muted autoplay loop playsinline preload="true">
          <source src="2016_Rv_injection_Saigo.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <br>
        <div class="faq">
          <details name="tolerance" open>
            <summary>ヨコヅナクマムシのゲノム解読 ー 独自の遺伝子が沢山ある！</summary>
            <img src="yokozuna-genome-ja.jpg" alt="クマムシゲノム" style="width: 100%; max-width:600px; height: auto; border-radius: 10px; display: block; margin: 0 auto;">
            <p>クマムシ類の中でも急速な乾燥に耐え、特に高い極限環境耐性を示すヨコヅナクマムシ（<span style="font-style: italic;">Ramazzottius varieornatus</span>, YOKOZUNA-1 strain）について遺伝研と共同でゲノムを解読しました。ゲノムサイズは 55Mb と小さく、ショウジョウバエの1/3、ヒトの1/50未満でした。15,000〜20,000遺伝子を持つと考えられ、およそ半分強が他の動物と共通しており、既知のストレス応答遺伝子（抗酸化や修復に関わる遺伝子）が増加していました。先祖以外に由来すると考えられる水平伝播遺伝子は2%未満と特筆するほど多くはありませんでした。全遺伝子の約40%が他の生物には見られないクマムシ固有のもので、タンパク質に注目した解析から発見された耐性タンパク質（下記）はこれら固有の遺伝子にコードされているものが多く見つかっており、独自の遺伝子が耐性に重要な役割を果たしていると考えられています。</p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">放射線から DNA を守る Dsup タンパク質</summary>
            <img src="dsup-ja.jpg" alt="Dsup" style="width: 100%; max-width:900px; height: auto; border-radius: 10px; display: block; margin: 0 auto;">
            <p>高線量の放射線や完全乾燥は DNA に二重鎖切断を始めとする重篤な障害を発生させます。こうしたストレスに耐性を示すヨコヅナクマムシは DNA を正常に保つ機能が高いと推定され、DNA に結合しているタンパク質の１つとして Dsup (Damage suppressor; ダメージを抑制するもの）と名付けたタンパク質を分離同定しました。Dsup はクマムシ以外には見つからないタンパク質でしたが、Dsup 遺伝子を組み込んだヒト培養細胞は、X 線によるDNA障害が約40%低減し、通常の細胞が死ぬような線量を照射したあとも一部の細胞は生き残り、増殖することがわかりました。<br>
            　世界中の研究室が様々な生物に Dsup を導入した結果、ショウジョウバエや酵母、稲、タバコといった生物でも DNA の保護効果を示すことが報告されています。</p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">ストレスに応答して線維化して細胞を守る CAHS タンパク質</summary>
            <video width="504" height="504" muted autoplay loop playsinline preload="true">
              <source src="deh-reh-ja-text.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
            <img src="cahs-ja.jpg" alt="Dsup" style="width: 100%; max-width:600px; height: auto; border-radius: 10px; display: block; margin: 0 auto;">
            <p>CAHSタンパク質もクマムシにしかないタンパク質ファミリーで2012年に当研究室により初めて同定されました。加熱しても沈殿しない性質を持ち、多くのクマムシ種で乾燥時に発現が顕著に増加します。近年、濃度上昇に伴って自発的に繊維を形成することが私たちを含む複数の研究室によりほぼ同時期に報告されました。私たちは、CAHSタンパク質が細胞内で脱水ストレスに応答して多数の構造を形成し、細胞を物理的に強化してストレスから保護することを見出しました。この変化は可逆的でストレスがかかった時だけ、ちょうど鉄筋のような構造を細胞内に張り巡らせて守っているのではないかと考えています。</p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">ゲノム編集個体の作出法の開発（DIPA-CRISPR）</summary>
            <p>クマムシはいろんな場所に生息していますが、乾眠能力を持つものを採取するのであれば、コンクリート壁や路上に生えている乾いたコケから採るのが成績良好です。　住みやすそうな湿ったところよりも、頻繁に乾燥する厳しい環境の方がこうしたクマムシはむしろ生き残りやすいようです。良く乾いたコケを採取して水を加えて数時間から一晩放置すると、乾眠していたクマムシが動き出します。</p>
          </details>
          <details name="tolerance">
            <summary>発見したクマムシ固有の耐性遺伝子の配布</summary>
            <p>私たちが発見したクマムシ固有の耐性遺伝子などについては下記の配布機関から入手することができます（原則として研究機関に限ります）。<br>
            ・<a href="https://www.addgene.org/Takekazu_Kunieda/" target="_blank">Addgene: Kunieda Lab</a><br>
            ・<a href="https://knowledge.brc.riken.jp/xsearch/catalog/list?__lang__=ja&query=Takekazu+Kunieda" target="_blank">理研BRC: Takekazu Kunieda</a><br>
            </p>
          </details>
          <details name="tolerance">
            <summary>関連動画</summary>
            <p>・2016 : <a href="https://www.youtube.com/watch?v=Rg3n7_fvMp0" target="_blank">極限状態に耐える動物クマムシの秘密を探る - 東京大学オープンキャンパス</a><br>
            ・2016 : <a href="https://www.youtube.com/watch?v=A2hM_W-lP5c" target="_blank">クマムシの強さの謎を解く - UTokyo Research プレスリリース</a><br>
            ・2016 : <a href="https://www.youtube.com/watch?v=UD0R37eGOec" target="_blank">Demystifying the resilience of water bears - UTokyo Research 英文リリース</a><br>
            ・2020 : <a href="https://www.youtube.com/watch?v=ERKDgQ1Cykw" target="_blank">宇宙も平気なクマムシ - JAXA</a><br>
            ・2024 : <a href="https://www.youtube.com/watch?v=WRmGIK-mkQ4" target="_blank">最強生物クマムシ - いまからサイエンス #60予告編 (BSテレ東)</a><br></p>
          </details>
        </div>
#        align: center
    design:
      columns: "1"
      spacing:
         padding: ["50px", "5%", "30px", "5%"]
#      # Slide height is automatic unless you force a specific height (e.g. '400px')
#      slide_height: ''
#      is_fullscreen: true
#      # Automatically transition through slides?
#      loop: false
      # Duration of transition between slides (in ms)
#      interval: 2000
---
