"""
File: scene.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: 
Extra: 
"""
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, 300, 150, 200)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, 150, 400, 400)
    draw_cloud(canvas, 700, 350, 400)
    draw_cloud(canvas, 450, 450, 400)
    draw_pine_tree(canvas, 600, 150, 250)
    draw_pine_tree(canvas, 700, 130, 250)
    draw_pine_tree(canvas, 650, 75, 250)
    draw_pine_tree(canvas, 400, 150, 250)
    draw_pine_tree(canvas, 500, 130, 250)
    draw_pine_tree(canvas, 450, 75, 250)
    draw_pine_tree(canvas, 800, 75, 250)
    draw_pine_tree(canvas, 900, 60, 250)
    draw_pine_tree(canvas, 750, 45, 250)
    draw_pine_tree(canvas, 550, 35, 250)
    draw_house(canvas, 100, 50, 250)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

#Objects in the sky.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="steelBlue1")
    draw_rectangle(canvas, 0, scene_height / 1.5, scene_width, scene_height, width=0, fill="steelBlue2")
    draw_rectangle(canvas, 0, scene_height / 1.2, scene_width, scene_height, width=0, fill="steelBlue3")
    draw_rectangle(canvas, 0, scene_height / 1.1, scene_width, scene_height, width=0, fill="steelBlue")
    draw_rectangle(canvas, 0, scene_height / 1.05, scene_width, scene_height, width=0, fill="steelBlue4")

def draw_cloud(canvas, center_x, bottom, height):
    #Main cloud body.
    main_cloud_width = height / 2
    main_cloud_height = height / 6
    main_cloud_left = center_x - main_cloud_width / 2
    main_cloud_bottom = bottom
    main_cloud_right = center_x + main_cloud_width / 2
    main_cloud_top = bottom + main_cloud_height
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "honeydew2")
    #Left nub of cloud.
    main_cloud_width = height / 12
    main_cloud_height = height / 8
    main_cloud_left = (center_x - main_cloud_width / 2) - 100
    main_cloud_bottom = bottom - 10
    main_cloud_right = center_x + main_cloud_width / 2
    main_cloud_top = (bottom + main_cloud_height) - 10
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "honeydew1")
    #Right nub of cloud.
    main_cloud_width = height / 12
    main_cloud_height = height / 8
    main_cloud_left = (center_x - main_cloud_width / 2)
    main_cloud_bottom = bottom - 25
    main_cloud_right = center_x + main_cloud_width / 2 + 100
    main_cloud_top = (bottom + main_cloud_height) - 25
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "ivory1")
    
def draw_sun(canvas, center_x, bottom, height):
    #Fourth color layer.
    main_sun_width = height / 2 + 75
    main_sun_height = height / 2 + 75
    main_sun_left = center_x - main_sun_width / 2
    main_sun_bottom = bottom - 30
    main_sun_right = center_x + main_sun_width / 2
    main_sun_top = bottom + main_sun_height - 30
    draw_oval(canvas, main_sun_left, main_sun_bottom, main_sun_right, main_sun_top, width = 0, fill = "darkGoldenRod")
    #Third color layer.
    main_sun_width = height / 2 + 50
    main_sun_height = height / 2 + 50
    main_sun_left = center_x - main_sun_width / 2
    main_sun_bottom = bottom - 20
    main_sun_right = center_x + main_sun_width / 2
    main_sun_top = bottom + main_sun_height - 20
    draw_oval(canvas, main_sun_left, main_sun_bottom, main_sun_right, main_sun_top, width = 0, fill = "darkGoldenRod3")
    #Secondary color layer.
    main_sun_width = height / 2 + 25
    main_sun_height = height / 2 + 25
    main_sun_left = center_x - main_sun_width / 2
    main_sun_bottom = bottom - 10
    main_sun_right = center_x + main_sun_width / 2
    main_sun_top = bottom + main_sun_height - 10
    draw_oval(canvas, main_sun_left, main_sun_bottom, main_sun_right, main_sun_top, width = 0, fill = "darkGoldenRod2")
    #Main sun body.
    main_sun_width = height / 2
    main_sun_height = height / 2
    main_sun_left = center_x - main_sun_width / 2
    main_sun_bottom = bottom
    main_sun_right = center_x + main_sun_width / 2
    main_sun_top = bottom + main_sun_height
    draw_oval(canvas, main_sun_left, main_sun_bottom, main_sun_right, main_sun_top, width = 0, fill = "darkGoldenRod1")

#Objects on the ground.
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0 , scene_width, scene_height - 300, width = 0, fill = "oliveDrab1")
    draw_rectangle(canvas, 0, 0 , scene_width, scene_height - 400, width = 0, fill = "oliveDrab2")
    draw_rectangle(canvas, 0, 0 , scene_width, scene_height - 440, width = 0, fill = "oliveDrab3")
    draw_rectangle(canvas, 0, 0 , scene_width, scene_height - 470, width = 0, fill = "oliveDrab4")
    draw_rectangle(canvas, 0, 0 , scene_width, scene_height - 490, width = 0, fill = "darkOliveGreen")

