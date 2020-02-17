from scrapy.spiders import CSVFeedSpider

class JugadoresFutbolArania(CSVFeedSpider):

    name = "fifa"

    start_urls = [
        'https://query.data.world/s/dn353t4vsz7tnxaofyu6wq644cum5q'
    ]

    delimiter = ','

    headers = [
        'id',
        'name',
        'full_name',
        'birth_date',
        'age',
        'height_cm',
        'weight_kgs',
        'positions',
        'nationality',
        'overall_rating',
        'potential',
        'value_euro',
        'wage_euro',
        'preferred_foot',
        'international_reputation(1-5)',
        'weak_foot(1-5)',
        'skill_moves(1-5)',
        'work_rate',
        'body_type',
        'release_clause_euro',
        'club_team',
        'club_rating',
        'club_position',
        'club_jersey_number',
        'club_join_date',
        'contract_end_year',
        'national_team',
        'national_rating',
        'national_team_position',
        'national_jersey_number',
        'crossing',
        'finishing',
        'heading_accuracy',
        'short_passing',
        'volleys',
        'dribbling',
        'curve',
        'freekick_accuracy',
        'long_passing',
        'ball_control',
        'acceleration',
        'sprint_speed',
        'agility',
        'reactions',
        'balance',
        'shot_power',
        'jumping',
        'stamina',
        'strength',
        'long_shots',
        'aggression',
        'interceptions',
        'positioning',
        'vision',
        'penalties',
        'composure',
        'marking',
        'standing_tackle',
        'sliding_tackle',
        'GK_diving',
        'GK_handling',
        'GK_kicking',
        'GK_positioning',
        'GK_reflexes',
        'tags',
        'traits',
        'LS',
        'ST','RS','LW','LF','CF','RF','RW','LAM',
        'CAM','RAM','LM','LCM','CM','RCM','RM',
        'LWB','LDM','CDM','RDM','RWB','LB','LCB',
        'CB','RCB','RB' 
    ]

    def parse_row(self, response, row):
        print(type(row))
        print('full_name = ', row['full_name'])
        print('age = ', row['age'])
        print('height_cm = ', row['height_cm'])
        print('weight_kgs = ', row['weight_kgs'])
        print('positions = ', row['positions'])
        print('nationality = ', row['nationality'])
        print('potential = ', row['potential'])
        print('value_euro = ', row['value_euro'])
        print('finishing = ', row['finishing'])
        print('short_passing = ', row['short_passing'])
        print('dribbling = ', row['dribbling'])
        print('freekick_accuracy = ', row['freekick_accuracy'])
        print('long_passing = ', row['long_passing'])
        print('ball_control = ', row['ball_control'])
        print('acceleration = ', row['acceleration'])
        print('sprint_speed = ', row['sprint_speed'])
        print('agility = ', row['agility'])
        with open('fifa.csv', 'a+', encoding='utf-8') as archivo:
            archivo.write(row['full_name']+';'
            + row['age'] + ';' 
            + row['height_cm'] + ';' 
            + row['weight_kgs'] + ';' 
            + row['positions'] + ';'
            + row['nationality'] + ';'
            + row['potential'] + ';'
            + row['value_euro'] + ';'
            + row['finishing'] + ';'
            + row['short_passing'] + ';'
            + row['dribbling'] + ';'
            + row['freekick_accuracy'] + ';'
            + row['long_passing'] + ';'
            + row['ball_control'] + ';'
            + row['acceleration'] + ';'
            + row['sprint_speed'] + ';'
            + row['agility'] + '\n')