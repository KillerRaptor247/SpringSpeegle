"""revised users admin

Revision ID: 77a3a344bea1
Revises: 2e5cddd521a0
Create Date: 2024-04-22 11:56:40.678237

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77a3a344bea1'
down_revision = '2e5cddd521a0'
branch_labels = None
depends_on = None


def upgrade():

    return

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('team_2B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_H', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('park_name', mysql.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('team_FP', mysql.DOUBLE(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('team_3B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_ER', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('WCWin', mysql.VARCHAR(length=1), nullable=True))
        batch_op.add_column(sa.Column('team_G_home', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('DivWin', mysql.VARCHAR(length=1), nullable=True))
        batch_op.add_column(sa.Column('divID', mysql.CHAR(length=1), nullable=True))
        batch_op.add_column(sa.Column('team_rank', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_E', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_PPF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_SB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_SF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_HR', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_CS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_projW', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_attendance', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_HRA', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_SV', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_SO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_projL', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_SOA', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_BBA', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_HA', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_IPouts', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_ERA', mysql.DOUBLE(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('team_RA', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('lgID', mysql.CHAR(length=2), nullable=True))
        batch_op.add_column(sa.Column('team_L', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_W', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('franchID', mysql.VARCHAR(length=3), nullable=True))
        batch_op.add_column(sa.Column('team_HBP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_CG', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_R', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_AB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('LgWin', mysql.VARCHAR(length=1), nullable=True))
        batch_op.add_column(sa.Column('WSWin', mysql.VARCHAR(length=1), nullable=True))
        batch_op.add_column(sa.Column('team_DP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_BB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('teams_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('team_SHO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('team_BPF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('teams_ibfk_2', 'leagues', ['lgID'], ['lgID'])
        batch_op.create_foreign_key('teams_ibfk_1', 'franchises', ['franchID'], ['franchID'])
        batch_op.drop_index(batch_op.f('ix_teams_teamID'))
        batch_op.create_index('teams_teamID_yearID', ['teamID', 'yearID'], unique=False)
        batch_op.alter_column('team_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('teamID',
               existing_type=sa.String(length=3),
               type_=mysql.CHAR(length=3),
               existing_nullable=False)
        batch_op.drop_column('teams_id')

    op.create_table('people',
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('birthYear', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('birthMonth', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('birthDay', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('birthCountry', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('birthState', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('birthCity', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('deathYear', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('deathMonth', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('deathDay', mysql.INTEGER(display_width=12), autoincrement=False, nullable=True),
    sa.Column('deathCountry', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('deathState', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('deathCity', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('nameFirst', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('nameLast', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('nameGiven', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('weight', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True),
    sa.Column('height', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True),
    sa.Column('bats', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('throws', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('debutDate', sa.DATE(), nullable=True),
    sa.Column('finalGameDate', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('playerID')
    )
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.create_index('people_nameLast_nameFirst', ['nameLast', 'nameFirst'], unique=False)

    op.create_table('fielding',
    sa.Column('fielding_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('stint', mysql.SMALLINT(display_width=4), autoincrement=False, nullable=False),
    sa.Column('position', mysql.VARCHAR(length=2), nullable=True),
    sa.Column('f_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_GS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_InnOuts', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_PO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_A', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_E', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_DP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_PB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_WP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_SB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_CS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_ZR', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fielding_ibfk_1'),
    sa.PrimaryKeyConstraint('fielding_ID')
    )
    with op.batch_alter_table('fielding', schema=None) as batch_op:
        batch_op.create_index('k_fie_team', ['teamID'], unique=False)
        batch_op.create_index('fielding_playerID_yearID_teamID', ['playerID', 'yearID', 'teamID'], unique=False)

    op.create_table('appearances',
    sa.Column('appearances_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamId', mysql.CHAR(length=3), nullable=False),
    sa.Column('G_all', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('GS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_batting', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_defense', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_p', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_c', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_1b', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_2b', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_3b', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_ss', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_lf', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_cf', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_rf', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_of', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_dh', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_ph', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('G_pr', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='appearances_ibfk_1'),
    sa.PrimaryKeyConstraint('appearances_ID')
    )
    with op.batch_alter_table('appearances', schema=None) as batch_op:
        batch_op.create_index('k_app_team', ['teamId'], unique=False)
        batch_op.create_index('appearances_playerID_yearID', ['playerID', 'yearID'], unique=False)

    op.create_table('homegames',
    sa.Column('homegames_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('parkID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('firstGame', sa.DATE(), nullable=True),
    sa.Column('lastGame', sa.DATE(), nullable=True),
    sa.Column('games', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('openings', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('attendance', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parkID'], ['parks.parkID'], name='homegames_ibfk_1'),
    sa.PrimaryKeyConstraint('homegames_ID')
    )
    with op.batch_alter_table('homegames', schema=None) as batch_op:
        batch_op.create_index('k_hg_park', ['parkID'], unique=False)

    op.create_table('franchises',
    sa.Column('franchID', mysql.VARCHAR(length=3), nullable=False),
    sa.Column('franchName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('active', mysql.CHAR(length=1), nullable=True),
    sa.Column('NAassoc', mysql.VARCHAR(length=3), nullable=True),
    sa.PrimaryKeyConstraint('franchID')
    )
    op.create_table('halloffame',
    sa.Column('halloffame_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('votedBy', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('ballots', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('needed', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('votes', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('inducted', mysql.VARCHAR(length=1), nullable=True),
    sa.Column('category', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('note', mysql.VARCHAR(length=25), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fk_people'),
    sa.PrimaryKeyConstraint('halloffame_ID')
    )
    with op.batch_alter_table('halloffame', schema=None) as batch_op:
        batch_op.create_index('halloffame_playerID', ['playerID'], unique=False)

    op.create_table('pitchingpost',
    sa.Column('pitchingpost_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('round', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('p_W', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_L', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_CG', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SHO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SV', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_IPOuts', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('p_H', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_ER', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_HR', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BAOpp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('p_ERA', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('p_IBB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_WP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_HBP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BK', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BFP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_R', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SH', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GIDP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='pitchingpost_ibfk_1'),
    sa.PrimaryKeyConstraint('pitchingpost_ID')
    )
    with op.batch_alter_table('pitchingpost', schema=None) as batch_op:
        batch_op.create_index('pitchingpost_playerID_yearID_teamID', ['playerID', 'yearID', 'teamID'], unique=False)
        batch_op.create_index('k_pp_team', ['teamID'], unique=False)

    op.create_table('awardsshare',
    sa.Column('awardsshare_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('awardID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('lgID', mysql.CHAR(length=2), nullable=False),
    sa.Column('pointsWon', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('pointsMax', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('votesFirst', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fk_awdshr_peo'),
    sa.PrimaryKeyConstraint('awardsshare_ID')
    )
    op.create_table('seasonpitching',
    sa.Column('playerID', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('p_W', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_L', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_G', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_GS', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_CG', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_SHO', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_SV', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_IPOuts', mysql.DECIMAL(precision=32, scale=0), nullable=True),
    sa.Column('p_H', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_ER', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_HR', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_BB', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_SO', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_IBB', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_WP', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_HBP', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_BK', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_BFP', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_GF', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_R', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_SH', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_SF', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.Column('p_GIDP', mysql.DECIMAL(precision=27, scale=0), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='seasonpitching_ibfk_1'),
    sa.PrimaryKeyConstraint('playerID', 'yearID')
    )
    op.create_table('allstarfull',
    sa.Column('allstarfull_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('lgID', mysql.CHAR(length=2), nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('gameID', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('GP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('startingPos', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['lgID'], ['leagues.lgID'], name='allstarfull_ibfk_1'),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='allstarfull_ibfk_2'),
    sa.PrimaryKeyConstraint('allstarfull_ID')
    )
    with op.batch_alter_table('allstarfull', schema=None) as batch_op:
        batch_op.create_index('allstarfull_playerID', ['playerID'], unique=False)

    op.create_table('salaries',
    sa.Column('salaries_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearId', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('salary', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='salaries_ibfk_1'),
    sa.PrimaryKeyConstraint('salaries_ID')
    )
    with op.batch_alter_table('salaries', schema=None) as batch_op:
        batch_op.create_index('salaries_playerID', ['playerID'], unique=False)
        batch_op.create_index('key_team', ['teamID'], unique=False)

    op.create_table('managers',
    sa.Column('managers_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('inSeason', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('manager_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('manager_W', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('manager_L', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('teamRank', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('plyrMgr', mysql.VARCHAR(length=1), nullable=True),
    sa.Column('half', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fk_man_person'),
    sa.PrimaryKeyConstraint('managers_ID')
    )
    with op.batch_alter_table('managers', schema=None) as batch_op:
        batch_op.create_index('managers_playerID', ['playerID'], unique=False)

    op.create_table('fieldingpost',
    sa.Column('fieldingpost_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('round', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('position', mysql.VARCHAR(length=2), nullable=True),
    sa.Column('f_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_GS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_InnOuts', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_PO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_A', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_E', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_DP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_TP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('f_PB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fieldingpost_ibfk_1'),
    sa.PrimaryKeyConstraint('fieldingpost_ID')
    )
    with op.batch_alter_table('fieldingpost', schema=None) as batch_op:
        batch_op.create_index('k_fp_team', ['teamID'], unique=False)
        batch_op.create_index('fielding_playerID_yearID_teamID', ['playerID', 'yearID', 'teamID'], unique=False)

    op.create_table('battingpost',
    sa.Column('battingpost_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearId', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('round', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('b_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_AB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_R', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_H', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_2B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_3B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_HR', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_RBI', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_CS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_BB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_IBB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_HBP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SH', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_GIDP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='battingpost_ibfk_1'),
    sa.PrimaryKeyConstraint('battingpost_ID')
    )
    with op.batch_alter_table('battingpost', schema=None) as batch_op:
        batch_op.create_index('k_bp_team', ['teamID'], unique=False)
        batch_op.create_index('battingpost_playerID_yearID_teamID', ['playerID', 'yearId', 'teamID'], unique=False)

    op.create_table('batting',
    sa.Column('batting_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearId', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('stint', mysql.SMALLINT(display_width=4), autoincrement=False, nullable=False),
    sa.Column('b_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_AB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_R', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_H', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_2B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_3B', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_HR', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_RBI', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_CS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_BB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_IBB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_HBP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SH', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_SF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('b_GIDP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='batting_ibfk_1'),
    sa.PrimaryKeyConstraint('batting_ID')
    )
    with op.batch_alter_table('batting', schema=None) as batch_op:
        batch_op.create_index('k_bat_team', ['teamID'], unique=False)
        batch_op.create_index('batting_playerID_yearID_teamID', ['playerID', 'yearId', 'teamID'], unique=False)

    op.create_table('parks',
    sa.Column('parkID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('park_alias', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('park_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('state', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('parkID')
    )
    op.create_table('seriespost',
    sa.Column('seriespost_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('teamIDwinner', mysql.CHAR(length=3), nullable=False),
    sa.Column('teamIDloser', mysql.CHAR(length=3), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('round', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('wins', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('losses', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('ties', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('seriespost_ID')
    )
    with op.batch_alter_table('seriespost', schema=None) as batch_op:
        batch_op.create_index('seriespost_teamIDwinner_teamIDloser_yearid', ['teamIDwinner', 'teamIDloser', 'yearID'], unique=False)
        batch_op.create_index('k_sp_tw', ['teamIDwinner'], unique=False)
        batch_op.create_index('k_sp_tl', ['teamIDloser'], unique=False)

    op.create_table('collegeplaying',
    sa.Column('collegeplaying_ID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('schoolID', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='collegeplaying_ibfk_2'),
    sa.ForeignKeyConstraint(['schoolID'], ['schools.schoolId'], name='collegeplaying_ibfk_1'),
    sa.PrimaryKeyConstraint('collegeplaying_ID')
    )
    op.create_table('schools',
    sa.Column('schoolId', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('school_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('school_city', mysql.VARCHAR(length=55), nullable=True),
    sa.Column('school_state', mysql.VARCHAR(length=55), nullable=True),
    sa.Column('school_country', mysql.VARCHAR(length=55), nullable=True),
    sa.PrimaryKeyConstraint('schoolId')
    )
    op.create_table('divisions',
    sa.Column('divisions_ID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('divID', mysql.CHAR(length=2), nullable=False),
    sa.Column('lgID', mysql.CHAR(length=2), nullable=False),
    sa.Column('division_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('division_active', mysql.CHAR(length=1), nullable=False),
    sa.ForeignKeyConstraint(['lgID'], ['leagues.lgID'], name='divisions_ibfk_1'),
    sa.PrimaryKeyConstraint('divisions_ID')
    )
    with op.batch_alter_table('divisions', schema=None) as batch_op:
        batch_op.create_index('divisions_divID', ['divID'], unique=False)
        batch_op.create_index('divID', ['divID', 'lgID'], unique=False)

    op.create_table('awards',
    sa.Column('awards_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('awardID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('lgID', mysql.CHAR(length=2), nullable=False),
    sa.Column('tie', mysql.VARCHAR(length=1), nullable=True),
    sa.Column('notes', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='fk_awd_peo'),
    sa.PrimaryKeyConstraint('awards_ID')
    )
    op.create_table('leagues',
    sa.Column('lgID', mysql.CHAR(length=2), nullable=False),
    sa.Column('league_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('league_active', mysql.CHAR(length=1), nullable=False),
    sa.PrimaryKeyConstraint('lgID')
    )
    op.create_table('pitching',
    sa.Column('pitching_ID', mysql.INTEGER(display_width=12), autoincrement=True, nullable=False),
    sa.Column('playerID', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('yearID', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('teamID', mysql.CHAR(length=3), nullable=False),
    sa.Column('stint', mysql.SMALLINT(display_width=4), autoincrement=False, nullable=False),
    sa.Column('p_W', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_L', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_G', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GS', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_CG', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SHO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SV', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_IPOuts', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('p_H', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_ER', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_HR', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SO', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BAOpp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('p_ERA', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('p_IBB', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_WP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_HBP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BK', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_BFP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_R', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SH', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_SF', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('p_GIDP', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['playerID'], ['people.playerID'], name='pitching_ibfk_1'),
    sa.PrimaryKeyConstraint('pitching_ID')
    )
    with op.batch_alter_table('pitching', schema=None) as batch_op:
        batch_op.create_index('pitching_playerID_yearID_teamID', ['playerID', 'yearID', 'teamID'], unique=False)
        batch_op.create_index('k_pit_team', ['teamID'], unique=False)

    # ### end Alembic commands ###