def draw_pine_tree(canvas, center_x, bottom, height):
    #Trunk of tree.
    trunk_width = height / 8
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    top_trunk = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, top_trunk, width = 2, outline = "darkGoldenrod4", fill = "darkGoldenrod")
    #Skirt of tree.
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = top_trunk
    skirt_center = center_x
    skirt_top = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, width = 2, outline="darkGreen", fill="forestGreen")

def draw_house(canvas, center_x, bottom, height):
    #Main section of home.
    house_width = height / 1.5
    house_height = height / 1.5
    left_house = center_x - house_width / 2
    bottom_house = bottom
    right_house = center_x + house_width / 2
    top_house = bottom + house_height
    draw_rectangle(canvas, left_house, bottom_house, right_house, top_house, width = 1, fill = "tan2")
    #Main section door.
    door_width = height / 3.5
    door_height = height / 3.5
    left_door = center_x - door_width / 3.5
    bottom_door = bottom
    right_door = center_x + door_width / 3.5
    top_door = bottom + door_height
    draw_rectangle(canvas, left_door, bottom_door, right_door, top_door, width = 1, outline = "black", fill = "orange4")
    #Main section door knob.
    doorknob_width = height / 10
    doorknob_height = height / 25
    left_doorknob = (center_x - doorknob_width / 10) + 15
    bottom_doorknob = bottom + 30
    right_doorknob = (center_x + doorknob_width / 10) + 15
    top_doorknob = bottom + doorknob_height + 30
    draw_oval(canvas, left_doorknob, bottom_doorknob, right_doorknob, top_doorknob, width = 0, outline = "darkGoldenrod4", fill = "gold1")
    #Main section window left.
    window1_width = height / 3.5
    window1_height = height / 6
    left_window1 = (center_x - window1_width / 3.5) - 40
    bottom_window1 = bottom + 100
    right_window1 = (center_x + window1_width / 3.5) - 40
    top_window1 = (bottom + window1_height) + 100
    draw_rectangle(canvas, left_window1, bottom_window1, right_window1, top_window1, width = 2, outline = "white", fill = "lightBlue1")
    #Main section window right.
    window2_width = height / 3.5
    window2_height = height / 6
    left_window2 = (center_x - window2_width / 3.5) + 40
    bottom_window2 = bottom + 100
    right_window2 = (center_x + window2_width / 3.5) + 40
    top_window2 = (bottom + window2_height) + 100
    draw_rectangle(canvas, left_window2, bottom_window2, right_window2, top_window2, width = 2, outline = "white", fill = "lightBlue1")
    #Main section roof.
    main_roof_x0 = (center_x - house_width / 2)
    main_roof_y0 = bottom + 168
    main_roof_x1 = (center_x - house_width / 2) + 82.5
    main_roof_y1 = bottom + 250
    main_roof_x2 = (center_x - house_width / 2) + 165
    main_roof_y2 = bottom + 168
    draw_polygon(canvas,main_roof_x0,main_roof_y0,main_roof_x1,main_roof_y1,main_roof_x2,main_roof_y2, width = 0, fill = "orange4")

    #Side section of home.
    house_width_side = height / 2
    house_height_side = height / 2
    left_house_side = (center_x - house_width_side / 2) + 145
    bottom_house_side = bottom
    right_house_side = (center_x + house_width_side / 2) + 145
    top_house_side = bottom + house_height_side
    draw_rectangle(canvas, left_house_side, bottom_house_side, right_house_side, top_house_side, width = 1, fill = "tan1")
    #Side section window left.
    window3_width = height / 3.5
    window3_height = height / 6
    left_window3 = (center_x - window3_width / 3.5) + 115
    bottom_window3 = bottom + 50
    right_window3 = (center_x + window3_width / 3.5) + 115
    top_window3 = (bottom + window3_height) + 50
    draw_rectangle(canvas, left_window3, bottom_window3, right_window3, top_window3, width = 2, outline = "white", fill = "lightBlue1")
    #Side section window right.
    window4_width = height / 3.5
    window4_height = height / 6
    left_window4 = (center_x - window4_width / 3.5) + 175
    bottom_window4 = bottom + 50
    right_window4 = (center_x + window4_width / 3.5) + 175
    top_window4 = (bottom + window4_height) + 50
    draw_rectangle(canvas, left_window4, bottom_window4, right_window4, top_window4, width = 2, outline = "white", fill = "lightBlue1")
    #Side section roof.
    side_roof_x0 = (center_x - house_width / 2) + 166
    side_roof_y0 = bottom + 125
    side_roof_x1 = (center_x - house_width / 2) + 166
    side_roof_y1 = bottom + 168
    side_roof_x2 = (center_x - house_width / 2) + 292
    side_roof_y2 = bottom + 125
    draw_polygon(canvas,side_roof_x0,side_roof_y0,side_roof_x1,side_roof_y1,side_roof_x2,side_roof_y2, width = 0, fill = "orange4")

# Call the main function so that
# this program will start executing.
main()