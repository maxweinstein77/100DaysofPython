sleep_hours = float(input("How many hours did you sleep for?"))
study_hours = float(input("How many hours did you study for?"))
exercise_hours = float(input("How many hours did you exercise for?"))

hours_in_day = 24
free_hours = hours_in_day - (sleep_hours + study_hours + exercise_hours)

print("Free hours:", free_hours)