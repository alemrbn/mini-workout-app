from .workout_action import WorkoutAction
from ..utils import (
    global_messages,
    clear_screen,
    check_empty_list
)

class ListWorkout(WorkoutAction):
    LIST_WORKOUT_MESSAGES = {
        'view_workout': 'Which workout would you like to view? '
    }

    def list_workouts(self):
        clear_screen()
        if check_empty_list(self.storage.workouts):
            return
        while True:
            selected_workout = self._list_and_select_workout(
                self.LIST_WORKOUT_MESSAGES['view_workout']
            )
            if not selected_workout:
                return
            while True:
                clear_screen()
                print(self.format_workout(selected_workout))
                back = input(f"{global_messages['back']}")
                if back.strip().lower() in ['b', 'back']:
                    clear_screen()
                    break

    def format_workout(self, workout):
        workout_name = f"Workout: {workout['name']}\n"
        workout_description = workout.get('description', None)
        output = workout_name
        if workout_description:
            output += f"Description: {workout['description']}\n"
        for day, info in workout['days'].items():
            output += f'\n{day.capitalize()}:\n'
            for exercises in info['exercises']:
                output += (
                    f"    - {exercises['name']}: "
                    f"{exercises['series']} series x "
                    f"{exercises['reps_min']}-{exercises['reps_max']} reps\n"
                )
        return output
