from utils import (
    clear_screen,
    global_messages,
    check_empty_list,
    list_workouts
)

all_workouts = []


class CreateWorkout:
    DAYS = ['monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday'
            ]

    CREATE_WORKOUT_MESSAGES = {
        'ask_workout_name': 'What is the workout name? ',
        'invalid_workout_name': 'Please enter a valid name.',
        'ask_exercise_name': 'Enter the exercise name: ',
        'invalid_exercise_name': 'Please enter a valid exercise name.',
        'ask_another_exercise': (
            'Add another exercise for this day? '
            '[y]es / [n]o: '
        ),
        'ask_exercise_series': 'How many sets? ',
        'empty_exercise_series': 'You must enter at least one set.',
        'ask_exercise_reps_min': 'Minimum reps: ',
        'ask_exercise_reps_max': 'Maximum reps: ',
        'invalid_exercise_reps': 'Invalid input. Please enter valid numbers.',
        'available_days': 'Available days:\n',
        'choose_day': '\nChoose a day or type [d]one to finish: ',
        'no_days_selected': 'You must select at least one day.',
        'invalid_day': 'Please choose a valid day.',
        'complete_workout': 'Workout created successfully!'
    }

    def __init__(self):
        self.workout_data = {}

    def ask_workout_name(self):
        clear_screen()
        workout_name = ''
        while not workout_name:
            workout_name_input = input(
                self.CREATE_WORKOUT_MESSAGES['ask_workout_name']
                ).strip()
            if workout_name_input.isdigit() or len(workout_name_input) < 1:
                print(self.CREATE_WORKOUT_MESSAGES['invalid_workout_name'])
                continue
            else:
                workout_name = workout_name_input.strip().title()
        return workout_name

    def ask_exercise_name(self):
        clear_screen()
        exercise_name = ''
        while not exercise_name:
            exercise_name_input = input(
                self.CREATE_WORKOUT_MESSAGES['ask_exercise_name']
                ).strip()
            if exercise_name_input.isdigit() or len(exercise_name_input) < 1:
                print(self.CREATE_WORKOUT_MESSAGES['invalid_exercise_name'])
                continue
            else:
                exercise_name = exercise_name_input.title()
        return exercise_name

    def ask_exercise_series(self):
        clear_screen()
        exercise_series = 0
        while exercise_series <= 0:
            exercise_series_input = input(
                self.CREATE_WORKOUT_MESSAGES['ask_exercise_series']
                ).strip()
            if not exercise_series_input.isdigit():
                print(self.CREATE_WORKOUT_MESSAGES['empty_exercise_series'])
                continue
            exercise_series = int(exercise_series_input)
        return exercise_series

    def ask_exercise_reps(self):
        clear_screen()
        exercise_reps_min = 0
        exercise_reps_max = 0
        while exercise_reps_min <= 0 or exercise_reps_max <= 0:
            exercise_reps_min_input = input(
                self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_min']
                ).strip()
            exercise_reps_max_input = input(
                self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_max']
                ).strip()
            check_inputs_is_digit = (
                not exercise_reps_min_input.isdigit() or
                not exercise_reps_max_input.isdigit()
                )
            check_inputs_is_empty = (
                exercise_reps_min_input == '' or
                exercise_reps_max_input == ''
                )
            if check_inputs_is_digit or check_inputs_is_empty:
                print(self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps'])
                continue
            exercise_reps_min_input_int = int(exercise_reps_min_input)
            exercise_reps_max_input_int = int(exercise_reps_max_input)
            exercise_reps_min = exercise_reps_min_input_int
            exercise_reps_max = exercise_reps_max_input_int
        return exercise_reps_min, exercise_reps_max

    def build_workout(self):
        workout_name = self.ask_workout_name()
        clear_screen()
        self.workout_data['name'] = workout_name
        self.workout_data['days'] = {}
        available_days = self.DAYS.copy()
        while available_days:
            print(self.CREATE_WORKOUT_MESSAGES['available_days'])
            for i, day in enumerate(available_days):
                print(f"{i}) {day.capitalize()}")
            day_input = input(
                self.CREATE_WORKOUT_MESSAGES['choose_day']
                ).strip().lower()
            chosen_day = None
            if day_input in ['d', 'done']:
                if not self.workout_data['days']:
                    clear_screen()
                    print(self.CREATE_WORKOUT_MESSAGES['no_days_selected'])
                    continue
                break
            if day_input.isdigit():
                index = int(day_input)
                if index >= 0 and index < len(available_days):
                    chosen_day = available_days[index]
                else:
                    clear_screen()
                    print(self.CREATE_WORKOUT_MESSAGES['invalid_day'])
                    continue
            elif day_input in available_days:
                chosen_day = day_input
            else:
                clear_screen()
                print(self.CREATE_WORKOUT_MESSAGES['invalid_day'])
                continue
            self.workout_data['days'][chosen_day] = {'exercises': []}
            ask_workout_infos_flag = True
            while ask_workout_infos_flag:
                exercise_name = self.ask_exercise_name()
                series = self.ask_exercise_series()
                reps_min, reps_max = self.ask_exercise_reps()
                self.workout_data['days'][chosen_day]['exercises'].append({
                    'name': exercise_name,
                    'series': series,
                    'reps_min': reps_min,
                    'reps_max': reps_max
                })
                clear_screen()
                ask_another_loop_flag = True
                while ask_another_loop_flag:
                    add_another = input(
                        self.CREATE_WORKOUT_MESSAGES['ask_another_exercise']
                        ).strip().lower()
                    if add_another in ['y', 'yes']:
                        clear_screen()
                        ask_another_loop_flag = False
                    elif add_another in ['no', 'n']:
                        clear_screen()
                        ask_another_loop_flag = False
                        ask_workout_infos_flag = False
                    else:
                        continue
            available_days.remove(chosen_day)
        clear_screen()
        print(self.CREATE_WORKOUT_MESSAGES['complete_workout'])


class EditWorkout:
    EDIT_WORKOUT_MESSAGES = {
        'ask_edit_workout': 'Which workout do you want to edit? ',
        'invalid_edit_workout_option': 'Invalid option.',
        'available_for_edit': 'Available for editing:\n',
        'ask_edit_workout_item': 'Which item do you want to edit? ',
        'ask_new_workout_name':  'What name would you like to use? '
    }

    def __init__(self):
        pass

    def edit_workout(self):
        clear_screen()
        if check_empty_list(all_workouts):
            return
        listing = True
        while listing:
            print(
                list_workouts(
                    global_messages['listed_workouts'],
                    all_workouts
                )
            )
            for i, workout in enumerate(all_workouts):
                print(f'{i})', workout['name'])
            print(f"\n{global_messages['back']}")
            edit_input = input(self.EDIT_WORKOUT_MESSAGES['ask_edit_workout'])
            clear_screen()
            if edit_input in ['b', 'back']:
                listing = False
                print(global_messages['welcome'])
                continue
            if edit_input.isdigit():
                index = int(edit_input)
                if index >= 0 and index < len(all_workouts):
                    selected_workout = all_workouts[index]
                    editing = True
                    while editing:
                        under_development = (
                            '-== This menu is still under development.. ==-\n'
                        )
                        print(under_development)
                        available_options = ['rename workout']
                        workout_name_msg = (
                            f"Workout: {selected_workout['name']}\n"
                        )
                        print(workout_name_msg)
                        print(self.EDIT_WORKOUT_MESSAGES['available_for_edit'])
                        for i, option in enumerate(available_options):
                            print(f'{i}) {option.title()}')
                        print(f"\n{global_messages['back']}")
                        edit_input_option = input(
                            self.EDIT_WORKOUT_MESSAGES['ask_edit_workout_item']
                        )
                        if edit_input_option in ['b', 'back']:
                            clear_screen()
                            break
                        if edit_input_option == '0':
                            self.rename_workout(
                                selected_workout,
                                workout_name_msg
                            )
                        else:
                            clear_screen()
                            print(
                                self.EDIT_WORKOUT_MESSAGES[
                                    'invalid_edit_workout_option'
                                ]
                            )
                else:
                    print(global_messages['invalid_workout'])
            else:
                print(global_messages['invalid_workout'])

    def rename_workout(self, workout, title_msg):
        rename_workout_flag = True
        while rename_workout_flag:
            clear_screen()
            print(title_msg)
            new_workout_name = input(
                self.EDIT_WORKOUT_MESSAGES['ask_new_workout_name']
                )
            workout['name'] = new_workout_name.title().strip()
            rename_workout_flag = False
            clear_screen()


class DeleteWorkout:
    DELETE_WORKOUT_MESSAGES = {
        'ask_delete': 'Which workout do you wish to delete? ',
        'ask_sure_delete': (
            'Are you sure? This action is irreversible! '
            '[y]es / [n]o '),
        'successfully_deleted': 'Workout successfully deleted!'
    }

    def __init__(self):
        pass

    def delete_workout(self):
        clear_screen()
        if check_empty_list(all_workouts):
            return
        listing = True
        while listing:
            print(
                list_workouts(
                    global_messages['listed_workouts'],
                    all_workouts
                )
            )
            for i, workout in enumerate(all_workouts):
                print(f'{i})', workout['name'])
            print(f"\n{global_messages['back']}")
            delete_input = input(self.DELETE_WORKOUT_MESSAGES['ask_delete'])
            clear_screen()
            if delete_input in ['b', 'back']:
                listing = False
                print(global_messages['welcome'])
                continue
            user_response = False
            if delete_input.isdigit():
                index = int(delete_input)
                if index >= 0 and index < len(all_workouts):
                    while not user_response:
                        sure_or_not = input(
                            self.DELETE_WORKOUT_MESSAGES['ask_sure_delete']
                            )
                        if sure_or_not in ['y', 'yes']:
                            del all_workouts[index]
                            user_response = True
                            listing = False
                            clear_screen()
                            print(
                                self.DELETE_WORKOUT_MESSAGES[
                                    'successfully_deleted'
                                    ]
                                )
                        elif sure_or_not in ['n', 'no']:
                            user_response = True
                            clear_screen()
                        else:
                            continue
                else:
                    print(global_messages['invalid_workout'])
            else:
                print(global_messages['invalid_workout'])


class ListWorkout:
    LIST_WORKOUT_MESSAGES = {
        'view_workout': 'Which workout would you like to view? '
    }

    def __init__(self):
        pass

    def list_workouts(self):
        clear_screen()
        if check_empty_list(all_workouts):
            return
        while True:
            print(
                list_workouts(
                    global_messages['listed_workouts'],
                    all_workouts
                )
            )
            for i, workout in enumerate(all_workouts):
                print(f'{i})', workout['name'])
            print(f"\n{global_messages['back']}")
            workout_input = input(self.LIST_WORKOUT_MESSAGES['view_workout'])
            if workout_input in ['b', 'back']:
                clear_screen()
                print(global_messages['welcome'])
                break
            if workout_input.isdigit():
                index = int(workout_input)
                if index >= 0 and index < len(all_workouts):
                    selected_workout = all_workouts[index]
                    while True:
                        clear_screen()
                        print(self.format_workout(selected_workout))
                        back = input(f"{global_messages['back']}")
                        if back in ['b', 'back']:
                            clear_screen()
                            break
                else:
                    clear_screen()
                    print(global_messages['invalid_workout'])
                    continue
            else:
                clear_screen()
                print(global_messages['invalid_workout'])
                continue

    def format_workout(self, workout):
        workout_name = f"Workout: {workout['name']}\n"
        output = workout_name
        for day, info in workout['days'].items():
            output += f'\n{day.capitalize()}:\n'
            for exercises in info['exercises']:
                output += (
                    f"  - {exercises['name']}: "
                    f"{exercises['series']} series x "
                    f"{exercises['reps_min']}-{exercises['reps_max']} reps\n"
                )
        return output
