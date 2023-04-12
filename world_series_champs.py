# Luke Psyhogios, April 25th 2022, Section 001, Assignment 7, Problem #2: World Series Champs
import urllib.request

def download_data(url):
    # Will only work if the url allows data to be scraped
    try:
        url = str(url)
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        list_data = list(data.split('\n'))
        return list_data
    except:
        print('Sorry, that is not valid.')



# Get user input
user_url = str(input('Enter a URL: '))
# Assign list of champions to a variable
champions = download_data(user_url)
# Set variables
one_time = []
number = []
one_time_club = ''
# Determine how many teams have at least one championchip
for team in champions:
    if team in one_time:
        continue
    else:
        # Add champion to the list if this is the first time
        one_time.append(team)
for team in one_time:
    # Give each champion an exact number of World Series wins
    count = int(champions.count(team))
    number.append(count)

one_time.remove('')
# Set variables for display
n_one_time = len(one_time)
n_years = len(champions)
maximum = max(number)
maximum_index = number.index(maximum)
average = sum(number)/len(number)
for team in one_time:
    # Get the index to see how many times they've won a world series
    index = one_time.index(team)
    if number[index] == 1:
        one_time_club += team + ', '

# Display output
print('*', n_one_time, 'teams have won the World Series at least once.')
print('* The data contains', n_years, 'years of World Series.')
print('*', one_time[maximum_index], 'has won the most World Series, with a total of', number[maximum_index], 'wins.')
print('*', one_time_club, 'have only won one Worls Series each.')
print('* Among teams who have won at least one World Series, the average number of wins was', average)
