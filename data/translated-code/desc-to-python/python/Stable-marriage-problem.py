```python
class StableMarriage:
    def __init__(self):
        self.guys_preferences = {
            'guy1': ['gal1', 'gal2', 'gal3'],
            'guy2': ['gal2', 'gal1', 'gal3'],
            'guy3': ['gal3', 'gal1', 'gal2']
        }
        self.gals_preferences = {
            'gal1': ['guy3', 'guy2', 'guy1'],
            'gal2': ['guy1', 'guy3', 'guy2'],
            'gal3': ['guy2', 'guy1', 'guy3']
        }
        self.engagements = {}

    def matchmaker(self):
        free_guys = list(self.guys_preferences.keys())
        while free_guys:
            guy = free_guys.pop(0)
            gal = self.guys_preferences[guy].pop(0)
            fiance = self.engagements.get(gal)
            if not fiance:
                self.engagements[gal] = guy
            else:
                gal_preferences = self.gals_preferences[gal]
                if gal_preferences.index(guy) < gal_preferences.index(fiance):
                    self.engagements[gal] = guy
                    free_guys.append(fiance)
                else:
                    free_guys.append(guy)

    def check_stability(self):
        for gal, guy in self.engagements.items():
            gal_preferences = self.gals_preferences[gal]
            rival_guys = gal_preferences[:gal_preferences.index(guy)]
            for rival_guy in rival_guys:
                rival_gals_fiance = self.engagements[rival_guy]
                if self.guys_preferences[rival_guy].index(gal) < self.guys_preferences[rival_guy].index(rival_gals_fiance):
                    print("Unstable match found")
                    return

        print("All matches are stable")

sm = StableMarriage()
sm.matchmaker()
print("Engagements:", sm.engagements)
sm.check_stability()
```