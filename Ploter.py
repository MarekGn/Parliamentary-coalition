import matplotlib.pyplot as plt
import InitParams

def plot_shapley(party_params_dic):
    names = [party_name for party_name in party_params_dic]
    shapleys = [party_params_dic[party_name]["shapley"] for party_name in party_params_dic]

    plt.xlabel('Shapley value (-)')
    plt.ylabel('Party name')
    plt.title('Parties Shapley values')
    for i, v in enumerate(shapleys):
        plt.text(v, i, str(format(v, '0.2f')),  fontsize=8)

    plt.barh(names, shapleys, height=0.5, color="darkblue")
    plt.tight_layout()
    plt.savefig("shapley.jpg")
    plt.show()
    plt.clf()


def plot_occurrences(party_params_dic):
    names = [party_name for party_name in party_params_dic]
    shapleys = [party_params_dic[party_name]["occurrences"] for party_name in party_params_dic]

    plt.xlabel('Party occurrence (-)')
    plt.ylabel('Party name')
    plt.title('Parties occurrences in possible coalitions')

    for i, v in enumerate(shapleys):
        plt.text(v, i, str(v),  fontsize=8)

    plt.barh(names, shapleys, height=0.5, color="darkblue")
    plt.tight_layout()
    plt.savefig("occurences.jpg")
    plt.show()
    plt.clf()


def plot_shares(political_parties):
    names = [party.name for party in political_parties]
    shapleys = [party.parlament_percentage for party in political_parties]

    plt.xlabel('Party share (-)')
    plt.ylabel('Party name')
    plt.title('Parliament shares distribution')

    for i, v in enumerate(shapleys):
        plt.text(v, i, str(v),  fontsize=8)

    plt.barh(names, shapleys, height=0.5, color="darkblue")
    plt.tight_layout()
    plt.savefig("shares.jpg")
    plt.show()
    plt.clf()
