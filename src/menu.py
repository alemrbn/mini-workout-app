from utils import clear_screen, global_messages
from workout_manager import (
    CreateWorkout,
    EditWorkout,
    DeleteWorkout,
    ListWorkout,
    all_workouts
)


class Menu:
    MENU = """
1. Create workout
2. Edit workout
3. Delete workout
4. List workouts
5. Exit\n
"""

    def __init__(self):
        self.loop_menu()

    def loop_menu(self):
        clear_screen()
        print(global_messages['welcome'])
        while True:
            user_option = input(Menu.MENU)
            user_option = user_option.lower().strip()
            print()
            if user_option in ['1', 'create', 'create workout']:
                create_workout = CreateWorkout()
                create_workout.build_workout()
                all_workouts.append(create_workout.workout_data)
            elif user_option in ['2', 'edit', 'edit workout']:
                EditWorkout().edit_workout()
            elif user_option in ['3', 'delete', 'delete workout']:
                DeleteWorkout().delete_workout()
            elif user_option in ['4', 'list', 'list workout']:
                ListWorkout().list_workouts()
            elif user_option in ['5', 'exit']:
                clear_screen()
                exit()
            else:
                clear_screen()
                print(global_messages['welcome'])
                continue
