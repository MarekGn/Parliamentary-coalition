import matplotlib.pyplot as plt


def plot_shapley(party_params_dic):
    names = [party_name for party_name in party_params_dic]
    shapleys = [party_params_dic[party_name]["shapley"] for party_name in party_params_dic]

    plt.xlabel('Shapley value (-)')
    plt.ylabel('Party name')
    plt.title('Parties Shapley values')
    for i, v in enumerate(shapleys):
        plt.text(v+0.005, i, str(v),  fontsize=10)

    plt.barh(names, shapleys, height=0.5, color="darkblue")
    plt.show()


def plot_occurrences(party_params_dic):
    names = [party_name for party_name in party_params_dic]
    shapleys = [party_params_dic[party_name]["occurrences"] for party_name in party_params_dic]

    plt.xlabel('Party occurrence (-)')
    plt.ylabel('Party name')
    plt.title('Parties occurrences in possible in possible coalitions')

    for i, v in enumerate(shapleys):
        plt.text(v+0.15, i, str(v),  fontsize=10)

    plt.barh(names, shapleys, height=0.5, color="darkblue")
    plt.show()

