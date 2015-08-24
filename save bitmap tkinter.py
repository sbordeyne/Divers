def savebitmap(event):
   form = "Saving {0}%"
   img = PhotoImage(width = canvas_width, height = canvas_height)
   perc = -1
   for y in range(canvas_height):
      perc1 = (100*y) // canvas_height
      if perc1 != perc:
         perc = perc1
         setmessage(form.format(perc), True)
      row = "{"
      for x in range(canvas_width):
         ids = w.find_overlapping(x, y, x, y)
         color = w.itemcget(ids[-1], "fill") if ids else canvas_background
         row += color + " "
      img.put(row + "}", (0, y))
   img.write("kritzel.ppm", format="ppm")
   setmessage()