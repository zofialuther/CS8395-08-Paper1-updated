import Data.List
import qualified Data.ByteString.Char8 as B

allPokemon = [B.pack(word) for word in "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask".split()]

def growChains(pcs):
    if not nextChainSet:
        return pcs[0]
    else:
        return growChains(nextChainSet)

    nextChainSet = [findLinks(pc) for pc in pcs]
    findLinks(pc):
        return [pc + [x] for x in filter(lambda x: isLink(pc[-1], x), list(set(allPokemon) - set(pc)))]
    isLink(pl, pr):
        return pl[-1] == pr[0]

main = [B.putStrLn(x) for x in growChains([[x] for x in allPokemon])]
