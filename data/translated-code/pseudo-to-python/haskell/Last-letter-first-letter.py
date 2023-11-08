import Data.List
import qualified Data.ByteString.Char8 as B

allPokemon = list(map(B.pack, "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon \
    \cresselia croagunk darmanitan deino emboar emolga exeggcute gabite \
    \girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan \
    \kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine \
    \nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 \
    \porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking \
    \sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko \
    \tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"))

def growChains(pcs):
    if not nextChainSet:
        return pcs[0]
    else:
        return growChains(nextChainSet)
    nextChainSet = [findLinks(pc) for pc in pcs]
    findLinks(pc):
        return [pc + [x] for x in list(filter(lambda pr: B.last(pc[-1]) == B.head(pr), list(filter(lambda p: p not in pc, allPokemon))))]

main = list(map(B.putStrLn, growChains(list(map(lambda x: [x], allPokemon))))