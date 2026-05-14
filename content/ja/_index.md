---
# Leave the homepage title empty to use the site title
title: 
date: 2022-10-24
type: landing

sections:
#  - block: markdown
#    content:
#      text: |-
#        <div style="position: relative; width: 100%;">
#          <img src="/media/welcome.jpg" style="width: 100%; display: block;">
#          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 30%; background: rgba(0,0,0,0.4);"></div>
#          <div style="position: absolute; top: 5%; left: 5%; text-align: left; color: white;">
#            <h1 style="font-size: clamp(1.2rem, 4.5vw, 3rem); font-weight: bold; color: white;">生き抜くための分子ロジックを読み解く</h1>
#            <p style="font-size: clamp(0.9rem, 3.5vw, 2rem); font-weight: bold;">〜 極限耐性の分子メカニズム 〜</p>
#          </div>
#        </div>
  - block: hero
    content:
      title: "生き抜くための分子ロジックを読み解く<span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.8em; opacity: 0.7; margin-top: -0.35em;'>Decoding Molecular Logic of Survival</span><span style='display: block; font-size: 0.7em; margin-top: 0.5em;'>ー 極限耐性の分子メカニズム ー</span><span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.6em; opacity: 0.7; margin-top: -0.3em;'>Mechanisms of Extreme Tolerance</span>"
      
      #"生き抜くための分子ロジックを読み解く<span style='display: block; font-size: 0.7em; margin-top: -0.2em;'>ー 極限耐性の分子メカニズム ー</span><span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.8em; opacity: 0.8; margin-top: 0.2em;'>Decoding Molecular Logic of Survival</span><span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.6em; opacity: 0.8; margin-top: -0.3em;'>- Mechanisms of Extreme Tolerance -</span>"
      
      #"生き抜くための分子ロジックを読み解く<span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.8em; opacity: 0.7; margin-top: -0.35em;'>Decoding molecular logic of survival</span><span style='display: block; font-size: 0.7em; margin-top: 0.2em;'>ー 極限耐性の分子メカニズム ー</span><span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.6em; opacity: 0.7; margin-top: -0.3em;'>Mechanisms of Extreme Tolerance</span>"
      
      #  filename: welcome.jpg
      text: |
        <br><br>
        クマムシやワムシなどの極限耐性生物を材料に、完全乾燥や極限ストレスに耐える仕組みを分子レベルで解き明かします。さらに、その知見をヒト細胞をはじめとする他種生物の耐性向上や、生体分子の乾燥保存へ応用展開しています。<br><br>

        <div style="display: flex; gap: 0px; flex-wrap: wrap; justify-content: flex-start; margin-bottom: -20px; line-height: 1;">
        <a href="./tardigrade/" class="btn btn-green-color btn-lg">
          <i class="fas fa-microscope mr-1"></i> クマムシとは？
        </a>
        <a href="./tolerance/" class="btn btn-green-color btn-lg">
          <i class="fas fa-shield-alt mr-1"></i> 耐性のメカニズム
        </a>
        <a href="./rotifer/" class="btn btn-lg btn-green-color">
          <i class="fas fa-spinner mr-1"></i> ワムシとは？
        </a>
        <a href="https://www.sci.u-hyogo.ac.jp/life/biosig/japanese/yan_jiu_nei_rong.html" class="btn btn-lg btn-green-color">
          <i class="fas fa-arrows-spin mr-1"></i> 細胞周期
        </a>
        </div><br>
        
    design:
      background:
        image:
          filename: kumanui2.jpg
          filters:
            brightness: 0.5
          position: left
          color: '#333'
          parallax: false
          size: cover
        text_color_light: true
  
  - block: markdown
    content:
      text: |
        🚚❗國枝研（くまむし研究グループ）は2025年4月に兵庫県立大学理学研究科に移動しました。<br>
    design:
      # 上下左右の余白を最小限にする [上, 右, 下, 左]
      spacing:
        padding: ["20px", "0", "50px", "0"]
      # カラムを1にすると、タイトル分のスペースが消えます
      columns: "1"
      
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 3
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news
    design:
      view: card
      columns: '1'
      spacing:
        padding: ["20px", "0", "50px", "0"]
  
#  - block: markdown
#    content:
#      title:
#      subtitle: ''
#      text:
#    design:
#      columns: '1'
#      background:
#        image: 
#          filename: coders.jpg
#          filters:
#            brightness: 1
#          parallax: false
#          position: center
#          size: cover
#          text_color_light: true
#      spacing:
#        padding: ['30px', '0', '20px', '0']
#      css_class: fullscreen

  - block: collection
    content:
      title: Latest Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        #publication_type: 'article'
    design:
      view: citation
      columns: '1'
      spacing:
        padding: ["20px", "0", "50px", "0"]

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; gap: 0px; flex-wrap: wrap; justify-content: center; line-height: 1;">
        <a href="./news/" class="btn btn-blue-color btn-lg">
          <i class="fas fa-seedling mr-1"></i> News
        </a>
        <a href="./publication/" class="btn btn-blue-color btn-lg">
          <i class="fas fa-file-alt mr-1"></i> Publications
        </a>
        <a href="./member/" class="btn btn-blue-color btn-lg">
          <i class="fas fa-users mr-1"></i> Meet the team
        </a>
        <a href="./contact/" class="btn btn-blue-color btn-lg">
          <i class="fas fa-paper-plane mr-1"></i> Contact the lab-head
        </a>
        </div>
      #  {{% cta cta_link="./member/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
      spacing:
        padding: ["20px", "0", "20px", "0"]
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
---
