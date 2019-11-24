from itertools import permutations
from copy import copy


class Parliament:

    def __init__(self, parties):
        self.parties = parties

    def get_parties_properties(self, threshold):
        '''Function calculating dictionary with shapley value for each party in given array, each party occurrences in
         possible coalitions and calculating array of those possible coalitions'''
        # generate all possible permutations
        permutations_ = permutations(self.parties)
        coalitions = []
        parties_dic = {}
        self._add_parties_properties_dict(parties_dic)
        # permutation amount for shapley calculations
        permutations_amount = len(list(copy(permutations_)))
        for permutation in permutations_:
            for parties_amount in range(1, len(permutation)+1):
                possible_coalition = [party.name for party in permutation[:parties_amount]]
                parliament_score = sum([party.parlament_percentage for party in permutation[:parties_amount]])
                if parliament_score > threshold:
                    parties_dic[permutation[parties_amount-1].name]["occurrences"] += 1
                    if sorted(possible_coalition) not in coalitions:
                        coalitions.append(possible_coalition)
                    break
        self._calculate_shapley(parties_dic=parties_dic, permutations_amount=permutations_amount)
        return parties_dic, coalitions

    def _add_parties_properties_dict(self, parties_dic):
        for party in self.parties:
            parties_dic[party.name] = {"shapley": None,
                                       "occurrences": 0}

    def _calculate_shapley(self, parties_dic, permutations_amount):
        for party in self.parties:
            parties_dic[party.name]["shapley"] = parties_dic[party.name]["occurrences"] / permutations_amount