from Tkinter import *

import ttk
import tkFileDialog
import os
import csv
import re
import shutil

class MainWindow:

    def __init__(self, master):

        self.csv_directory = None       # the absolute path of the directory chosen
        self.all_csv_files = []         # all file names under the csv_directory
        self.selected_csv_files = []    # integers representing the index of files chosen (from self.all_csv_files)
        self.all_vidaud_files = []       # all video or audio files within the attached directory

        self.export_file = None

        self.root = master
        self.root.title("Batch Export")
        self.root.geometry("900x500")
        self.main_frame = Frame(root)
        self.main_frame.pack()

        # All the file listbox variables and GUI elements
        self.file_listbox_label = Label(self.main_frame, text="Files")
        self.file_listbox_label.grid(row=0, column=1)



        self.file_listbox = Listbox(self.main_frame,
                                    width=53,
                                    height=20,
                                    selectmode=MULTIPLE)

        self.file_listbox.grid(row=1, column=1, padx=10)




        self.file_list_loadvids_button = Button(self.main_frame,
                                            text="Load Videos",
                                            command=self.directory_loadvids)
        
        self.file_list_loadauds_button = Button(self.main_frame,
                                            text="Load Audios",
                                            command=self.directory_loadauds)

        self.file_list_loadvids_button.grid(row=2, column=1)
        self.file_list_loadauds_button.grid(row=3, column=1)





        self.file_select_button = Button(self.main_frame,
                                         text="Select",
                                         command=self.select_files)

        self.file_select_button.grid(row=2, column=2)

        self.file_selectall_button = Button(self.main_frame,
                                         text="Select All",
                                         command=self.select_all)

        self.file_selectall_button.grid(row=4, column=2)

        self.file_list_clear_button = Button(self.main_frame,
                                             text="Clear All",
                                             command=self.directory_clear)

        self.file_list_clear_button.grid(row=5, column=2)


        self.file_selected_clear_button = Button(self.main_frame,
                                                 text="Clear Selected",
                                                 command=self.clear_selected)

        self.file_selected_clear_button.grid(row=3, column=2)


        self.files_selected_label = Label(self.main_frame, text="files selected", fg="green")


        # All the file extension variables and GUI elements
        self.file_extension = None
        self.filename_contains = None


        # Final export button
        self.export_csv = Button(self.main_frame, text="Export", command=self.export_csv)
        self.export_csv.grid(row=5, column=1)


        #self.file_tree = ttk.Treeview(self.main_frame)
        #self.file_tree.grid(row=1, column=3, padx=10)

    def directory_loadvids(self):

        self.directory_clear()

        # get the extension and filename substring for searching/filtering
        self.file_extension = "mp4"
        self.filename_contains = "video"

        print "extension: " + str(self.file_extension) + "######"

        self.csv_directory = tkFileDialog.askdirectory()

        all_files = []

        for dir, subdirs, files in os.walk(self.csv_directory):
            print "dir: " + str(dir) + "\nsubdirs: " + str(subdirs) + "\nfiles: " + str(files) + "\n\n"
            for file in files:

                all_files.append(os.path.join(dir, file))
                # if file.endswith(self.file_extension):
                #     if not self.filename_contains_box.get(): # check if filename_contains is empty
                #         self.all_csv_files.append(file)
                #     elif file.find(self.filename_contains) is not -1:
                #         self.all_csv_files.append(file)
                #print os.path.join(subdir, file)
                #print self.all_csv_files
            
        self.csv_directory = os.path.commonprefix(all_files)
        prefix_len = len(self.csv_directory)
        for i, file in enumerate(all_files):
            print "filename: " + file[prefix_len:]
            if file.endswith(self.file_extension) and re.match("(\\d+)(_)(\\d+)(_video)(\\.)(mp4)",os.path.basename(file)):
                self.all_vidaud_files.append(os.path.abspath(file))
                self.all_vidaud_files.sort()
                self.all_csv_files.append(file[prefix_len:])
                self.all_csv_files.sort()
            # if file.endswith(self.file_extension):
            #     if not self.filename_contains_box.get():    # if extension is not provided, continue
            #         continue
            # else:
            #     del all_files[i]





        for i, file in enumerate(self.all_csv_files):
            filename = os.path.split(file)[1]
            self.file_listbox.insert(i, filename)
            
    def directory_loadauds(self):

        self.directory_clear()

        # get the extension and filename substring for searching/filtering
        self.file_extension = "wav"
        self.filename_contains = "_"

        print "extension: " + str(self.file_extension) + "######"

        self.csv_directory = tkFileDialog.askdirectory()

        all_files = []

        for dir, subdirs, files in os.walk(self.csv_directory):
            for file in files:

                all_files.append(os.path.join(dir, file))
                # if file.endswith(self.file_extension):
                #     if not self.filename_contains_box.get(): # check if filename_contains is empty
                #         self.all_csv_files.append(file)
                #     elif file.find(self.filename_contains) is not -1:
                #         self.all_csv_files.append(file)
                #print os.path.join(subdir, file)
                #print self.all_csv_files

        self.csv_directory = os.path.commonprefix(all_files)
        prefix_len = len(self.csv_directory)
        for i, file in enumerate(all_files):
            if file.endswith(self.file_extension) and re.match("(\\d+)(_)(\\d+)(\\.)(wav)",os.path.basename(file)):
                self.all_vidaud_files.append(os.path.abspath(file))
                self.all_vidaud_files.sort()
                self.all_csv_files.append(file[prefix_len:])
                self.all_csv_files.sort()
            # if file.endswith(self.file_extension):
            #     if not self.filename_contains_box.get():    # if extension is not provided, continue
            #         continue
            # else:
            #     del all_files[i]

        for i, file in enumerate(self.all_csv_files):
            filename = os.path.split(file)[1]
            self.file_listbox.insert(i, filename)

    def directory_clear(self):

        del self.all_csv_files[:]
        del self.selected_csv_files[:]

        self.file_extension = None

        self.file_listbox.delete(0, END)

        self.files_selected_label.grid_remove()

    def select_files(self):

        print self.file_listbox.curselection()
        for selection in self.file_listbox.curselection():
            if self.all_csv_files[int(selection)] not in self.selected_csv_files:
                self.selected_csv_files.append(self.all_csv_files[int(selection)])

        if len(self.selected_csv_files) > 0:
            self.files_selected_label.grid(row=6, column=1)
        print self.selected_csv_files

    def select_all(self):
        self.file_listbox.select_set(0, END)
        
    def clear_selected(self):

        self.file_listbox.select_clear(0, END)
        self.files_selected_label.grid_remove()
        del self.selected_csv_files[:]

    def export_csv(self):
        #
        # if (not self.word_list) or\
        #         (not self.word_list_file) or\
        #         (not self.all_csv_files) or\
        #         (not self.csv_directory):
        #     raise Exception("you need to load all the files first")

        self.export_file = tkFileDialog.askdirectory()
        print self.selected_csv_files
        selectionarr = self.file_listbox.curselection()
        count = 0
        for file in self.selected_csv_files:
            print "File being copied: " + os.path.abspath(file)
            shutil.copy(self.all_vidaud_files[int(selectionarr[count])], self.export_file)
            print "File successfully copied: " + os.path.abspath(file)
            count= count+1


if __name__ == "__main__":
    root = Tk()
    MainWindow(root)
    root.mainloop()
