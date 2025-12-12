from ..utils import (
    global_messages,
    clear_screen,
    is_nonempty_string,
    validate_positive_int,
    get_validated_input
)

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
        'invalid_exercise_series': 'You must enter at least one set.',
        'ask_exercise_reps_min': 'Minimum reps: ',
        'ask_exercise_reps_max': 'Maximum reps: ',
        'invalid_exercise_reps': 'Invalid input. Please enter valid numbers.',
        'available_days': 'Available days:\n',
        'choose_day': '\nChoose a day or type [d]one to finish: ',
        'no_days_selected': 'You must select at least one day.',
        'invalid_day': 'Please choose a valid day.',
        'ask_description': (
           'Would you like to add a description?\n'
           '(Use :break: to break line)\n'
           '[y]es / [no] '
        ),
        'description': 'Enter your description:\n\n',
        'complete_workout': 'Workout created successfully!'
    }

    def __init__(self, storage):
        self.storage = storage
        self.workout_data = {}

    def _validate_name(self, name, error_msg):
        if not is_nonempty_string(name) or name.isdigit():
            raise ValueError(error_msg)
        return name.strip().title()

    def _validate_workout_name(self, name):
        return self._validate_name(
            name, self.CREATE_WORKOUT_MESSAGES['invalid_workout_name']
        )

    def _validate_exercise_name(self, name):
        return self._validate_name(
            name, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_name']
        )

    def _validate_series(self, value):
        return validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_series']
        )

    def _validate_reps_min(self, value):
        return validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )

    def _validate_reps_max(self, value, reps_min):
        num = validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        if num < reps_min:
            raise ValueError(
                self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
            )
        return num

    def _ask_workout_name(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_workout_name'],
            self._validate_workout_name,
            self.CREATE_WORKOUT_MESSAGES['invalid_workout_name']
        )

    def _ask_exercise_name(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_name'],
            self._validate_exercise_name,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_name']
        )

    def _ask_exercise_series(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_series'],
            self._validate_series,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_series']
        )

    def _ask_exercise_reps(self):
        clear_screen()
        reps_min = get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_min'],
            self._validate_reps_min,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        reps_max = get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_max'],
            lambda value: self._validate_reps_max(value, reps_min),
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        return reps_min, reps_max

    def _ask_day(self, available_days):
        while True:
            print(self.CREATE_WORKOUT_MESSAGES['available_days'])
            for i, day in enumerate(available_days):
                print(f"{i}) {day.capitalize()}")
            day_input = input(
                self.CREATE_WORKOUT_MESSAGES['choose_day']
            ).strip().lower()
            if day_input in ['d', 'done']:
                return 'done'
            if day_input.isdigit():
                index = int(day_input)
                if 0 <= index < len(available_days):
                    return available_days[index]
            elif day_input in available_days:
                return day_input
            clear_screen()
            print(self.CREATE_WORKOUT_MESSAGES['invalid_day'])

    def _ask_exercises_for_day(self, day):
        while True:
            exercise_name = self._ask_exercise_name()
            series = self._ask_exercise_series()
            reps_min, reps_max = self._ask_exercise_reps()
            self.workout_data['days'][day]['exercises'].append({
                'name': exercise_name,
                'series': series,
                'reps_min': reps_min,
                'reps_max': reps_max
            })
            clear_screen()
            while True:
                add_another = input(
                    self.CREATE_WORKOUT_MESSAGES['ask_another_exercise']
                ).strip().lower()
                if add_another in ['n', 'no']:
                    clear_screen()
                    return
                elif add_another in ['y', 'yes']:
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(global_messages['invalid_input'])

    def _ask_description(self):
        clear_screen()
        while True:
            ask_description = input(self.CREATE_WORKOUT_MESSAGES['ask_description'])
            if ask_description in ['n', 'no']:
                clear_screen()
                break
            elif ask_description in ['y', 'yes']:
                while True:
                    clear_screen()
                    line_break = ':break:'
                    description = input(self.CREATE_WORKOUT_MESSAGES['description'])
                    description = description.replace(line_break, '\n')
                    self.workout_data['description'] = description
                    break
                break
            else:
                clear_screen()
                print(global_messages['invalid_input'])


    def build_workout(self):
        workout_name = self._ask_workout_name()
        clear_screen()
        self.workout_data['name'] = workout_name
        self.workout_data['days'] = {}
        available_days = self.DAYS.copy()
        while available_days:
            chosen_day = self._ask_day(available_days)
            if chosen_day == 'done':
                if not self.workout_data['days']:
                    clear_screen()
                    print(self.CREATE_WORKOUT_MESSAGES['no_days_selected'])
                    continue
                break  
            self.workout_data['days'][chosen_day] = {'exercises': []}
            self._ask_exercises_for_day(chosen_day)
            available_days.remove(chosen_day)
        self._ask_description()
        clear_screen()
        self.storage.save_workout(self.workout_data)
        print(self.CREATE_WORKOUT_MESSAGES['complete_workout'])
