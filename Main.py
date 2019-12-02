from Parliament import Parliament
from PoliticalParty import PoliticalParty
from Ploter import *

if __name__ == '__main__':
    THRESHOLD = 0.5

    political_parties = [
        PoliticalParty(name='PartyA', parlament_percentage=0.20),
        PoliticalParty(name='PartyB', parlament_percentage=0.20),
        PoliticalParty(name='PartyC', parlament_percentage=0.20),
        PoliticalParty(name='PartyD', parlament_percentage=0.20),
        PoliticalParty(name='PartyE', parlament_percentage=0.20)
    ]

    parliament = Parliament(parties=political_parties)
    party_params_dic, coalitions = parliament.get_parties_properties(threshold=THRESHOLD)

    plot_shapley(party_params_dic)
    plot_occurrences(party_params_dic)
    plot_shares(political_parties)