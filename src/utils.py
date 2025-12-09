import os

global_messages = {
  'welcome': '-== Welcome! ==-',
  'back': 'Type [b]ack to return ',
  'invalid_workout': 'Invalid workout selection.',
  'empty_workout': 'No workout was found.',
  'listed_workouts': 'Workouts found'
}


def clear_screen():
    system = os.name
    if system == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def check_empty_list(workouts):
    if len(workouts) == 0:
        print(global_messages['empty_workout'])
        return True
    return False


def list_workouts(msg, workouts):
    message = (
        f"{msg} "
        f"({len(workouts)}):\n"
    )
    return message


def is_nonempty_string(value):
    return isinstance(value, str) and value.string() != ""


def is_positive_int(value):
    return value.isdigit() and int(value) > 0
