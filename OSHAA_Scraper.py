import csv

from GetEvents import EventScraper
from GetSchoolIds import SchoolScraper
from GetSchoolAddress import SchoolAddressScraper

def write_all_games_CSV(all_events,all_games,school_id_map):
    with open('all_games.csv', 'w')as handle:
        writer = csv.writer(handle)

        for eventId in all_events:
            teams = all_events[eventId]
            home_team = None
            away_team = None

            #More logic is needed here to add tournament games and opponents outside of state
            #assert len(teams)==2
            if len(teams) != 2:
                print teams, eventId
                continue
            for each_team in teams:
                if each_team['is_home']:
                    home_team = each_team['team_id']
                else:
                    away_team = each_team['team_id']

            #assert home_team and away_team
            if not (home_team and away_team):
                print home_team, away_team, eventId
                continue

            this_home_team = school_id_map[home_team]['name']
            this_away_team = school_id_map[away_team]['name']

            game_to_add = all_games[eventId]
            writer.writerow(
                [game_to_add['date'], game_to_add['time'], this_home_team, this_away_team, game_to_add['`location']])


def write_addresses_CSV(schools):
    with open('school_addresses.csv', 'w')as handle:
        writer = csv.writer(handle)
        for each_school in schools:
            writer.writerow([each_school['id'], each_school['name'],each_school['address']])




def main():
    ##instantiate classes
    schools=SchoolScraper().get_schools()
    school_address_scraper=SchoolAddressScraper()
    event_scraper=EventScraper()
    all_games ={}
    all_events={}
    all_varsity_teams=set()

    for school in schools:
        school['address']=school_address_scraper.get_address(school['id'])
        if not school['address']:
            continue
        events=event_scraper.get_events(school['id'])
        if events:
            all_varsity_teams.add(school['id'])
        for an_event in events:
            all_events.setdefault(an_event['id'], []).append({'team_id': school['id'], 'is_home': an_event['is_home']})
            all_games[an_event['id']]=an_event

    school_id_map={school['id']: school for school in schools}


    ##for eventId in all_events:
        ##print eventId, all_events[eventId], all_games[eventId]
    print 'Number of varsity teams:',len(all_varsity_teams)
    write_all_games_CSV(all_events, all_games, school_id_map)
    write_addresses_CSV(schools)



if __name__== '__main__':
    main()