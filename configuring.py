# import libraries
import os, sys, platform
from datetime import datetime as dt
import pytz

# user defined modules
class configures:
    """
    read user's configuration
    In Github/GitLab, we may use html file to set the configuration
    However, user may run code on local machine. 
    User can define the configure.dat file and put all settings in the file
    This module would read and backup the settings
    """
    # class attribute for version info
    __version__ = '0.1'     # basic version
    
    def __info__(self):
        """
        Level 0: provide basic version info
        """
        class_name = self.__class__.__name__
        print(f"\t class: {class_name}, version: {self.__version__}")


    def __init__(self, work_path : str = None, configuration : str = "configure.txt"):
        """
        Level 1: initialize universal variables which can derive other variables. specific ones can be initialized in specific methods, such as sc_model_initial(self)
        initialize parameters/variables which includes variables read from contol file and defined variables for codes use
        para:
            interrupt_flag: bool, default False means start from beginning, otherwise start from interruption point
            work_path: configuration file location, please give absolute path
            configuration: configuration file name, default "configuration.txt", user can define different names for other purposes, e.g. FLAG.TXT
        return:
            None
        """
        # environment configuration
        self.splitter = "\\" if "Win" in platform.system() else "/"

        # target path in which the data and configuration files are saved
        self.work_dir = work_path.strip() + self.splitter if work_path != None else os.getcwd().strip() + self.splitter
        self.configuration_file = self.work_dir + configuration
        print(f"L72: {self.configuration_file}")

        # convert default timezone to US/Eastern timezone
        self.est = pytz.timezone('US/Eastern')
        self.time_stamp = dt.now(self.est).strftime("%Y-%m-%d_%H-%M-%S")
                
        # read configuration file
        try:
            # initialized parameters from configuration_file
            print(f"reading {self.configuration_file}")
            i = 0
            with open(self.configuration_file, "r+", encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    i += 1
                    print(f"L58: {i}, {line}")
                    if line.startswith("#"):  # skip comments line
                        print("skipped comment line")
                        pass
                    else:
                        variable_name, variable_value = map(str.strip, line.split('='))
                        if "#" in variable_value:  # remove comments if existing 
                            variable_value = variable_value.split("#")[0].strip()
                        if variable_name == "work_dir" and variable_value == 'None':
                            pass
                        else:
                            if (variable_value.count(".") == 1 and (variable_value.replace('.','').isdigit())):  # test float number
                                setattr(self, variable_name, float(variable_value))
                            elif variable_value.isdigit():  # test int number
                                setattr(self, variable_name, int(variable_value))
                            else:   # other type
                                setattr(self, variable_name, variable_value)
                                
        except FileNotFoundError:
            print("\nFile not existing")

        except Exception as e:
            print(f"Error reading variables from {self.configuration_file}: {e}")


    def display_variables(self, save_flag : bool =False) -> None:
        """
        Level 1: display initialized variables read from configuration and customerized variables. 
        display all initialized variables for user to develop or debug
        para:
            save_flag: bool, default False, not save to a backup file
        return:
            directly display on screen
        """
        print("========================= display initialized variables ==============================")
        for variable_name, variable_value in self.__dict__.items():
            print(f"{variable_name}: {variable_value}")
        # print(f"self: {self.event}")  # test a specific one to see whether the var has been defined well
        if save_flag:
            backup_var_file = self.work_dir + self.splitter + "var_backup.txt"
            # with open(backup_var_file, "wb") as f:
            #     for variable_name, variable_value in self.__dict__.items():

    