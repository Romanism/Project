# import package
from selenium import webdriver
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# crawling premierleague game information
def premier(df, startpage, endpage) :

    '''
    이 함수는 프리미어리그 경기 정보를 크롤링하는 함수입니다
    방식은 Selenium을 사용했습니다
    각 팀별로 Possesion(점유율), Shots on target(유효슈팅), Shots(슈팅), Touches(터치), Passes(패스),
    Tackles(태클), Clearances(방어), Corners(코너킥), Offsides(오프사이드), Goal(골)을 수집했습니다
    '''

    for i in range(startpage, endpage+1):

        driver = webdriver.Chrome()
        driver.get("https://www.premierleague.com/match/"+ str(i))
        time.sleep(30)
        driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.wrapper.col-12 > div > div > ul > li:nth-child(3)").click()
        time.sleep(5)

        # Home Team
        data = {
        "Team" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > thead > tr > th:nth-child(1) > a").text,
        "Possession" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(1) > td:nth-child(1) > p").text,
        "Shots on target" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(2) > td:nth-child(1) > p").text,
        "Shots" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(3) > td:nth-child(1) > p").text,
        "Touches" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(4) > td:nth-child(1) > p").text,
        "Passes" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(5) > td:nth-child(1) > p").text,
        "Tackles" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(6) > td:nth-child(1) > p").text,
        "Clearances" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(7) > td:nth-child(1) > p").text,
        "Corners" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(8) > td:nth-child(1) > p").text,
        "Offsides" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(9) > td:nth-child(1) > p").text,
        'Goal' : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > section > div.scoreboxContainer > div > div > div.teamsContainer > div.matchScoreContainer > div > div").text[0]
        }

        df.loc[len(df)] = data

       # Away Team
        data = {
        "Team" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > thead > tr > th:nth-child(3) > a").text,
        "Possession" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(1) > td:nth-child(3) > p").text,
        "Shots on target" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(2) > td:nth-child(3) > p").text,
        "Shots" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(3) > td:nth-child(3) > p").text,
        "Touches" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(4) > td:nth-child(3) > p").text,
        "Passes" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(5) > td:nth-child(3) > p").text,
        "Tackles" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(6) > td:nth-child(3) > p").text,
        "Clearances" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(7) > td:nth-child(3) > p").text,
        "Corners" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(8) > td:nth-child(3) > p").text,
        "Offsides" : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > div.mcTabsContainer > div.mcTabs > section.mcMainTab.head-to-head.active > div.mcTabs > div.mcStatsTab.statsSection.season-so-far.wrapper.col-12.active > table > tbody > tr:nth-child(9) > td:nth-child(3) > p").text,
        'Goal' : driver.find_element_by_css_selector("#mainContent > div > section > div.centralContent > section > div.scoreboxContainer > div > div > div.teamsContainer > div.matchScoreContainer > div > div").text[2],
        }

        df.loc[len(df)] = data

        time.sleep(5)
        driver.close()


# input year
def year(df, year) :

    '''
    이 함수는 경기가 발생한 년도를 입력하는 함수입니다
    '''

    # make dataframe
    df['Year'] = ''

    df['Year'] = year


# input home
def home(df) :

    '''
    이 함수는 홈, 어웨이를 입력하는 함수입니다
    홈에서 경기를 했으면 1, 어웨이에서 경기를 했으면 0에서 표시했습니다
    '''

    # make dataframe
    df['Home'] = ''

    # for문 (20teams * 38round)
    for i in range(0, 760, 2):

        df['Home'][i] = 1
        df['Home'][i+1] = 0


# input result
def result(df) :

    '''
    이 함수는 경기의 승패를 입력하는 함수입니다
    경기에서 졌으면 0, 이겼으면 1, 비겼으면 2로 표시했습니다
    '''

    # make dataframe
    df['Result'] = ''

    # for문 (20teams * 38round)
    for i in range(0, 760, 2):

        if df['Goal'][i] > df['Goal'][i+1] :
            df['Result'][i] = 1
            df['Result'][i+1] = 0

        elif df['Goal'][i] < df['Goal'][i+1] :
            df['Result'][i] = 0
            df['Result'][i+1] = 1

        else :
            df['Result'][i] = 2
            df['Result'][i+1] = 2
