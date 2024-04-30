import pymysql
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text, ForeignKey, func, Float, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload
import sys
import csv
import pandas as pd

from . import csi3335sp2023 as dbC

Base = declarative_base()


class HallOfFame(Base):
    __tablename__ = 'hallOfFame'

    halloffame_ID = Column(Integer, primary_key=True,autoincrement=True)
    playerID = Column(String(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    votedBy = Column(String(64), nullable=False)
    ballots = Column(SmallInteger, nullable=True)
    needed = Column(SmallInteger, nullable=True)
    votes = Column(SmallInteger, nullable=True)
    inducted = Column(String(1), nullable=True)
    category = Column(String(20), nullable=True)
    note = Column(String(25), nullable=True)

def updateHOF():

    enginestr = "mysql+pymysql://" + dbC.mysql['user'] + ":" + dbC.mysql['password'] + "@" + dbC.mysql[
        'location'] + ":3306/" + dbC.mysql['database']

    engine = create_engine(enginestr)

    Session = sessionmaker(bind=engine)
    session = Session()

    prequery = session.query(HallOfFame).filter(HallOfFame.yearID == 2023)
    if prequery.count() == 0:
        # Open the CSV file
        with open('lahman_1871-2023_csv/lahman_1871-2023_csv/HallOfFame.csv', 'r') as file:
            reader = csv.DictReader(file)

            # reader = pd.read_csv(file, iterator=True, na_values=[''])

            next(reader, None)

            # Iterate over each row in the CSV file
            for row in reader:
                # Extract the data from the row based on the mappings

                if (row['yearid'] != '2023'):
                    continue

                playerID = row['playerID']
                yearID = row['yearid']
                votedBy = row['votedBy']
                ballots = row['ballots']
                needed = row['needed']
                votes = row['votes']
                inducted = row['inducted']
                category = row['category']
                note = row['needed_note']



                newHallOfFame = HallOfFame(playerID = playerID,yearID = yearID, votedBy = votedBy, ballots = ballots, needed = needed,
                                           votes = votes,inducted = inducted, category = category, note = note
                                        )

                session.add(newHallOfFame)

        session.commit()
        query = session.query(HallOfFame).filter(HallOfFame.yearID == 2023)

        print(query.count())

        session.close()
        print("Hall Of Fame updated")