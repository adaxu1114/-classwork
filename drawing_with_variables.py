import arcade


WIDTH = 640
HEIGHT = 480


arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

#sun
arcade.draw_circle_filled(WIDTH-100, HEIGHT-100, 50, arcade.color.YELLOW)

#grass
arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, 100, arcade.color.GREEN)

#Tree 1
arcade.draw_triangle_filled(200, 125, 200+80, 125, 240, 200, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(WIDTH-230, 130, 410+80, 130, 450, 205, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(WIDTH-155, 130, 565, 130, 565-40, 205, arcade.color.DARK_GREEN)

#Tree 2
arcade.draw_xywh_rectangle_filled(200+30, 50, 20, 75, arcade.color.BROWN)
arcade.draw_xywh_rectangle_filled(WIDTH-200, 55, 20, 75, arcade.color.BROWN)
arcade.draw_xywh_rectangle_filled(WIDTH-125, 55, 20, 75, arcade.color.BROWN)



# End drawing
arcade.finish_render()
arcade.run()

