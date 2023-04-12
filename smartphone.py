# Luke Psyhogios, May 2nd 2022, Section 001, Assignment 11, Problem #2: Smartphone
# Set up class
class Smartphone:
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.capacity_used = 0
        self.name = name
        self.apps = {}
        # Announce creation
        print('Smartphone created!')
    def add_app(self, appname, appsize):
        appsize = int(appsize)
        # Capacity used if the app is added
        capacity_after = int(appsize)+int(self.capacity_used)
        # Ensure app is not already installed
        if appname in self.apps.keys():
            print('App already installed')
        elif capacity_after>self.capacity:
            print('Cannot install app, no available space')
        else:
            self.apps.update({appname: appsize})
            self.capacity_used += appsize
    def remove_app(self, appname):
        if appname in self.apps.keys():
            self.capacity_used -= self.apps[appname]
            del self.apps[appname]
        # If app is not installed
        else:
            print('App not installed. Unable to remove.')
    def has_app(self, appname):
        if appname in self.app.keys():
            return True
        else:
            return False
    def get_available_space(self):
        available = self.capacity - self.capacity_used
        return available
    def report(self):
        # Get the names of the apps in a list
        apps_names = list(self.apps.keys())
        # Display report
        print('Name:', self.name)
        print('Capacity:', self.capacity_used, 'out of', self.capacity, 'GB')
        print('Available space:', self.capacity-self.capacity_used)
        print('Apps installed:', len(apps_names))
        # Display apps
        for app in apps_names:
            size = self.apps[app]
            print('* ', app, 'is using', size, 'GB')


# Set up initial variables
valid_1 = False
valid_2 = False
valid_3 = False

# While loop to get capacity and name of phone
while valid_1 == False:
    # Get capacity
    capacity_USE = int(input('Size of your new smartphone (32, 64 or 128 GB): '))
    # Get name
    name_USE = input('Smartphone name: ')
    valid_1 = True

# Create phone
phone = Smartphone(capacity_USE, name_USE)
phone.report()
# While loop for program
while valid_3 == False:
    choice = input('(r)eport, (a)dd app, r(e)move app or (q)uit: ')
    # If user wants to add an app
    if choice == 'a':
        appname_USE = input('App name to add: ')
        appsize_USE = input('App size in GB: ')
        # Add app
        phone.add_app(appname_USE, appsize_USE)
        print('\n')
    if choice == 'r':
        # Print report
        phone.report()
        print('\n')
    if choice == 'e':
        appname = input('App name to remove: ')
        # Remove app
        phone.remove_app(appname)
        print('App removed:', appname)
        print('\n')
    # Quit program
    if choice == 'q':
        print('Goodbye!')
        valid_3 = True