---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: "<span style='letter-spacing: 0em; font-weight: bold;'>Decoding Molecular Logic of Survival</span><span style='display: block; letter-spacing: 0em; font-weight: normal; font-size: 0.7em; margin-top: -0.25em;'>- Mechanisms of Extreme Tolerance -</span>"
      #image:
      #  filename: welcome.jpg
      #  <h2 style="font-style: italic; ">- Mechanisms of Extreme Tolerance -</h2>
      text: |
        <br>
        We study extremotolerant organisms, including tardigrades, to elucidate the molecular mechanisms that enable survival under extreme stresses. We further apply these insights to enhance stress tolerance in other organisms, including human cells, and to protect biomolecules from drying.<br>

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
