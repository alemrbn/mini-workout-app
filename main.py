
all_workouts = []

class Menu():
  main_menu_messages = {
      'welcome': '-== welcome! ==-\n',
      'options': '1. Create workout\n2. Edit workout\n3. Delete workout\n4. List workouts\n5. Exit\n\n'
    }
  
  def __init__(self):
    self.loop_menu()

  def loop_menu(self):
    print(Menu.main_menu_messages['welcome'])

    while True:
      user_option = input(Menu.main_menu_messages['options'])
      user_option = user_option.lower().strip()

      print()

      if user_option in ['1', 'create', 'create workout']:
        create_workout = CreateWorkout()
        create_workout.build_workout()
        all_workouts.append(create_workout.workout_data)
      elif user_option in ['2', 'edit', 'edit workout']:
        print('edit workout')
        break
      elif user_option in ['3', 'delete', 'delete workout']:
        print('delete workout')
        break
      elif user_option in ['4', 'list', 'list workout']:
        list_workout = ListWorkout()
        list_workout.list_workouts()
      elif user_option in ['5', 'exit']:
        print('exit')
        break
      else:
        print('invalid option')
        break

  
class CreateWorkout():
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  create_workout_messages = {
    'ask_workout_name': 'What is the name of the workout? ',
    'invalid_workout_name': 'Enter a valid name.',
    'ask_exercise_name': 'What is the exercise name? ',
    'invalid_exercise_name': 'Enter a valid exercise name.',
    'ask_another_exercise': 'Add another exercise for this day? [y]es or [n]ot: ',
    'ask_exercise_series': 'How many series? ',
    'empty_exercise_series': 'You must enter at least one series',
    'ask_exercise_reps_min': 'How many minimum reps? ',
    'ask_exercise_reps_max': 'How many maximum reps? ',
    'invalid_exercise_reps': 'One or both inputs invalid.',
    'available_days': 'Available days:',
    'choose_day': 'Choose the day or type [d]one if finished: ',
    'no_days_selected': 'You need to select at least one day.',
    'invalid_day': 'Select a valid day.',
    'complete_workout': '\nWorkout creation complete!\n'
  }

  def __init__(self):
    self.workout_data = {}

  def ask_workout_name(self):
    workout_name = ''
    while not workout_name:
      workout_name_input = input(self.create_workout_messages['ask_workout_name']).strip()
      if workout_name_input.isdigit() or len(workout_name_input) < 1:
        print(self.create_workout_messages['invalid_workout_name'])
        continue
      else:
        workout_name = workout_name_input.strip().title()
    return workout_name

  def ask_exercise_name(self):
    exercise_name = ''
    while not exercise_name:
      exercise_name_input = input(self.create_workout_messages['ask_exercise_name']).strip()
      if exercise_name_input.isdigit() or len(exercise_name_input) < 1:
        print(self.create_workout_messages['invalid_exercise_name'])
        continue
      else:
        exercise_name = exercise_name_input.title()
    return exercise_name

  def ask_exercise_series(self):
    exercise_series = 0
    while exercise_series <= 0:
      exercise_series_input = input(self.create_workout_messages['ask_exercise_series']).strip()
      if not exercise_series_input.isdigit():
        print(self.create_workout_messages['empty_exercise_series'])
        continue
      exercise_series = int(exercise_series_input)
    return exercise_series
  
  def ask_exercise_reps(self):
    exercise_reps_min = 0
    exercise_reps_max = 0
    while exercise_reps_min <= 0 or exercise_reps_max <= 0:
      exercise_reps_min_input = input(self.create_workout_messages['ask_exercise_reps_min']).strip()
      exercise_reps_max_input = input(self.create_workout_messages['ask_exercise_reps_max']).strip()
      check_inputs_is_digit = not exercise_reps_min_input.isdigit() or not exercise_reps_max_input.isdigit()
      check_inputs_is_empty = exercise_reps_min_input == '' or exercise_reps_max_input == ''
      if check_inputs_is_digit or check_inputs_is_empty:
        print(self.create_workout_messages['invalid_exercise_reps'])
        continue
      exercise_reps_min_input_int = int(exercise_reps_min_input)
      exercise_reps_max_input_int = int(exercise_reps_max_input)
      exercise_reps_min = exercise_reps_min_input_int
      exercise_reps_max = exercise_reps_max_input_int
    return exercise_reps_min, exercise_reps_max
  
  def build_workout(self):
    workout_name = self.ask_workout_name()
    self.workout_data['name'] = workout_name
    self.workout_data['days'] = {}
    available_days = self.days.copy()
    while available_days:
      print(self.create_workout_messages['available_days'])
      for i, day in enumerate(available_days):
        print(f"{i}) {day.capitalize()}")
      print()
      day_input = input(self.create_workout_messages['choose_day']).strip().lower()
      chosen_day = None
      if day_input in ['d', 'done']:
        if not self.workout_data['days']:
          print(self.create_workout_messages['no_days_selected'])
          continue
        break
      if day_input == '':
        print(self.create_workout_messages['invalid_day'])
        continue
      if day_input.isdigit():
        index = int(day_input)
        if index >= 0 and index < len(available_days):
          chosen_day = available_days[index]
        else:
          print(self.create_workout_messages['invalid_day'])
          continue
      elif day_input in available_days:
        chosen_day = day_input
      else:
        print(self.create_workout_messages['invalid_day'])
        continue
      self.workout_data['days'][chosen_day] = {'exercises': []}
      while True:
        exercise_name = self.ask_exercise_name()
        series = self.ask_exercise_series()
        reps_min, reps_max = self.ask_exercise_reps()
        self.workout_data['days'][chosen_day]['exercises'].append({
          'name': exercise_name,
          'series': series,
          'reps_min': reps_min,
          'reps_max': reps_max
        })
        add_another = input(self.create_workout_messages['ask_another_exercise']).strip().lower()
        if add_another not in ['y', 'yes']:
          break
      available_days.remove(chosen_day)
    print(self.create_workout_messages['complete_workout'])
      
