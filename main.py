
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
        create = Create_workout()
        create.workout_infos['name'] = create.ask_workout_name()
        break
      elif user_option in ['2', 'edit', 'edit workout']:
        print('edit workout')
        break
      elif user_option in ['3', 'delete', 'delete workout']:
        print('delete workout')
        break
      elif user_option in ['4', 'list', 'list workout']:
        print('exit')
        break
      elif user_option in ['5', 'exit']:
        print('exit')
        break
      else:
        print('invalid option')
        break

  
class Create_workout():
  create_workout_messages = {
    'name': 'What is the name of the workout?\n\n',
    'name_error': 'Workout name cannot be empty!\n',
    #'days': '0) Monday\n1) Tuesday\n2) Wednesday\n3) Thursday\n4) Friday\n5) Saturday\n6) Sunday\n\n',
    'choose_day': 'Choose the day:\n',
    'choose_day_or_done': 'Choose another day or type [d]one: '
  }

  def __init__(self):
    self.workout_infos = {}
      # 'name': '',
      # 'days': {
      #   'monday': {
      #     'name': '',
      #     'exercises': [
      #       {'name': '', 'series': '', 'reps': ''}
      #     ]
      #   },
      #   'tuesday': {},
      #   'wednesday': {},
      #   'thursday': {},
      #   'friday': {},
      #   'saturday': {},
      #   'sunday': {}
      # }

  def ask_workout_name(self):
    name = ''
    while not name:
      name_typing = input(self.create_workout_messages['name'])
      if len(name_typing) < 1:
        print(self.create_workout_messages['name_error'])
        continue
      else:
        name = name_typing.strip().title()
    return name
    

Menu()
