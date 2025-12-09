from utils import clear_screen, global_messages
from workout_manager import (
    CreateWorkout,
    EditWorkout,
    DeleteWorkout,
    ListWorkout
)


class Menu:
    MENU = """
1. Create workout
2. Edit workout
3. Delete workout
4. List workouts
5. Exit\n
"""

    def __init__(self, storage):
        self.storage = storage
        self.loop_menu()

    def loop_menu(self):
        clear_screen()
        print(global_messages['welcome'])
        while True:
            user_option = input(Menu.MENU)
            user_option = user_option.lower().strip()
            print()
            if user_option in ['1', 'create', 'create workout']:
                create_workout = CreateWorkout(self.storage)
                create_workout.build_workout()
            elif user_option in ['2', 'edit', 'edit workout']:
                edit_workout = EditWorkout(self.storage)
                edit_workout.edit_workout()
            elif user_option in ['3', 'delete', 'delete workout']:
                delete_workout = DeleteWorkout(self.storage)
                delete_workout.delete_workout()
            elif user_option in ['4', 'list', 'list workout']:
                ListWorkout(self.storage).list_workouts()
            elif user_option in ['5', 'exit']:
                clear_screen()
                exit()
            else:
                clear_screen()
                print(global_messages['welcome'])
                continue
