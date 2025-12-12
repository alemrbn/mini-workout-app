from .workout_action import WorkoutAction
from ..utils import (
    global_messages,
    clear_screen,
    check_empty_list,
    format_line_breaks,
    validate_is_digit,
    validate_positive_int
)

class EditWorkout(WorkoutAction):
    EDIT_WORKOUT_MESSAGES = {
        'ask_edit_workout': 'Which workout do you want to edit? ',
        'invalid_edit_workout_option': 'Invalid option.',
        'available_for_edit': 'Available for editing:\n',
        'ask_edit_workout_item': 'Which item do you want to edit? ',
        'ask_new_workout_name': 'What name would you like to use? ',
        'current_description': 'Your current description:\n\n',
        'new_description': 'New description (Enter to keep):\n\n',
        'ask_rename_exercise': '\nWhich exercise do you want to rename? ',
        'new_name': 'New name: '
    }

    def edit_workout(self):
        clear_screen()
        if check_empty_list(self.storage.workouts):
            return   
        selected_workout = self._list_and_select_workout(
            self.EDIT_WORKOUT_MESSAGES['ask_edit_workout']
        )
        if not selected_workout:
            return
        editing = True
        while editing:
            under_development = (
                '-== This menu is still under development.. ==-\n'
            )
            print(under_development)
            available_options = ['rename workout', 'rename exercise', 'edit description']
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
            ).strip().lower() 
            if edit_input_option in ['b', 'back']:
                clear_screen()
                break
            if edit_input_option == '0':
                self.rename_workout(
                    selected_workout,
                    workout_name_msg
                )
            if edit_input_option == '1':
                self.rename_exercise(
                    selected_workout,
                    workout_name_msg
                )
            elif edit_input_option == '2':
                self.description_edit(
                    selected_workout,
                    workout_name_msg
                )
            else:
                clear_screen()
                print(
                    self.EDIT_WORKOUT_MESSAGES['invalid_edit_workout_option']
                )

    def rename_workout(self, workout, title_msg):
        rename_workout_flag = True
        while rename_workout_flag:
            clear_screen()
            print(title_msg)
            new_workout_name = input(
                self.EDIT_WORKOUT_MESSAGES['ask_new_workout_name']
            ).strip().title()
            old_name = workout['name']
            workout['name'] = new_workout_name
            self.storage.rename_workout_file(
                old_name, new_workout_name, workout
            )
            rename_workout_flag = False
            clear_screen()

    def rename_exercise(self, workout, title_msg):
        clear_screen()
        while True:
            print(title_msg)
            exercises = []
            for day_name, info in workout['days'].items():
                for exercise in info['exercises']:
                    exercises.append((day_name, exercise))
            for i, (day_name, exercise) in enumerate(exercises):
                print(f"{i}) {exercise['name']} ({day_name.capitalize()})")
            selected = input(self.EDIT_WORKOUT_MESSAGES['ask_rename_exercise'])
            if selected.isdigit():
                index = int(selected)
                if 0 <= index < len(exercises):
                    day_name, exercise = exercises[index]
                    clear_screen()
                    new_name = input(self.EDIT_WORKOUT_MESSAGES['new_name']).strip().title()
                    exercise['name'] = new_name
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(global_messages['invalid_input'])
            else:
                clear_screen()
                print(global_messages['invalid_input'])

    def description_edit(self, workout, title_msg):
        clear_screen()
        print(title_msg)
        current_desc = workout['description']
        print(f"{self.EDIT_WORKOUT_MESSAGES['current_description']}{current_desc}\n")
        new_desc_input = input(self.EDIT_WORKOUT_MESSAGES['new_description'])
        new_desc = format_line_breaks(new_desc_input)
        if new_desc.strip():
            workout['description'] = new_desc
            clear_screen()
        clear_screen()
