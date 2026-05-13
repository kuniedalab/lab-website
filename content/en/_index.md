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
        <br><br>
        We study extremotolerant organisms, including tardigrades, to elucidate the molecular mechanisms that enable survival under extreme stresses. We further apply these insights to enhance stress tolerance in other organisms, including human cells, and to protect biomolecules from drying.<br><br><br><br>

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