class ListWorkout():
  list_workout_messages = {
    'listed': 'Workouts',
    'back': 'type [b]ack to back ',
    'view_workout': 'What workout would you like to view? ',
    'invalid_workout': 'Invalid workout!',
    'empty_workout': 'No one workout for list.\n'
  }

  def __init__(self):
    pass

  def list_workouts(self):
    available_workouts = len(all_workouts)
    if self.check_empty_workout(available_workouts):
      return
    print(self.list_workout_messages['listed'], f'({available_workouts}):')
    while True:
      print()
      for i, workout in enumerate(all_workouts):
        print(f'{i})', workout['name'])
      print(f"\n{self.list_workout_messages['back']}")
      workout_input = input(self.list_workout_messages['view_workout'])
      if workout_input in ['b', 'back']:
        break
      if workout_input.isdigit():
        index = int(workout_input)
        if index >= 0 and index < available_workouts:
          selected_workout = all_workouts[index]
          while True:
            print(self.format_workout(selected_workout))
            back = input(f"{self.list_workout_messages['back']}")
            if back in ['b', 'back']:
              break
        else:
          print(self.list_workout_messages['invalid_workout'])
          continue

  def check_empty_workout(self, workouts):
    if workouts == 0:
      print(self.list_workout_messages['empty_workout'])
      return True
    return False
  
  def format_workout(self, workout):
    workout_name = f"Workout: {workout['name']}\n"
    output = workout_name
    for day, info in workout['days'].items():
      output += f'\n{day.capitalize()}:\n'
      for exercises in info['exercises']:
        output += f"  - {exercises['name']}: {exercises['series']} series x {exercises['reps_min']}-{exercises['reps_max']} reps\n"
    return output

Menu()
