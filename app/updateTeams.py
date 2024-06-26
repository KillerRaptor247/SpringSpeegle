#mapping: 
# 2023 data mapping: current = new
# teams_ID = autogenerated
# teamID = teamID
# yearId = yearID
# lgID = lgID
# divID = divID
# franchID = franchID
# team_name = name
# team_rank = Rank
# team_G = G
# team_G_home = GHome
# team_W = W
# team_L = L
# DivWin = DivWin
# WCWin = WCWin
# LgWin = LgWin
# WSWin = WSWin
# team_R = R
# team_AB = AB
# team_H = H
# team_2B = 2B
# team_3B = 3B
# team_HR = HR
# team_BB = BB
# team_SO = SO
# team_SB = SB
# team_CS = CS
# team_HBP = HBP
# team_SF = SF
# team_RA = RA
# team_ER = ER
# team_ERA = ERA
# team_CG = CG
# team_SHO = SHO
# team_SV = SV
# team_IPouts = IPouts
# team_HA = HA
# team_HRA = HRA
# team_BBA = BBA
# team_SOA = SOA
# team_E = E
# team_DP = DP
# team_FP = FP
# park_name = park
# team_attendance = attendance
# team_BPF = BPF
# team_PPF = PPF
# team_projW = 
# team_projL =

import pymysql
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text, ForeignKey, func, Float, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload
from . import csi3335sp2023 as dbC
import sys
import csv
import pandas as pd


Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'

    teams_ID = Column(Integer, primary_key=True, autoincrement=True)
    teamID = Column(String(3), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    lgID = Column(String(2))
    divID = Column(String(1))
    franchID = Column(String(3))
    team_name = Column(String(50))
    team_rank = Column(SmallInteger)
    team_G = Column(SmallInteger)
    team_G_home = Column(SmallInteger)
    team_W = Column(SmallInteger)
    team_L = Column(SmallInteger)
    DivWin = Column(String(1))
    WCWin = Column(String(1))
    LgWin = Column(String(1))
    WSWin = Column(String(1))
    team_R = Column(SmallInteger)
    team_AB = Column(SmallInteger)
    team_H = Column(SmallInteger)
    team_2B = Column(SmallInteger)
    team_3B = Column(SmallInteger)
    team_HR = Column(SmallInteger)
    team_BB = Column(SmallInteger)
    team_SO = Column(SmallInteger)
    team_SB = Column(SmallInteger)
    team_CS = Column(SmallInteger)
    team_HBP = Column(SmallInteger)
    team_SF = Column(SmallInteger)
    team_RA = Column(SmallInteger)
    team_ER = Column(SmallInteger)
    team_ERA = Column(Float)
    team_CG = Column(SmallInteger)
    team_SHO = Column(SmallInteger)
    team_SV = Column(SmallInteger)
    team_IPouts = Column(Integer)
    team_HA = Column(SmallInteger)
    team_HRA = Column(SmallInteger)
    team_BBA = Column(SmallInteger)
    team_SOA = Column(SmallInteger)
    team_E = Column(SmallInteger)
    team_DP = Column(SmallInteger)
    team_FP = Column(Float)
    park_name = Column(String(50))
    team_attendance = Column(Integer)
    team_BPF = Column(SmallInteger)
    team_PPF = Column(SmallInteger)
    team_projW = Column(SmallInteger)
    team_projL = Column(SmallInteger)

def updateTeams():
    enginestr = "mysql+pymysql://" + dbC.mysql['user'] + ":" + dbC.mysql['password'] + "@" + dbC.mysql['location'] + ":3306/" + dbC.mysql['database']

    engine = create_engine(enginestr)

    Session = sessionmaker(bind=engine)
    session = Session()
    prequery = session.query(Teams).filter(Teams.yearID == 2023)
    if prequery.count() == 0:

        # Open the CSV file
        with open('lahman_1871-2023_csv/lahman_1871-2023_csv/Teams.csv', 'r') as file:
            reader = csv.DictReader(file)

            # reader = pd.read_csv(file, iterator=True, na_values=[''])

            next(reader, None)

            # Iterate over each row in the CSV file
            for row in reader:
                # Extract the data from the row based on the mappings

                if (row['yearID'] != '2023'):
                    continue

                teamID = row['teamID']
                yearID = row['yearID']
                lgID = row['lgID']
                divID = row['divID']
                franchID = row['franchID']
                team_name = row['name']
                team_rank = row['Rank']
                team_G = row['G']
                team_G_home = row['Ghome']
                team_W = row['W']
                team_L = row['L']
                DivWin = row['DivWin']
                WCWin = row['WCWin']
                LgWin = row['LgWin']
                WSWin = row['WSWin']
                team_R = row['R']
                team_AB = row['AB']
                team_H = row['H']
                team_2B = row['2B']
                team_3B = row['3B']
                team_HR = row['HR']
                team_BB = row['BB']
                team_SO = row['SO']
                team_SB = row['SB']
                team_CS = row['CS']
                team_HBP = row['HBP']
                team_SF = row['SF']
                team_RA = row['RA']
                team_ER = row['ER']
                team_ERA = row['ERA']
                team_CG = row['CG']
                team_SHO = row['SHO']
                team_SV = row['SV']
                team_IPouts = row['IPouts']
                team_HA = row['HA']
                team_HRA = row['HRA']
                team_BBA = row['BBA']
                team_SOA = row['SOA']
                team_E = row['E']
                team_DP = row['DP']
                team_FP = row['FP']
                park_name = row['park']
                team_attendance = row['attendance']
                team_BPF = row['BPF']
                team_PPF = row['PPF']

                win_percentage= pow(int(team_R), 1.83)/(pow(int(team_R), 1.83) + pow(int(team_RA), 1.83))

                team_projW = int(team_G) * win_percentage
                team_projL = int(team_G) - team_projW

                newTeam = Teams(teamID=teamID, yearID=yearID, lgID=lgID, divID=divID, franchID=franchID, team_name=team_name, team_rank=team_rank, team_G=team_G, team_G_home=team_G_home, team_W=team_W, team_L=team_L, DivWin=DivWin, WCWin=WCWin, LgWin=LgWin, WSWin=WSWin, team_R=team_R, team_AB=team_AB, team_H=team_H, team_2B=team_2B, team_3B=team_3B, team_HR=team_HR, team_BB=team_BB, team_SO=team_SO, team_SB=team_SB, team_CS=team_CS, team_HBP=team_HBP, team_SF=team_SF, team_RA=team_RA, team_ER=team_ER, team_ERA=team_ERA, team_CG=team_CG, team_SHO=team_SHO, team_SV=team_SV, team_IPouts=team_IPouts, team_HA=team_HA, team_HRA=team_HRA, team_BBA=team_BBA, team_SOA=team_SOA, team_E=team_E, team_DP=team_DP, team_FP=team_FP, park_name=park_name, team_attendance=team_attendance, team_BPF=team_BPF, team_PPF=team_PPF, team_projW=team_projW, team_projL=team_projL)

                session.add(newTeam)

        session.commit()
        query = session.query(Teams).filter(Teams.yearID == 2023)

        print(query.count())

        session.close()
        print("Teams updated")

