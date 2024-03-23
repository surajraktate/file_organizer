from os.path import expanduser
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import isfile, join
from os import listdir
import os
import shutil

PATH_SEPARATOR = "/"


class Watcher:
    DIRECTORY_TO_WATCH = expanduser("~") + "/Downloads/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            move_file_by_type(event.src_path)
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)


class FileUtils:
    """this class provides method of file utility"""
    file_name = None

    dir_name = None
    dir_path = None
    full_path = None
    dest_path = None

    def __init__(self, src):
        """intials varibles"""
        self.full_path = src
        self.set_file_name_by_path()
        self.make_dir_by_type()
        self.move(self.full_path, self.dest_path)

    def move(self, src, dest):
        """move file to defined path"""
        print(src)
        print(dest)
        if src and dest:
            return shutil.move(src, dest)
        return False

    def copy(self, scr, dest):
        """copy file to defined path"""
        if scr and dest:
            return shutil.copyfile(scr, dest)
        return False

    def set_file_name_by_path(self):
        """return file name by path"""
        if PATH_SEPARATOR in self.full_path:
            self.file_name = self.full_path.split("/")[-1]
        return False

    def make_dir_by_type(self):
        """make directory by file type"""
        print("Here")
        splited_path = self.full_path.split("/")
        file_type = self.file_name.split(".")[-1]
        if self.file_name in splited_path:
            splited_path.remove(self.file_name)
        self.dir_path = os.path.join("/".join(splited_path), file_type)

        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
        self.dest_path = os.path.join(self.dir_path, self.file_name)


def move_file_by_type(file_src):
    """ this function do whole moving work"""
    if "crdownload" in file_src or os.path.isdir(file_src):
        return
    FileUtils(file_src)


if __name__ == '__main__':
    w = Watcher()
    w.run()
