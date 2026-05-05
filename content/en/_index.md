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
      title: Decoding Molecular Logic of Survival
      #image:
      #  filename: welcome.jpg
      text: |
        <h2 style="font-style: italic; ">- Mechanisms of Extreme Tolerance -</h2>
        <br>
        We study extremotolerant organisms, including tardigrades, to elucidate the molecular mechanisms that enable survival under extreme stresses. We further apply these insights to enhance stress tolerance in other organisms, including human cells, and to protect biomolecules from drying.
#        完全乾燥に耐えるクマムシやワムシなどの極限環境耐性生物を対象に、新規耐性因子や独自の耐性メカニズムの解明に取り組んでいます。さらに、得られた知見をヒト細胞をはじめとする他種生物の耐性向上や、生体分子の乾燥保護へ応用展開しています。
    design:
      background:
        image:
          filename: kumanui2.jpg
          filters:
            brightness: 0.5
          position: center
          color: '#333'
          parallax: false
          size: cover
        text_color_light: true
      
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 2
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
#        padding: ['20px', '0', '20px', '0']
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

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./member/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
