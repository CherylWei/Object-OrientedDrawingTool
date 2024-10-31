"""
File: my_drawing.py
Name:Cheryl
----------------------
TODO:
"""
from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():    #background
    """
    Title: 晚霞獨釣 Fishing at sunset
    I've been quite busy recently,
    leaving me under considerable stress.
    As a way to cope, I envision myself as the angler in a painting,
    slowing down the pace of life and enjoying the tranquility of a sunset.
    """

    window = GWindow(width=800, height=400,title='晚霞獨釣')
    background=GRect(800,400,x=0,y=290)
    background.filled = True
    background.fill_color='#642A02'
    background.color='#642A02'
    sky=GRect(800,290)
    sky.filled=True
    sky.fill_color='#D36D3D'
    sky.color = '#D36D3D'


    #Cloud
    #Cluster 1
    cloud_1_1=GOval(120,80,x=40,y=50)
    cloud_1_1.filled = True
    cloud_1_1.fill_color = '#FFEFA1'
    cloud_1_1.color = '#FFEFA1'
    cloud_1_2=GOval(120,50,x=10,y=70)
    cloud_1_2.filled = True
    cloud_1_2.fill_color = '#FFEFA1'
    cloud_1_2.color = '#FFEFA1'
    cloud_1_3 = GOval(140, 60, x=70, y=60)
    cloud_1_3.filled = True
    cloud_1_3.fill_color = '#FFEFA1'
    cloud_1_3.color = '#FFEFA1'

    #Cloud Cluster 2
    cloud_2_1=GOval(140,90,x=550,y=50)
    cloud_2_1.filled = True
    cloud_2_1.fill_color = '#FFEFA1'
    cloud_2_1.color = '#FFEFA1'
    cloud_2_2=GOval(140,60,x=530,y=80)
    cloud_2_2.filled = True
    cloud_2_2.fill_color = '#FFEFA1'
    cloud_2_2.color = '#FFEFA1'
    cloud_2_3 = GOval(160, 60, x=590, y=80)
    cloud_2_3.filled = True
    cloud_2_3.fill_color = '#FFEFA1'
    cloud_2_3.color = '#FFEFA1'


    #sun
    sun=GOval(150,150,x=170,y=30)
    sun.filled = True
    sun.fill_color = '#FFB53C'
    sun.color = '#FFB53C'


    #mountain
    #GArc(寬 高 起點 增加角度)
    mountain_left = GArc(1000,1800,45,90,x=-150,y=160)
    mountain_left.color='#B12C25'
    mountain_left.filled=True
    mountain_left.fill_color='#B12C25'
    mountain_right = GArc(1100,1900,40,120,x=150,y=95)
    mountain_right.color='#CA4026'
    mountain_right.filled=True
    mountain_right.fill_color='#CA4026'


    #water_shadow
    #water_shadow_left
    water_shadow_1_1 = GLine(0, 300,150,300)
    water_shadow_1_1.color = '#FFEFA1'
    water_shadow_1_2 = GLine(0, 310,190,310)
    water_shadow_1_2.color = '#FFB53C'
    water_shadow_1_3 = GLine(0, 315,130,315)
    water_shadow_1_3.color = '#FFEFA1'
    water_shadow_1_4 = GLine(0, 325,240,325)
    water_shadow_1_4.color = '#FFEFA1'
    water_shadow_1_5 = GLine(0, 330,120,330)
    water_shadow_1_5.color = '#FFB53C'
    water_shadow_1_6 = GLine(0, 333,130,333)
    water_shadow_1_6.color = '#FFEFA1'

    #water_shadow_right
    water_shadow_2_1 = GLine(600, 320,800,320)
    water_shadow_2_1.color = '#FFB53C'
    water_shadow_2_2 = GLine(530, 325,800,325)
    water_shadow_2_2.color = '#FFEFA1'
    water_shadow_2_3 = GLine(500, 333,800,333)
    water_shadow_2_3.color = '#FFB53C'
    water_shadow_2_4 = GLine(750, 345,800,345)
    water_shadow_2_4.color = '#FFEFA1'
    water_shadow_2_5 = GLine(720, 348,800,348)
    water_shadow_2_5.color = '#FFEFA1'
    water_shadow_2_6 = GLine(630, 352,800,352)
    water_shadow_2_6.color = '#FFB53C'


    #boat
    boat=GPolygon()
    boat.add_vertex((430, 290))
    boat.add_vertex((500, 290))
    boat.add_vertex((520, 280))
    boat.add_vertex((520, 270))
    boat.add_vertex((410, 270))
    boat.add_vertex((410, 280))
    boat.add_vertex((430, 290))
    boat.filled = True
    boat.color = "#1F1F29"
    boat.fill_color = "#1F1F29"
    head=GOval(19,20,x=460,y=220)
    head.filled = True
    head.color = "#1F1F29"
    head.fill_color = "#1F1F29"
    body=GArc(95,120,0,75,x=442,y=240)
    body.filled = True
    body.color = "#1F1F29"
    body.fill_color = "#1F1F29"
    fishing_1=GLine(480, 255, 380, 240)
    fishing_2=GArc(480, 255, 0, -80,182, 176)
    fishing_3=GOval(13, 7,x=293, y=297)


    #birds
    bird_1=GPolygon()
    bird_1.add_vertex((300, 60))
    bird_1.add_vertex((284, 50))
    bird_1.add_vertex((300, 67))
    bird_1.add_vertex((318, 52))
    bird_1.filled = True
    bird_1.color = "#1F1F29"
    bird_1.fill_color = "#1F1F29"
    bird_2=GPolygon()
    bird_2.add_vertex((285, 32))
    bird_2.add_vertex((260, 22))
    bird_2.add_vertex((285, 40))
    bird_2.add_vertex((310, 28))
    bird_2.filled = True
    bird_2.color = "#1F1F29"
    bird_2.fill_color = "#1F1F29"
    bird_3=GPolygon()
    bird_3.add_vertex((360, 45)) #中間上點
    bird_3.add_vertex((320, 32)) #左點
    bird_3.add_vertex((360, 55)) #中間下點
    bird_3.add_vertex((400, 28)) #右點
    bird_3.filled = True
    bird_3.color = "#1F1F29"
    bird_3.fill_color = "#1F1F29"


    #add
    window.add(sky)
    window.add(sun)
    window.add(cloud_1_1)
    window.add(cloud_1_2)
    window.add(cloud_1_3)
    window.add(cloud_2_1)
    window.add(cloud_2_2)
    window.add(cloud_2_3)
    window.add(mountain_left)
    window.add(mountain_right)
    window.add(background)
    window.add(water_shadow_1_1)
    window.add(water_shadow_1_2)
    window.add(water_shadow_1_3)
    window.add(water_shadow_1_4)
    window.add(water_shadow_1_5)
    window.add(water_shadow_1_6)
    window.add(water_shadow_2_1)
    window.add(water_shadow_2_2)
    window.add(water_shadow_2_3)
    window.add(water_shadow_2_4)
    window.add(water_shadow_2_5)
    window.add(water_shadow_2_6)
    window.add(boat)
    window.add(head)
    window.add(body)
    window.add(fishing_1)
    window.add(fishing_2)
    window.add(fishing_3)
    window.add(bird_1)
    window.add(bird_2)
    window.add(bird_3)


if __name__ == '__main__':
    main()
