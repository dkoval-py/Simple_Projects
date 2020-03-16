channels = ['BBC', 'Discovery', 'TV1000']


class TVController():

    def __init__(self, channels):
        self.channels = channels
        self.current_channel = channels[0]
        self.position = 0

    def first_channel(self):
        self.current_channel = self.channels[0]
        self.position = 0
        print(self.current_channel)

    def last_channel(self):
        self.current_channel = self.channels[-1]
        self.position = -1
        print(self.current_channel)

    def turn_channel(self, channel_number):
        self.current_channel = self.channels[channel_number - 1]
        self.position = channel_number - 1
        print(self.current_channel)

    def next_channel(self):
        if self.current_channel == self.channels[-1]:
            self.current_channel = self.channels[0]
            self.position = 0
        else:
            self.position += 1
            self.current_channel = self.channels[self.position]

        print(self.current_channel)

    def previous_channel(self):
        if self.current_channel == self.channels[0]:
            self.current_channel = self.channels[-1]
            self.position = -1
        else:
            self.position -= 1
            self.current_channel = self.channels[self.position]

        print(self.current_channel)

    def current(self):
        if len(self.current_channel) >= 9:
            print(self.current_channel, '|')
        else:
            print(self.current_channel, '\t|')

    def is_exist(self, entered_name):
        if entered_name in self.channels or entered_name == '1' or entered_name == '2' or entered_name == '3':
            print('\n\t---There is such channel---\n\n')
        else:
            print('\n\t---There is no such channel---\n\n')


example = TVController(channels)
is_active = True

while is_active:

    print('\t\t', '-' * 10, sep='')
    print('\t\t|TV is on|')
    print('-' * 49)
    print('|  You\'re currently watching channel: ', end='')
    example.current()
    print('-' * 49)

    print('\t\t  MENU')
    print('''
        1 - Last channel
        2 - First channel
        3 - Next channel
        4 - Previous channel
        5 - Turn the channel
        6 - Check if there is a channel
        7 - Turn off TV
        ''')
    choice = input('>>> ')

    if choice == '1':
        example.last_channel()
    elif choice == '2':
        example.first_channel()
    elif choice == '3':
        example.next_channel()
    elif choice == '4':
        example.previous_channel()
    elif choice == '5':
        check_number = True
        while check_number:
            try:
                number = int(input('Channels\'s number: '))
                if number < 0 or number > 3:
                    print('There are only 3 available channels')
                else:
                    example.turn_channel(number)
                    check_number = False
            except ValueError:
                print('Error >>> Incorrect channel\'s number. Please try again ')
    elif choice == '6':
        check_channel = input('Type channel\'s name or number: ')
        example.is_exist(check_channel)
    elif choice == '7':
        is_active = False

print('\t\t', '-' * 11, sep='')
print('\t\t|TV is off|')
print('\t\t', '-' * 11, sep='')
