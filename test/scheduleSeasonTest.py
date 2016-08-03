from BeautifulSoup import BeautifulSoup
import urllib2
import re
import csv
##url = 'http://schedules.myohsaa.org/SchoolHome/226/Season/Basketball/Boys/Varsity'


class EventScraper(object):
    def __init__(self):
        self.base_url = 'http://schedules.myohsaa.org/SchoolHome/{teamId}/Season/Basketball/Boys/Varsity'
        self.nonopponents =['meeting','parent','scrimmage']
        self.nonopponents=re.compile('|'.join(self.nonopponents),re.IGNORECASE)


    def get_events(self,school_id):
        url = self.base_url.format(teamId=school_id)
        event_list=[]

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        div_content = soup.find("div", {"class": "accordionTeamSchedule collapsableContainer"})

        print 'scarping team', school_id
        try:
            table_content = div_content.findChildren('tr')
        except:
            print 'this school has no Team!', school_id
            return event_list

        for b in table_content:
            sch = list(b.findChildren('td'))
            if not sch:
                continue

            # print len(sch)
            assert len(sch) == 4
            ##assert this information is valid

            thisEventId = sch[2].find('input')['value'].split('=')[-1]
            opponent = sch[2].find('span').renderContents().strip()
            ##IF OPPONENT CONTAINS
            if self.nonopponents.search(opponent):
                continue
            thisHomeTeam = '@' not in opponent

            # print thisHomeTeam

            # print thisEventId
            game = {
                'date': sch[0].renderContents().strip(),
                'time': sch[1].renderContents().strip(),
                'location': sch[3].renderContents().strip(),
                'is_home':thisHomeTeam
            }
            # get event id from sch[2]
            event_list.append(game)
        return event_list

            # print game

'''
    import itertools
    all_teams = itertools.chain(*schedules.values())
    all_teams = set([x['team_id'] for x in all_teams])
    print '# Varsity Teams', len(all_teams)




        for idx, a in enumerate(sch):
            print idx, a.renderContents().strip()


            if idx == 2:


                # PARSE EVENT ID GET FROM 2.
                event_id = None
                # PARSE HOME OR AWAY
                home_team = False
                # ITERATE BY TEAMID
                team_id = 226
                schedules.setdefault(event_id, []).append({'team_id': team_id, 'is_home': home_team})
                #Add event_id, time, date, home_team to games

        print '********'





    for a in div_content:
        #print a
        pass
    '''