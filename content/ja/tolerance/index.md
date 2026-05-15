---
title: 耐性メカニズム
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
          <i class="fas fa-arrows-spin mr-1"></i> 細胞周期
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
            <p>クマムシ類の中でも急速な乾燥に耐え、特に高い極限環境耐性を示すヨコヅナクマムシ（<span style="font-style: italic;">Ramazzottius varieornatus</span>, YOKOZUNA-1 strain）について遺伝研と共同でゲノムを解読しました。ゲノムサイズは 55Mb と小さく、ショウジョウバエの1/3、ヒトの1/50未満でした。15,000〜20,000遺伝子を持つと考えられ、およそ半分強が他の動物と共通しており、既知のストレス応答遺伝子（抗酸化や修復に関わる遺伝子）が増加していました。先祖以外に由来すると考えられる水平伝播遺伝子は2%未満と特筆するほど多くはありませんでした。</p>
            <p>　全遺伝子の約40%が他の生物には見られないクマムシ固有のもので、タンパク質に注目した解析から発見された耐性タンパク質（下記）はこれら固有の遺伝子にコードされているものが多く見つかっており、独自の遺伝子が耐性に重要な役割を果たしていると考えられています。<a href="https://doi.org/10.1038/ncomms12808" target="_blank">(Hashimoto <span style="font-style: italic;">et al., Nat Commun</span>, 2016)</a></p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">放射線から DNA を守る Dsup タンパク質</summary>
            <div class="img-pair" style="display: flex; gap: 15px; max-width: 1000px; margin: 0 auto;">
              <div style="flex: 815;">
                <img src="dsup1-ja.jpg" alt="Dsup1" style="display: block; width: 100%; height: auto; border-radius: 10px;">
              </div>
              <div style="flex: 966;">
                <img src="dsup2-ja.jpg" alt="Dsup2" style="display: block; width: 100%; height: auto; border-radius: 10px;">
              </div>
            </div>
            <p>高線量の放射線や完全乾燥は DNA に二重鎖切断を始めとする重篤な障害を発生させます。こうしたストレスに耐性を示すヨコヅナクマムシは DNA を正常に保つ機能が高いと推定され、DNA に結合しているタンパク質の１つとして Dsup (Damage suppressor; ダメージを抑制するもの）と名付けたタンパク質を分離同定しました。Dsup はクマムシ以外には見つからないタンパク質でしたが、Dsup 遺伝子を組み込んだヒト培養細胞は、X 線によるDNA障害が約40%低減し、通常の細胞が死ぬような線量を照射したあとも一部の細胞は生き残り、増殖することがわかりました。<a href="https://doi.org/10.1038/ncomms12808" target="_blank">(Hashimoto <span style="font-style: italic;">et al., Nat Commun</span>, 2016)</a></p>
            <p>　世界中の研究室が様々な生物に Dsup を導入した結果、<a href="https://doi.org/10.1016/j.isci.2023.106998" target="_blank">ショウジョウバエ</a>や<a href="https://doi.org/10.1126/sciadv.adx9669" target="_blank">線虫</a>、<a href="https://doi.org/10.1038/s41467-025-63652-3" target="_blank">酵母</a>、<a href="https://doi.org/10.1016/j.plaphy.2023.108184" target="_blank">稲</a>、<a href="https://doi.org/10.1007/s12033-020-00273-9" target="_blank">タバコ</a>といった生物でも DNA の保護効果を示すことが報告されています。</p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">ストレスに応答して線維化して細胞を守る CAHS タンパク質</summary>
            <video width="504" height="504" muted autoplay loop playsinline preload="true">
              <source src="deh-reh-ja-text.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
            <img src="cahs-ja.jpg" alt="Dsup" style="width: 100%; max-width:600px; height: auto; border-radius: 10px; display: block; margin: 0 auto;">
            <p>CAHSタンパク質もクマムシにしかないタンパク質ファミリーで2012年に当研究室により初めて同定されました。加熱しても沈殿しない性質を持ち、多くのクマムシ種で乾燥時に発現が顕著に増加します。近年、濃度上昇に伴って自発的に繊維を形成することが私たちを含む複数の研究室により独立に報告されました。私たちは、CAHSタンパク質が細胞内で脱水ストレスに応答して多数の繊維構造を形成し、細胞を物理的に強化してストレスから保護することを見出しました。この変化は可逆的でストレスがかかった時だけ、ちょうど鉄筋のような構造を細胞内に張り巡らせて守っているのではないかと考えています。<a href="https://doi.org/10.1371/journal.pbio.3001780" target="_blank">(Tanaka A <span style="font-style: italic;">et al., PLOS Biol</span>, 2022)</a></p>
          </details>
          <details name="tolerance">
            <summary class="hilite-summary">クマムシのゲノム編集技術を確立 ―耐性の謎に分子レベルで迫る―</summary>
            <img src="dipa-crispr-ja.jpg" alt="Dsup" style="width: 100%; max-width:600px; height: auto; border-radius: 10px; display: block; margin: 0 auto;">
            <p>2024年、長年垂涎の的だったクマムシの個体レベルでの遺伝子改変技術を確立しました。雌親の腹腔へCas9 RNPを注入することで、次世代で効率的に編集個体を得ることが可能です（DIPA-CRISPR）。現在、ノックアウトだけでなく、ssODNを用いたノックインにも成功しています。興味深いことに、得られた個体は編集配列をホモで保持していました。これは単為生殖特有の特殊な減数分裂機構に起因すると推測され、生物学的にも極めてユニークな現象です。<a href="https://doi.org/10.1371/journal.pgen.1011298" target="_blank">(Kondo <span style="font-style: italic;">et al., PLOS Genet</span>, 2024)</a></p>
            <p>　これまでに同定されている耐性遺伝子だけではクマムシと同じレベルの耐性能力を再現できていないことから、クマムシにはまだまだ未知の耐性遺伝子がたくさん眠っていると考えています。本技術により、クマムシの極限耐性を支える分子ロジックの解明が劇的に加速することが期待されます。</p>
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
