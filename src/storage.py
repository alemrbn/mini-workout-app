import os
import json


class Storage:
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.project_root = os.path.join(self.current_dir, "..")
        self.workouts_folder = os.path.abspath(
            os.path.join(self.project_root, "workouts_data")
            )
        if not os.path.exists(self.workouts_folder):
            os.makedirs(self.workouts_folder)

        self.workouts = []

    def save_workout(self, workout):
        archive_name = f'{workout["name"]}.json'
        full_path = os.path.join(self.workouts_folder, archive_name)
        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(workout, file, indent=4)
        if workout not in self.workouts:
            self.workouts.append(workout)

    def load_workouts(self):
        self.archives = os.listdir(self.workouts_folder)
        self.json_archives = []
        for archive in self.archives:
            if archive.endswith(".json"):
                self.json_archives.append(archive)
        for archive in self.json_archives:
            path = os.path.join(self.workouts_folder, archive)
            with open(path, "r", encoding="utf-8") as file:
                workout = json.load(file)
                if workout not in self.workouts:
                    self.workouts.append(workout)

    def delete_workout(self, name):
        path = os.path.join(self.workouts_folder, f"{name}.json")
        if os.path.exists(path):
            os.remove(path)
        self.workouts = [w for w in self.workouts if w["name"] != name]

    def rename_workout_file(self, old_name, new_name, workout_data):
        old_path = os.path.join(self.workouts_folder, f"{old_name}.json")
        new_path = os.path.join(self.workouts_folder, f"{new_name}.json")
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        with open(new_path, "w", encoding="utf-8") as file:
            json.dump(workout_data, file, indent=4)
