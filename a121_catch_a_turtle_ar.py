# a121_catch_a_turtle_ar.py
import turtle as tt
import random as rng
import leaderboard as lb

# Setups
tcolor = "White"
tshape = "circle"
tt.bgcolor("Red")
tfont = ("Roboto", 20, "normal")
tsize = 3
score = 0
timer = 30
count = 1000
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, circle, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, circle, score)

# Turtle Thing
circle = tt.Turtle()
circle.color(tcolor)
circle.shapesize(tsize)
circle.shape(tshape)
circle.pu()
manage_leaderboard()
tc = tt.Turtle()
tc.color("Lime")
tc.pu()
tc.goto(-190, 140)
tc.hideturtle()
score_display = tt.Turtle()
score_display.pu()
score_display.goto(190, 140)
score_display.color("Lime")
score_display.hideturtle()
# Game Itself

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write("Clicks: " + str(score), font=tfont)

def countdown():
  global timer, timer_up
  tc.clear()
  if timer <= 0:
    tc.write("Time's Up", font=tfont)
    timer_up = True
  else:
    tc.write("Timer: " + str(timer), font=tfont)
    timer -= 1
    tc.getscreen().ontimer(countdown, count)

def when_clicked(i, j):
    global timer, tsize
    if (timer_up == False):
        circle.color("Red")
        circle.stamp()
        circle.color(tcolor)
        tsize -= .03
        circle.shapesize(tsize)
        update_score()
        change_position()
    else:
        circle.hideturtle()

def  change_position():
    new_xpos = rng.randint(-200, 200)
    new_ypos = rng.randint(-150, 150)
    circle.goto(new_xpos, new_ypos)

circle.onclick(when_clicked)
wn = tt.Screen()
wn.ontimer(countdown, count) 
wn.mainloop()