import urllib.request
with open('input.txt','r') as inp:
    with open('output.txt','w') as outp:
        url = inp.readlines()
        for k in range(0, len(url)):
            f = urllib.request.urlopen(url[k])
            text = str(f.read())
            name_loc = text.find('nfl-c-player-header__title')
            name = text[text.find('>', name_loc)+1:text.find('</h1', name_loc)]
            att_loc = text.find('passingAttempts')
            att = int(text[text.find(' ',att_loc)+24:text.find('/th', att_loc)-23])
            comp_loc = text.find('passingCompletions')
            comp = int(text[text.find(' ',comp_loc)+24:text.find('/th', comp_loc)-23])
            yds_loc = text.find('passingYards')
            yds = int(text[text.find(' ',yds_loc)+24:text.find('/th', yds_loc)-23])
            td_loc = text.find('passingTouchdowns')
            td = int(text[text.find(' ',td_loc)+24:text.find('/th', td_loc)-23])
            int_loc = text.find('passingInterceptions')
            inte = int(text[text.find(' ',int_loc)+24:text.find('/th', int_loc)-23])
            rating_loc = text.find('passingPasserRating')
            rating = text[text.find(' ',rating_loc)+37:text.find('/th', rating_loc)-24]+'0'
            outp.write('{:<20s}{:<7d}{:<7d}{:<7d}{:<7d}{:<7d}{:<7s}'.format(name, comp, att, yds, td, inte, rating)+'\n')
