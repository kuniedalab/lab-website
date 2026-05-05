---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      text: |-
        <div style="position: relative; width: 100%;">
          <img src="/media/welcome.jpg" style="width: 100%; display: block;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 30%; background: rgba(0,0,0,0.4);"></div>
          <div style="position: absolute; top: 5%; left: 5%; text-align: left; color: white;">
            <h1 style="font-size: clamp(1.2rem, 4.5vw, 3rem); font-weight: bold; color: white;">生き抜くための分子ロジックを読み解く</h1>
            <p style="font-size: clamp(0.9rem, 3.5vw, 2rem); font-weight: bold;">〜 極限耐性の分子メカニズム 〜</p>
          </div>
        </div>
#  - block: hero
#    content:
#      title: 生き抜くための分子ロジックを解く
#      #image:
#      #  filename: welcome.jpg
#      text: |
#        *極限耐性の分子メカニズム*
#    design:
#      background:
#        image:
#          filename: welcome.jpg
#          filters:
#            brightness: 0.8
#          position: center
#          color: '#333'
#          parallax: false
#          size: cover
#        text_color_light: true
      
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
